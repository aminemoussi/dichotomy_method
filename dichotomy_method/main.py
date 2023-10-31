import matplotlib.pyplot as plt
import numpy as np
import inspect
from scipy.optimize import fsolve
import time

def f(x):
    return x**2 + 1

def dechotomy_methode(a, b, tolerance):
    xl = a
    xr = b
    i = 1
    while (np.abs(xl - xr) >= tolerance):
        c = (xr + xl)/2
        if ( (f(xl) * f(c)) > tolerance ):
            xl = c
            i += 1
        else:
            xr = c
            i += 1
    return c, i



tolerance = 1e-4
print("Now type in the interval: ")
a = int( input("Left side: ") )
b = int( input("right side: ") )

if (a >= b):
    print("Invalid interval must be fixed.")
    x = a
    a = b
    b = x


elements = np.arange(a, b, tolerance)

plt.figure(figsize = (8, 6))
plt.plot(elements, f(elements), label='y = x^3', color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = x^3')
plt.legend()
plt.grid()
plt.show()

cont = input("Does the graph seem continuous(y/n): ")
if (cont == 'n'):
    print("The method can't be applied on an uncontinuous graph.")
else:
    answer = dechotomy_methode(a, b, tolerance)
    print("The root value of the function \"", inspect.getsource(f) ,"\" with a tolerance of (", tolerance ,") is: ", answer[0])
    print("It took ",answer[1]," iterations.")

    print("\n")
    time.sleep(2)

    shortcut = fsolve(f, [-1.5, -1])
    print("fsolve found ", len(shortcut) ," answers.")
    print("Using scipy's \"fsolve\" we get: ", shortcut)