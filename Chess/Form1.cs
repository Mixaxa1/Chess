using System;
using System.Drawing;
using System.Windows.Forms;

namespace GameLoopProject
{
    public partial class Form1 : Form
    {
        Timer graphicsTimer;
        GameLoop gameLoop;

        public Form1()
        {
            InitializeComponent();
            // Initialize Paint Event
            Paint += Form1_Paint;
            // Initialize graphicsTimer
            graphicsTimer = new Timer();
            graphicsTimer.Interval = 1000 / 120;
            graphicsTimer.Tick += GraphicsTimer_Tick;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Rectangle resolution = Screen.PrimaryScreen.Bounds;

            // Initialize Game
            Game myGame = new Game();
            myGame.Resolution = new Size(resolution.Width, resolution.Height);

            // Initialize & Start GameLoop
            gameLoop = new GameLoop();
            gameLoop.Load(myGame);
            gameLoop.Start();

            // Start Graphics Timer
            graphicsTimer.Start();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // Draw game graphics on form
            gameLoop.Draw(e.Graphics);
        }

        private void GraphicsTimer_Tick(object sender, EventArgs e)
        {
            // Refresh form graphics
            Invalidate();
        }
    }
}
