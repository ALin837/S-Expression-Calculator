# S-Expression-Calculator
A simple command line program that acts as a calculator: it takes a single argument as an expression and prints out the integer result of evaluating it. 
The calculator only performs on the operators "add" and "multiply". 
Additionally, since it only considers the digits, it only works on natural numbers.

Some examples include:

```
"1" -> 1
"(add 1 100)" -> 101
"(add 3 (add (multiply 35 3) 3))" -> 111
"(multiply 2 (add (multiply 2 3) 8))" -> 28
"(multiply 3 (multiply (multiply 3 3) 3))" -> 81

```
