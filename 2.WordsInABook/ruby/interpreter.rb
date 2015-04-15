class Interpreter
  def self.most_frequent_words(str, top_n = 10)
    str.split.sort { |a,b| str.count(b) <=> str.count(a) }.uniq.take(top_n)
  end
end
