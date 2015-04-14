using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CorridorProblem.Core
{
    public class Corridor
    {
        private bool[] _lampsList;

        public bool[] Lamps
        {
            get { return _lampsList; }
            set { _lampsList = value; }
        }

        public Corridor(int count)
        {
            if (count <= 0)
            {
                throw new ArgumentOutOfRangeException("count", count, 
                    "Cannot instantiate a list of lamps with this length.");
            }

            _lampsList = new bool[count];
        }

        public void GoJoseGo()
        {
            for (var i = 1; i < Lamps.Length +1; i++)
            {
                GoJoseOnce(i);
            }
        }

        protected void GoJoseOnce(int iteration)
        {
            for (var i = iteration; i < Lamps.Length +1; i += iteration)
            {
                Lamps[i -1] = !Lamps[i -1];
            }
        }
    }
}
