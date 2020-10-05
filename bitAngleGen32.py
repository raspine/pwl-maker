from pwl_maker.signal import Signal
import matplotlib.pyplot as plt

def getIndex(noOnes):
    ret = []
    if noOnes == 0:
        return ret
    diff = 32/noOnes
    for x in range(0, noOnes, 1):
        ret.append((diff/noOnes) + x*diff)
    return ret

if __name__ == "__main__":
  s = Signal()
  cycles = 3
  amplitute = 3.3
  for w in range(32):
      print(w)
      pos = getIndex(w);
      for x in range(w*cycles, w*cycles+cycles):
          for y in range(w):
              s.at(pos[y]+x*32).to(amplitute).at(pos[y]+1+x*32).to(0)
          s.extend_to(32*x + 32)
  s.scale_time(60e-9);
  s.save()

  times, values = s.as_lists()

  plt.plot(times, values)
  plt.show()

