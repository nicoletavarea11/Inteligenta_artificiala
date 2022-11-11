import numpy
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
a = numpy.mean(speed)
b = numpy.median(speed)
c = stats.mode(speed, keepdims=False)
d = numpy.std(speed)
e = numpy.var(speed)
f = numpy.percentile(ages, 75)
print("Valoarea medie este ", a)
print("Valoarea mediana este ", b)
print("Valoarea care apare de cele mai multe ori este ", c)
print("Abaterea standard este ", d)
print("Deviatia standard este ", e)
print("Percentila de 75 este ", f)
g = numpy.random.uniform(0.0,5.0,250)
print("Matricea random este ", g)