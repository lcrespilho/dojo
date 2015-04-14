using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WordsInABook
{
    public class Interpreter
    {
        public int DefaultWordsCount = 10;
        public string Book { get; set; }

        public virtual Interpreter Take(string book)
        {
            Book = book;
            return this;
        }

        public virtual ICollection<string> MostFrequentWords()
        {
            return MostFrequentWords(DefaultWordsCount);
        }
        public virtual ICollection<string> MostFrequentWords(int count)
        {
            return Book
                .Split(' ')
                .GroupBy(word => word)
                .OrderByDescending(group => group.Count())
                .Take(count)
                .Select(group => group.Key)
                .ToList();
        }
    }
}
