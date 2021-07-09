//using System;
//using System.Drawing;
//using System.Threading.Tasks;

//namespace GameLoopProject
//{
//    class GameLoop
//    {
//        private Game _myGame;

//        public bool Running { get; private set; }

//        public void Load(Game gameObj)
//        {
//            _myGame = gameObj;
//        }

//        public async void Start()
//        {
//            _myGame.Load();

//            Running = true;

//            _myGame.Update();
//            await Task.Delay(1);

//            while (Running)
//            {
//                if (1 == 1)
//                {
//                    _myGame.Update();

//                    await Task.Delay(1);
//                }

//            }
//        }

//        public void Draw(Graphics gfx)
//        {
//            _myGame.Draw(gfx);
//        }
//    }
//}
