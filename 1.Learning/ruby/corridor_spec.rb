require_relative "corridor"

RSpec.describe Corridor do

  describe "::initialize" do

    context "when n is negative" do
      it "should raise error" do
        expect { Corridor.new(-1) }.to raise_error ArgumentError
      end
    end

    context "when n is 0" do
      it "should have no lamps" do
        expect(Corridor.new(0).lamps).to be_empty
      end
    end

    context "when n is positive" do
      it "should have all lamps off" do
        expect(Corridor.new(1).lamps).to eq [false]
        expect(Corridor.new(3).lamps).to eq [false, false, false]
      end
    end

    specify "its param should respond to :to_i" do
      duck = double()
      allow(duck).to receive(:to_i) { 0 }
      expect { Corridor.new(duck) }.not_to raise_error

      non_duck = double()
      allow(non_duck).to receive(:to_i) { raise NoMethodError }
      expect { Corridor.new(non_duck) }.to raise_error NoMethodError
    end     

  end

  describe "#go_joseph_go" do
    it "should produce the correct output" do
      expect(Corridor.new(0).go_joseph_go).to eq []
      expect(Corridor.new(1).go_joseph_go).to eq [true]
      expect(Corridor.new(3).go_joseph_go).to eq [true, false, false]

      expected_a = [true, false, false, true, false, false, false, false, true, false]
      expect(Corridor.new(10).go_joseph_go).to eq(expected_a)
    end
  end

end
