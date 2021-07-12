using System;
using System.Diagnostics;
using System.Drawing;
using System.Windows.Forms;

namespace GameLoopProject
{
    public partial class Form1 : Form
    {
        Game myGame;

        public Form1()
        {
            InitializeComponent();

            Paint += Form1_Paint;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Size size = new Size(400, 450);

            myGame = new Game();
            myGame.Resolution = size;
            myGame.Load();

            TurnLabel.Text = "Ход белых";
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            myGame.Draw(e.Graphics);
        }

        private void Form1_Click(object sender, EventArgs e)
        {
            Point pos = Cursor.Position;
            string turn;

            Debug.WriteLine(PointToClient(pos));
            turn = myGame.Update(PointToClient(pos));

            if (turn == "white")
            {
                TurnLabel.Text = "Ход белых";
            }
            else
            {
                TurnLabel.Text = "Ход черных";
            }

            Invalidate();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
