using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Linq;
using System.Collections.Generic;

namespace WordsInABook.Tests
{
    [TestClass]
    public class InterpreterTest
    {
        [TestMethod]
        public void MostFrequentWordsReturnsListAsLargeAsParameter()
        {
            var sizeExpected = 10;
            var book = "A a a nice new book book book book book book called a nice new book";
            
            var interpreter = new Interpreter
            {
                Book = book
            };

            var result = interpreter.MostFrequentWords(sizeExpected);

            Assert.IsTrue(result.Count <= sizeExpected);
        }

        [TestMethod]
        public void MostFrequentWordsReturnsListInCorrectOrder()
        {
            var book = "A a a nice new book book book book book book called a nice new book";
            var expectedOrder = new string[] { "book", "a", "nice" };
            
            var interpreter = new Interpreter
            {
                Book = book
            };

            var result = interpreter.MostFrequentWords(3);

            Assert.IsTrue(Enumerable.SequenceEqual(expectedOrder, result));
        }

        [TestMethod]
        public void MostFrequentWordsOnListOfUniqueWords()
        {
            var book = "A nice new book";
            var expectedOrder = new string[] { "A", "nice", "new", "book" };

            var result = new Interpreter()
                .Take(book)
                .MostFrequentWords();

            Assert.IsTrue(Enumerable.SequenceEqual(expectedOrder, result));
        }

        [TestMethod]
        public void MostFrequentWordsOnUnitaryList()
        {
            var book = "A";
            var expectedOrder = new string[] { "A" };

            var result = new Interpreter()
                .Take(book)
                .MostFrequentWords();

            Assert.IsTrue(Enumerable.SequenceEqual(expectedOrder, result));
        }
    }
}
