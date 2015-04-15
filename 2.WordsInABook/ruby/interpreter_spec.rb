require_relative 'interpreter'

RSpec.describe Interpreter do
  describe '::most_frequent_words' do
    it 'should be case sensitive' do
      str = "A A a"
      
      sensitive = Interpreter.most_frequent_words(str)
      insensitive = Interpreter.most_frequent_words(str.downcase)

      expect(sensitive).not_to eq(insensitive)
    end

    specify 'when string is empty' do
      expect(Interpreter.most_frequent_words('')).to eq []
    end

    specify 'when string has one char' do
      expect(Interpreter.most_frequent_words('a')).to eq ['a']
    end

    specify 'when all words are unique' do
      expect(Interpreter.most_frequent_words('a b')).to eq ['a', 'b']
      expect(Interpreter.most_frequent_words('a b ' * 10)).to eq ['a', 'b']
    end

    specify 'when not all words are unique' do
      expect(Interpreter.most_frequent_words('b a b a a c')).to eq ['a', 'b', 'c']
      expect(Interpreter.most_frequent_words('b a b a a c ' * 10)).to eq ['a', 'b', 'c']
    end
  end
end


