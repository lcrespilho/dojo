using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace WordsInABook.Infrastructure
{
    public class BookReader
    {
        public string Path { get; set; }
        public string Book { get; protected set; }

        public virtual BookReader Take(string path)
        {
            Path = path;
            return this;
        }

        public virtual BookReader Read()
        {
            Book = File.ReadAllText(Path);
            return this;
        }

        public virtual BookReader RemoveAlphaNumerical()
        {
            try
            {
                Book = new Regex("([^a-zA-Z0-9 -])").Replace(Book, " ");
                Book = new Regex("[ ]{2,}").Replace(Book, " ");
            }
            catch (NullReferenceException)
            {
                // Does nothing.
            }
            catch (RegexMatchTimeoutException)
            {
                throw;
            }

            return this;
        }
    }
}
