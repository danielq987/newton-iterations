"""
Newton's Iterative Method Calculator
Made because my math assignment wanted me to calculate 7 iterations of Newton's method and I was lazy.
Made by Daniel Qu
Notes:
  - Type 3x as 3*x
  - Type e^x as exp(x)
  
Currently not working for functions with fractional exponents
"""
from tabulate import tabulate # formats output into a table
from sympy import * # equation parsing, derivates
import math

NUM_ITERATIONS = 15 # iterations of Newton's method to go through
PRECISION = 6 # number of decimal points to display

def main():
  # read in input
  while True:
    try:
      expr = sympify(input("Enter a function in terms of x (lowercase): "))
      x0 = float(input("Enter an initial guess: "))
      break
    except SympifyError:
      print("Equation could not be parsed, try again.")

  # use sympy methods to make lambda functions
  x = Symbol('x')
  fx = lambdify(x, expr)
  ddx = lambdify(x, diff(expr, x))
  table = [["i", "xi", "f(xi)", "f'(xi)"]]
  xi = x0

  # iterate with newton's iterative method
  for i in range(NUM_ITERATIONS):
    table.append([i, round(xi, 6), round(fx(xi), 6), round(ddx(xi))])
    xi = xi - (fx(xi)/ddx(xi))
  print(tabulate(table, headers="firstrow"))

if __name__ == "__main__":
  main()
  