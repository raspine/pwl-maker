from pwl_maker.signal import Signal
import matplotlib.pyplot as plt

if __name__ == "__main__":
  s = Signal()
  s.at(3).to(5).at(4).to(0).extend_to(10)
  s.scale_time(1e-3);
  s.save()

  times, values = s.as_lists()

  plt.plot(times, values)
  plt.show()