using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using WordsInABook.Infrastructure;

namespace WordsInABook
{
    class Program
    {
        static void Main(string[] args)
        {
            var path = "book.txt";
            if (args.Length > 0)
            {
                path = args[0];
            }

            var numberOfWords = 10;
            if (args.Length > 1)
            {
                numberOfWords = int.Parse(args[1]);
            }

            var reader = new BookReader()
                .Take(path)
                .Read()
                .RemoveAlphaNumerical();

            var words = new Interpreter()
                .Take(reader.Book)
                .MostFrequentWords(10);

            Console.Write("{ ");
            foreach (var word in words)
            {
                Console.Write(word + ' ');
            }
            Console.WriteLine("}");
        }
    }
}
