"""

@Author: Li Zenghui
@Date: 2020-05-14 16:48
"""
import sympy as sy
u1 = sy.symbols('u1')
u2 = sy.symbols('u2')
u3 = sy.symbols('u3')
v1 = sy.symbols('v1')
v2 = sy.symbols('v2')
v3 = sy.symbols('v3')
a = sy.solve([
    20*u1*v1 + 10*u1*v2 + 10*u1*v3 -100,
    15*u2*v1 + 25*u2*v2 + 20*u2*v3 -100,
    10*u3*v1 + 15*u3*v2 + 15*u3*v3 -125,
    20*v1*u1 + 15*v1*u2 + 10*v1*u3 -125,
    10*v2*u1 + 25*v2*u2 + 15*v2*u3 -90,
    10*v3*u1 + 20*v3*u2 + 15*v3*u3 -110],[u1,u2,u3,v1,v2,v3])
print(a)
