using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using WordsInABook.Infrastructure;

namespace WordsInABook.Tests
{
    [TestClass]
    public class BookReaderTest
    {
        [TestMethod]
        public void ReadsCorrectly()
        {
            var reader = new BookReader
            {
                Path = "book.txt"
            };

            var book = reader
                .Read()
                .RemoveAlphaNumerical()
                    .Book;

            Assert.IsFalse(string.IsNullOrEmpty(book));
        }
    }
}
