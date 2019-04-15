from matplotlib import pyplot
pyplot.rcParams['font.family'] = 'IPAPGothic'

import numpy

x = numpy.linspace(-numpy.pi * 2, numpy.pi * 2, 1024, endpoint = True)
y_sin = numpy.sin(x)
y_cos = numpy.cos(x)

pyplot.plot(x, y_sin)
pyplot.plot(x, y_cos)
pyplot.show()
