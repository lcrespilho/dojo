using System;
using System.Text;
using System.Collections.Generic;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using CorridorProblem.Core;
using System.Linq;

namespace CorridorProblem.Tests
{
    /// <summary>
    /// Tests for Corridor class.
    /// </summary>
    [TestClass]
    public class CorridorTest
    {
        [TestMethod]
        public void InitialState()
        {
            var expected = 3;
            var corridor = new Corridor(expected);

            var actual = corridor.Lamps.Length;

            Assert.AreEqual(expected, actual);
            Assert.IsTrue(
                corridor.Lamps.All(l => l == false), "There is at least one lamp which is on."
            );
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentOutOfRangeException))]
        public void InvalidInitialState()
        {
            var invalidNumberOfLamps = -3;
            var corridor = new Corridor(invalidNumberOfLamps);

            // It hasn't thrown any exceptions.
            Assert.Fail();
        }

        [TestMethod]
        public void ValidGoJoseGo3()
        {
            bool[] expected = { true, false, false };
            var corridor = new Corridor(expected.Length);

            corridor.GoJoseGo();

            Assert.IsTrue(expected.SequenceEqual(corridor.Lamps), "At least one lamp is wrong!");
        }

        [TestMethod]
        public void ValidGoJoseGo1()
        {
            bool[] expected = { true };
            var corridor = new Corridor(expected.Length);

            corridor.GoJoseGo();

            Assert.IsTrue(expected.SequenceEqual(corridor.Lamps), "At least one lamp is wrong!");
        }

        [TestMethod]
        public void ValidGoJoseGo10()
        {
            bool[] expected = { true, false, false, true, false, false, false, false, true, false };
            var corridor = new Corridor(expected.Length);

            corridor.GoJoseGo();

            Assert.IsTrue(expected.SequenceEqual(corridor.Lamps), "At least one lamp is wrong!");
        }
    }
}
