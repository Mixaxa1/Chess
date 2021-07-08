using System;
using System.Drawing;
using System.Windows.Input;
using System.Collections.Generic;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using System.Windows.Forms;


namespace GameLoopProject
{
    class Game
    {
        private ScriptEngine engine;
        private ScriptSource source;
        private ScriptScope scope;

        private GameSprite sprite;
        private List<GameSprite> figures_sprites = new List<GameSprite>();
        private dynamic board;

        public Size Resolution { get; set; }

        public Game()
        {
            this.engine = Python.CreateEngine();
            this.source = this.engine.CreateScriptSourceFromFile("board.py");
            this.scope = this.engine.CreateScope();
            this.source.Execute(this.scope);
        }

        public void Load()
        {
            dynamic Board_object = scope.GetVariable("Board");
            dynamic Board_instance = Board_object();
            this.board = Board_instance.generate_board();

            List<GameSprite> figures_sprites = new List<GameSprite>();
            int size = 42;

            for (int row = 0; row < 8; row++)
            {
                for (int col = 0; col < 8; col++)
                {
                    if (board[row][col].figure != null)
                    {
                        dynamic figure = board[row][col].figure;
                        GameSprite sprite = new GameSprite();

                        sprite.SpriteImage = (Bitmap)Chess.Properties.Resources.ResourceManager.GetObject(figure.sprite);
                        sprite.X = figure.cords[0];
                        sprite.Y = figure.cords[1];
                        sprite.Width = size;
                        sprite.Height = size;

                        this.figures_sprites.Add(sprite);
                    }
                }
            }
        }

        public void Update()
        {
        }

        public void Draw(Graphics gfx)
        {
            Draw_Board(gfx);
            Draw_Figures(gfx);
        }

        public void Draw_Figures(Graphics gfx)
        {
            for (int i = 0; i < this.figures_sprites.Count; i++)
            {
                this.figures_sprites[i].Draw(gfx);
            }
        }

        public void Draw_Board(Graphics gfx)
        {
            for (int row = 0; row < 8; row++)
            {
                for (int col = 0; col < 8; col++)
                {
                    if (this.board[row][col].color == "white")
                    {
                        gfx.FillRectangle(new SolidBrush(Color.White), new Rectangle(row * 50, col * 50, 50, 50));
                    }
                    else
                    {
                        gfx.FillRectangle(new SolidBrush(Color.Maroon), new Rectangle(row * 50, col * 50, 50, 50));
                    }
                }
            }

        }
    }
}
