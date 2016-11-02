/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package europa;

import javax.swing.Action;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.Timer;
import java.util.TimerTask;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import javax.swing.AbstractAction;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.KeyStroke;

/**
 * FishTarget is a little application that pretends to be world of warcraft
 * in order to demonstrate the fishing bot program.
 *
 * @author Steve Rowe <srowe at cybernet.com>
 */
public class FishTarget extends JFrame
{
    /**
     * Image of what the scene looks like with no bobber
     */
    Image m_noBobber;


    /**
     * Image of what the scene looks like with a bobber but no fish.
     */
    Image m_bobber;

    /**
     * Image of what the scene looks like when a fish strikes.
     */
    Image m_strike;

    ImagePane m_imager;

    Timer m_strikeTimer = new Timer();

    TimerTask m_fishStrike;
    TimerTask m_noHook;

    /**
     * Construct a new FishTarget application.
     */
    public FishTarget()
    {
        super("NOT World of Warcraft");
        setSize(800, 600);
        setLocation(0,0);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        try
        {
            m_noBobber = ImageIO.read(ClassLoader.getSystemResource("fish07.jpg"));
            m_bobber = ImageIO.read(ClassLoader.getSystemResource("fish08.jpg"));
            m_strike = ImageIO.read(ClassLoader.getSystemResource("fish09.jpg"));
            m_imager = new ImagePane(m_noBobber);
            getContentPane().add(m_imager);
            m_imager.setEnabled(true);
            m_imager.requestFocusInWindow();
            setVisible(true);
        }
        catch (Exception x)
        {
            System.err.println("Couldn't load images: " + x);
            x.printStackTrace(System.err);
            System.exit(1);
        }
    }

    /**
     * Class for displaying an image as a JComponent.
     * This one contains handlers for mouse and key events.
     */
    class ImagePane extends JComponent implements KeyListener, MouseListener
    {
        /**
         * The image to display in the pane.
         */
        Image m_img; // = ImageIO.read(new File("fish04.jpg"));

        /**
         * Make a new ImagePane
         *
         * @param img The image to display
         */
        ImagePane(Image img)
        {
            m_img = img;
            setRequestFocusEnabled(true);
            addKeyListener(this);
            addMouseListener(this);
            registerKeyboardAction(castAction,
		KeyStroke.getKeyStroke(KeyEvent.VK_1, 0),
		JComponent.WHEN_FOCUSED);
            // System.out.println("Registered: " + this.getRegisteredKeyStrokes());
        }


        /**
         * Change the image to display.
         * @param img
         */
        public void setImage(Image img)
        {
            m_img = img;
            repaint();
        }

        @Override
        public Dimension getPreferredSize()
        {
            return new Dimension(m_img.getWidth(this), m_img.getHeight(this));
        }

        @Override
        public void paint(Graphics g)
        {
            g.drawImage(m_img, 0, 0, this);
        }

        @Override
        public void keyTyped(KeyEvent e)
        {
            //System.out.println("Key typed: " + e);
            if (e.getKeyChar() == '1')
            {
                System.out.println("Cast Detected.");
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException ex) {
                    Logger.getLogger(FishTarget.class.getName()).log(Level.SEVERE, null, ex);
                }
                m_imager.setImage(m_bobber);
                m_noHook = new TimerTask()
                {
                    public void run()
                    {
                        m_imager.setImage(m_noBobber);
                        System.out.println("No fish were hooked.");
                    }
                };

                m_strikeTimer.schedule(m_noHook, 16000);
                m_fishStrike = new TimerTask()
                {
                    public void run()
                    {
                        m_imager.setImage(m_strike);
                        try {
                            Thread.sleep(100);
                        } catch (InterruptedException ex) {
                            Logger.getLogger(FishTarget.class.getName()).log(Level.SEVERE, null, ex);
                        }
                        m_imager.setImage(m_bobber);
                    }
                };

                m_strikeTimer.schedule(m_fishStrike, (int) (Math.random() * 2000) + 7000);
            }
        }

        @Override
        public void keyPressed(KeyEvent e) {
            //System.out.println("Key Pressed: " + e);
        }

        @Override
        public void keyReleased(KeyEvent e) {
            //System.out.println("Key Release: " + e);
        }

        @Override
        public void mouseClicked(MouseEvent e)
        {
            if (e.getButton() == MouseEvent.BUTTON3)
            {
                System.out.println("Retrieve Detected");
                m_noHook.cancel();
                m_strikeTimer.purge();
                m_imager.setImage(m_noBobber);
            }
        }

        @Override
        public void mousePressed(MouseEvent e)
        {
        }

        @Override
        public void mouseReleased(MouseEvent e) {
        }

        @Override
        public void mouseEntered(MouseEvent e) {
        }

        @Override
        public void mouseExited(MouseEvent e) {
        }
    }


    public Action castAction = new AbstractAction("Cast")
    {
        public void actionPerformed(ActionEvent e)
        {
        }
    };

    /**
     * Create a frame and display an image in it using the ImagePane component.
     * @param img The image to display.
     */
    void displayImage(Image img)
    {
        JFrame f = new JFrame("The Picture");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ImagePane icon = new ImagePane(img);
        f.getContentPane().add(icon);
        f.pack();
        icon.requestFocusInWindow();
        f.setVisible(true);
    }

    public static void main(String[] args)
    {
        FishTarget t = new FishTarget();
    }
}
