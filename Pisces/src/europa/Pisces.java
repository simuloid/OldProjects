/*
 * Main.java
 *
 * Created on December 9, 2008, 9:09 AM
 *
 * To change this template, choose Tools | Template Manager
 * and open the template in the editor.
 */

package europa;

import java.awt.AWTException;
import java.awt.GridLayout;
import java.awt.Point;
import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.MouseEvent;
import java.awt.image.BufferedImage;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSlider;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.text.BadLocationException;

/**
 * This is the main (and only) class for the World of Warcraft fishing bot.
 * To use the bot, you must do the following:
 * <OL>
 * <LI>Run the game in windowed mode, 800x600, position the WoW window in the upper left corner
 *   of the primary display.</LI>
 * <LI>In game, equip your fishing pole and set the Fishing power to be activated by the 1 key.</LI>
 * <LI>In the game, position your character facing water and scroll the view so that you have a
 *   first-person view.</LI>
 * </OL>
 * @author stever
 */
public class Pisces extends JFrame implements Runnable, ChangeListener
{
    /**
     * The mechanism by which the program communicates with WoW.
     */
    Robot m_robby;
    /**
     * This is the factor by which the amount of red in the lure's feather exceeds the amount of blue and green.
     * If the bot can't find the lure (which causes it to automatically re-cast) make this number lower.
     * If the bot is pointing at some strange place on the screen, make this number higher.
     */
     double RED_FACTOR = 2.2;
    /**
     * This is the factor by which the amount of red in the lure's vicinity needs to change to trigger the bot to retrieve the fish.
     * If the bot is reeling in when no fish are hooked, make this number bigger.
     * If the bot is not responding when a fish strikes, make this number smaller.
     */
     double BOB_FACTOR = 0.5;

    /**
     * The slider used to change the RED_FACTOR
     */
     JSlider m_redSlider;

    /**
     * The slider used to change the BOB_FACTOR
     */
     JSlider m_bobSlider;

     /**
      * The window wherein status messages are displayed.
      */
     JTextField m_messageWindow;
    private JCheckBox paused;

    ActionListener checkboxHandler = new ActionListener() {

        @Override
        public void actionPerformed(ActionEvent ae) {
            System.out.println(paused.isSelected());
            transition = !paused.isSelected();
        }
        
    };
    private boolean transition;
    private long m_lastMoveTime;
    /** Creates a new instance of the FishBot */
    public Pisces()
    {
        super("Graphics");
        try {
            setSize(200,200);
            setLocation(810,0);
            setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            getContentPane().setLayout(new GridLayout(3, 1));
            getContentPane().add(makeSliderPanel());

            m_messageWindow = makeTextArea();
            paused = new JCheckBox("Paused", true);
            paused.addActionListener(checkboxHandler);
            getContentPane().add(paused);
            getContentPane().add(new JScrollPane(m_messageWindow));

            pack();
            m_robby = new Robot();
        } catch (AWTException ex) {
            ex.printStackTrace();
        }
    }

    /**
     * Utility method to create the text area to display status messages.
     *
     * @return The newly created text area.
     */
    final JTextField makeTextArea()
    {
        JTextField rc = new JTextField();
 //       rc.setLineWrap(true);
        rc.setEditable(false);
        rc.setFocusable(false);

        return rc;
    }

    /**
     * Append a message line to the message window.  Automatically keep the
     * cursor at the bottom of the window.
     *
     * @param msg The message to append to the window.
     */
    void addMessage(String msg)
    {
        if (m_messageWindow != null && m_messageWindow instanceof JTextField) {
            m_messageWindow.setText(msg);
        }
        /*
        try {
            m_messageWindow.append(msg);
            m_messageWindow.append("\n");
            int lineNo = m_messageWindow.getLineCount();
            if (lineNo > 1)
            {
                int position = m_messageWindow.getLineEndOffset(lineNo - 1);
                m_messageWindow.setCaretPosition(position);
            }
        } catch (BadLocationException ex) {
            Logger.getLogger(FishBot.class.getName()).log(Level.SEVERE, null, ex);
        }
        */
    }


    /**
     * Utility method to create the panel containing the paramater sliders.
     *
     * @return A JPanel containing the labeled sliders.
     */
    final JPanel makeSliderPanel()
    {
        JPanel p = new JPanel();
        p.setLayout(new GridLayout(4, 1));
        p.add(new JLabel("Contrast"));
        m_redSlider = makeSlider(1, 3, RED_FACTOR);
        p.add(m_redSlider);
        p.add(new JLabel("Sensitivity"));
        m_bobSlider = makeSlider(0, 1, BOB_FACTOR);
        p.add(m_bobSlider);

        return p;
    }

    /**
     * Utility method to create and initialize a slider.  Automatically adds slider to the listener list.
     * @param min Minimum value for the slider, floating point with 0.1 precision.
     * @param max Maximum value for the slider, floating point with 0.1 precision.
     * @param init Initial value for the slider, floating point with 0.1 precision.
     * @return The newly created slider.
     */
    JSlider makeSlider(double min, double max, double init)
    {
        JSlider rc = new JSlider();
        rc.setMaximum((int) (max * 10));
        rc.setMinimum((int) (min * 10));
        rc.setValue((int) (init * 10));
        rc.addChangeListener(this);
        return rc;
    }



    /**
     * Standard callback for slider change events.
     * @param e The event representing the change to the slider.
     */
    //@Override
    public void stateChanged(ChangeEvent e)
    {
        JSlider source = (JSlider) e.getSource();
        int value = source.getValue();
        if (source == m_redSlider)
        {
            RED_FACTOR = 0.1 * value;
        }
        else if (source == m_bobSlider)
        {
            BOB_FACTOR = 0.1 * value;
        }
    }

    /**
     * Over-ride of the standard setVisible method to also start a thread running the run method.
     * @param viz if true, set the window to visible.  Else set it invisible.
     */
    @Override
    public void setVisible(boolean viz)
    {
        super.setVisible(viz);
        Thread t = new Thread(this);
        t.start();
    }

    /**
     * This flag indicates when it is time to exit the main loop of the run() method.
     */
    boolean m_done;

    /**
     * Used by the main loop in run() to determine if it should continue.
     * @return true if the main loop should exit, false if it should continue.
     */
    boolean isDone()
    {
        return m_done;
    }

    /**
     * Given a picture of the scene in front of the character, find the bobber.
     * This works by finding all the (very) red pixels of the red feather on the bobber, and returning
     * the centroid of all those red pixels.  Beware if there are other red things in the scene, like
     * monster names, red flowers, etc.
     * @param img The buffered image to search for the bobber in.
     * @return The point that is the centroid of the red feather, if it is found.  If it is not found
     * the point (0,0) is returned.
     */
    Point findBobber(BufferedImage img)
    {
        Point p = new Point();
        double bobberX = -1;
        double bobberY = -1;

        for (int y = 50; y < img.getHeight(); ++y)
        {
            for (int x = 0; x < img.getWidth(); ++x)
            {
                try
                {
                    int pixel = img.getRGB(x,y);
                    if (isRed(pixel))
                    {
                        // addMessage("x,y = " + x + "," + y + "  r,g,b = " + r + ", " + g + ", " + b);
                        //img.setRGB(x, y, 0xffffff);
                        if (bobberX < 0)
                        {
                            bobberX = x;
                        }
                        else
                        {
                            bobberX = 0.9 * bobberX + 0.1 * x;
                        }

                        if (bobberY < 0)
                        {
                            bobberY = y;
                        }
                        else
                        {
                            bobberY = 0.9 * bobberY + 0.1 * y;
                        }
                    }
                }

                catch (Exception ex)
                {
                    System.err.println("Exception at coords " + x + "," + y + " : " + ex);
                }
            }
        }

        if (bobberX > 0)
        {
            p = new Point((int) bobberX, (int) bobberY);
        }
        //displayImage(img);
        return p;
    }

    /**
     * Determines if the given pixel is red, as defined by the RED_FACTOR parameter.
     * @param pixel The pixel to examine.  It is assumed to be a 24-bit RGB value.
     * @return true if the pixel is red, false if it is not.
     */
    boolean isRed(int pixel)
    {
        int r = (pixel & 0xff0000) >> 16;
        int g = (pixel & 0x00ff00) >> 8;
        int b = (pixel & 0x0000ff);
        return (r > g*RED_FACTOR && r > b*RED_FACTOR);
    }

    /**
     * Returns the number of red pixels in the given image.
     * @param img The image to count red pixels in.
     * @return The number of red pixels in the image.
     */
    int getAmountOfRed(BufferedImage img)
    {
        int redCount = 0;

        for (int y = 0; y < img.getHeight(); ++y)
        {
            for (int x = 0; x < img.getWidth(); ++x)
            {
                int pixel = img.getRGB(x, y);
                if (isRed(pixel))
                {
                    ++redCount;
                }
           }
        }

        return redCount;
    }

    /**
     * Given a "from" point and a "to" point, break the path between them into small pieces and feed them to the even system.
     * Also adds a sinusoidal path perturbation.  This is solely for the benefit of being less detectable.
     * @param from The point that the mouse is moving from.
     * @param to The point that the mouse is to be moved to.
     */
    void moveMouseTo(Point from, Point to)
    {
        double dx = (to.x - from.x);
        double dy = (to.y - from.y);
        int pixelDistance = (int) Math.max(Math.abs(dx), Math.abs(dy));
        int segments = (int) Math.max(10, Math.min(100, 0.2 * pixelDistance));
        dx = dx / segments;
        dy = dy / segments;

       for (int i = 0; i < segments; ++i)
        {
            m_robby.mouseMove((int) (from.x + dx * i + Math.sin(Math.PI * i / segments) * pixelDistance/2), (int) (from.y + dy * i + Math.sin(Math.PI * i/segments) * pixelDistance/2));
           m_robby.delay(10);
        }

        m_robby.mouseMove(to.x, to.y);
    }

    /**
     * Sends the events to WoW necessary to cause a fishing cast.
     * In this case, that means typing the 1 key.
     * The random pauses are used to keep the events from having timings that are "too perfect".
     */
    void cast()
    {
        m_robby.keyPress(KeyEvent.VK_1);
        m_robby.delay((int) (Math.random() * 20 + 10));
        m_robby.keyRelease(KeyEvent.VK_1);
        m_robby.delay((int) (Math.random() * 20 + 10));
    }

    boolean guiVisible = true;
    
    void setUIVisible(boolean vis) {
        if (guiVisible != vis) {
            toggleUIVisibility();
        }
    }
    
    void toggleUIVisibility() {
        m_robby.keyPress(KeyEvent.VK_ALT);
        m_robby.delay((int) (Math.random() * 20 + 10));
        m_robby.keyPress(KeyEvent.VK_Z);
        m_robby.delay((int) (Math.random() * 20 + 100));
        m_robby.keyRelease(KeyEvent.VK_Z);
        m_robby.delay((int) (Math.random() * 20 + 10));
        m_robby.keyRelease(KeyEvent.VK_ALT);
        m_robby.delay((int) (Math.random() * 20 + 10));
    }
    void toggleBagVisibility() {
        m_robby.keyPress(KeyEvent.VK_B);
        m_robby.delay((int) (Math.random() * 20 + 100));
        m_robby.keyRelease(KeyEvent.VK_B);
        m_robby.delay((int) (Math.random() * 20 + 10));
    }
    void toggleSkillVisibility() {
        m_robby.keyPress(KeyEvent.VK_K);
        m_robby.delay((int) (Math.random() * 20 + 100));
        m_robby.keyRelease(KeyEvent.VK_K);
        m_robby.delay((int) (Math.random() * 20 + 10));
    }
    /**
     * Sends the events to WoW necessary to hook the fish.  In this case, this means clicking the right
     * mouse button.  Random pauses are used to simulate imperfect human reflexes.
     */
    void hookIt()
    {
        // Hook
        //m_robby.keyPress(KeyEvent.VK_SHIFT);
        //m_robby.delay(randInt(5,20));
        m_robby.mousePress(MouseEvent.BUTTON3_MASK);
        m_robby.delay(randInt(10, 30));
        m_robby.mouseRelease(MouseEvent.BUTTON3_MASK);
        m_robby.delay(randInt(20,30));
        //m_robby.keyRelease(KeyEvent.VK_SHIFT);
       // m_robby.delay(randInt(10, 30));
    }

    public void jump() {
        int[] wsad = { KeyEvent.VK_W,  KeyEvent.VK_A, KeyEvent.VK_S, KeyEvent.VK_D };
        int key = wsad[randInt(0, 4)];
        m_robby.keyPress(key);
        m_robby.delay(20);
        m_robby.keyRelease(key);
//        m_robby.delay(randInt(1000, 1100));
        m_lastMoveTime = System.currentTimeMillis();
    }

   static int randInt(int max) {
      return randInt(0, max);
   }

   static int randInt(int min, int max) {
      return (int) (Math.random() * (max - min) + min);
   }
   
   void activateWindow() {
        m_robby.delay(1000);
        m_robby.mouseMove(100, 10);
        m_robby.mousePress(MouseEvent.BUTTON1_MASK);
        m_robby.delay(20);
        m_robby.mouseRelease(MouseEvent.BUTTON1_MASK);
        m_robby.delay(100);
        m_robby.mouseMove(100, 100);
   }
    /**
     * This is the main fishing loop.
     */
    //@Override
    public void run() {
        //testNibble();

        m_done = false;
        Point lastP = new Point();
        BufferedImage b;
        //displayImage(b);

        while (!isDone())
        {
            if (transition) {
                activateWindow();
                transition = false;
            }
            // Pause before re-casting.
            if (paused.isSelected()) {
                addMessage("Paused.");
                m_robby.delay(randInt(200, 300));
                continue;
            }
            addMessage("Waiting.");
            toggleUIVisibility();
            toggleBagVisibility();
            toggleSkillVisibility();
            m_robby.delay(randInt(5000, 6000));
            toggleUIVisibility();
            addMessage("Casting..."); // Casting
            if (paused.isSelected()) continue;
            if ((System.currentTimeMillis() - m_lastMoveTime) > 120000) {
                jump();
            }
             cast();
//                toggleUIVisibility();
             m_robby.delay(randInt(2900, 3100));
             b = m_robby.createScreenCapture(new Rectangle(0, 20, 700, 400));
//                toggleUIVisibility();
             Point p = findBobber(b);
             if (p.x == 0 && p.y == 0)
             {
                 // Can't find bobber.  Recast.
                addMessage("Recasting."); // Can't find bobber.  Recasting'
                 continue;
             }
             Point p2 = new Point(p.x, p.y+20);
             moveMouseTo(lastP, p2);
             lastP = p2;
             // m_robby.delay(1000);
             // Wait for nibble
             b = m_robby.createScreenCapture(new Rectangle(p.x, p.y-25, 50, 50));
             int baseRed = getAmountOfRed(b);
             addMessage("Base redness: " + baseRed);
             BufferedImage other;
             boolean fishHooked = false;
             for (int n = 0; n < 400; ++n)
             {
                 m_robby.delay(50);
                 b = m_robby.createScreenCapture(new Rectangle(p.x, p.y-25, 50, 50));
                 int curRed = getAmountOfRed(b);
                 addMessage("Cur redness: " + curRed);
                 if (curRed < (BOB_FACTOR * baseRed))
                 {
                     addMessage("Hooked!");
                     fishHooked = true;
                     break;
                 }
                if (paused.isSelected()) break;
                 //baseBrightness = curRed;
             }

            if (paused.isSelected()) continue;
            
             if (fishHooked)
             {
                 m_robby.delay(randInt(100, 500));
                 hookIt();
                 m_robby.delay(randInt(1000, 1300));
             }

            Point random = new Point(randInt(500), randInt(500));

            moveMouseTo(lastP, random);
            lastP = random;
        }
    }

    /**
     * Call this method to stop the loop in the run() method.
     */
    synchronized void quit()
    {
        m_done = true;
    }

    /**
     * This is the entry point of the program.  It just creates an instance of the fishing
     * bot and starts it running.
     * @param args The command line arguments.  These are currently ignored.
     */
    public static void main(String[] args) {
        // NOTE: To see the program work without running WoW, uncomment the
        // line with FishTarget in it below.
//        FishTarget t = new FishTarget();
        Pisces f = new Pisces();
        f.setVisible(true);
    }

}
