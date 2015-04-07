class Corridor
  # getter and setter
  attr_accessor :lamps

  def initialize(n)
    @lamps = Array.new(n.to_i, false)
  end

  def go_joseph_go
    n = @lamps.size
    
    n.times do |i|
      go_joseph_once(i)
    end

    @lamps
  end

  private
  def go_joseph_once(current)
    @lamps.each_index do |i|
      @lamps[i] = !@lamps[i] if (i+1) % (current+1) == 0
    end
  end
end
