import numpy as np

a, b = 1, 1
n = 7
r = 3

y,x = np.ogrid[-a:n-a, -b:n-b]
mask = x*x + y*y <= r*r

array = np.ones((n, n))
array[mask] = 255
print array
