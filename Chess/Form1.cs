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

            Paint += Form1_Paint;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Game myGame = new Game();
            myGame.Resolution = new Size(400, 400);

            gameLoop = new GameLoop();
            gameLoop.Load(myGame);
            gameLoop.Start();

        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            gameLoop.Draw(e.Graphics);
        }

        private void Form1_Click(object sender, EventArgs e)
        {
            Invalidate();
        }
    }
}
