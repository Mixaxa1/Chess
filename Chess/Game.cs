using System;
using System.Drawing;
using System.Windows.Input;
using System.Collections.Generic;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using System.Windows.Forms;
using System.Diagnostics;

namespace GameLoopProject
{
    class Game
    {
        private ScriptEngine engine;
        private ScriptSource source;
        private ScriptScope scope;
        private dynamic instance;
        private dynamic game;

        private List<GameSprite> figures_sprites = new List<GameSprite>();
        private dynamic board;

        public Size Resolution { get; set; }

        public Game()
        {
            engine = Python.CreateEngine();
            source = engine.CreateScriptSourceFromFile("Game.py");
            scope = engine.CreateScope();
            source.Execute(scope);

            instance = scope.GetVariable("Game");
            game = instance();
        }

        public void Load()
        {
            this.board = game.get_board();

            List<GameSprite> figures_sprites = new List<GameSprite>();

            for (int row = 0; row < 8; row++)
            {
                for (int col = 0; col < 8; col++)
                {
                    if (this.board[row][col].figure != null)
                    {
                        dynamic figure = board[row][col].figure;
                        GameSprite sprite = new GameSprite();

                        sprite.SpriteImage = (Bitmap)Chess.Properties.Resources.ResourceManager.GetObject(figure.sprite);
                        sprite.X = figure.cords[0] * 50 + 4;
                        sprite.Y = figure.cords[1] * 50 + 54;
                        sprite.Width = 42;
                        sprite.Height = 42;

                        this.figures_sprites.Add(sprite);
                    }
                }
            }
        }

        public void Update(Point cursor_pos)
        {
            int pos_x = cursor_pos.X, pos_y = cursor_pos.Y;
            game.set_pos_x(pos_x);
            game.set_pos_y(pos_y);
            game.process_action();
            this.board = game.get_board();

            this.figures_sprites.Clear();

            for (int row = 0; row < 8; row++)
            {
                for (int col = 0; col < 8; col++)
                {
                    if (this.board[row][col].figure != null)
                    {
                        dynamic figure = board[row][col].figure;
                        GameSprite sprite = new GameSprite();

                        sprite.SpriteImage = (Bitmap)Chess.Properties.Resources.ResourceManager.GetObject(figure.sprite);
                        sprite.X = figure.cords[0] * 50 + 4;
                        sprite.Y = figure.cords[1] * 50 + 54;
                        sprite.Width = 42;
                        sprite.Height = 42;

                        this.figures_sprites.Add(sprite);
                    }
                }
            }
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
                    dynamic tile = this.board[row][col];

                    if (tile.highlighted == true)
                    {
                        if (tile.highlight_color == "yellow")
                        {
                            gfx.FillRectangle(new SolidBrush(Color.Yellow), new Rectangle(row * 50, 50 + col * 50, 50, 50));
                        }
                        else if (tile.highlight_color == "red")
                        {
                            gfx.FillRectangle(new SolidBrush(Color.Red), new Rectangle(row * 50, 50 + col * 50, 50, 50));
                        }
                    }
                    else if (tile.color == "white")
                    {
                        gfx.FillRectangle(new SolidBrush(Color.BurlyWood), new Rectangle(row * 50, 50 + col * 50, 50, 50));
                    }
                    else
                    {
                        gfx.FillRectangle(new SolidBrush(Color.Maroon), new Rectangle(row * 50, 50 + col * 50, 50, 50));
                    }
                }
            }

        }
    }
}
