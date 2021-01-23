# S-Expression-Calculator
A simple command line program that acts as a calculator.
The calculator only performs on the operators "add" and "multiply". 
Additionally, since it only considers the digits, it only works on natural numbers.

**Examples:**

```
$ ./calc.py "1"
>> 1

$ ./calc.py "(add 3 4)"
>> 7

$ ./calc.py "(multiply 2 12)"
>> 24

$ ./calc.py "(add 3 (add (multiply 35 3) 3))"
>> 111

```
