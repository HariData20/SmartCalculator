# SmartCalculator
Here is an example of an expression that contains all possible operations:

3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1)
The result is 121.

A general expression can contain many parentheses and operations with different priorities. It is difficult to calculate such expressions if you do not use special methods. Fortunately, there is a fairly effective and universal solution, using a stack, to calculate the most general expressions. This program converts a infix expression to postfix and performs operations.

Infix notation is not very convenient if an expression has operations with different priorities, especially when brackets are used. But we can use postfix notation, also known as Reverse Polish notation (RPN). In this notation, operators follow their operands. See several examples below.

Infix notation 1:

3 + 2 * 4
Postfix notation 1:

3 2 4 * +
Infix notation 2:

2 * (3 + 4) + 1
Postfix notation 2:

2 3 4 + * 1 +

A stack (LIFO) is used to convert an expression from infix to postfix notation. The stack is used to store operators for reordering.
Expression in postfix notation, is processed using another stack.
###Steps to convert Infix to Postfix:

Add operands (numbers and variables) to the result (postfix notation) as they arrive.
If the stack is empty or contains a left parenthesis on top, push the incoming operator on the stack.
If the incoming operator has higher precedence than the top of the stack, push it on the stack.
If the precedence of the incoming operator is lower than or equal to that of the top of the stack, pop the stack and add operators to the result until you see an operator that has smaller precedence or a left parenthesis on the top of the stack; then add the incoming operator to the stack.
If the incoming element is a left parenthesis, push it on the stack.
6.If the incoming element is a right parenthesis, pop the stack and add operators to the result until you see a left parenthesis. Discard the pair of parentheses.
7.At the end of the expression, pop the stack and add all operators to the result.
8.No parentheses should remain on the stack. Otherwise, the expression has unbalanced brackets. It is a syntax error.
###Calculating the result

If the incoming element is a number, push it into the stack (the whole number, not a single digit!).

If the incoming element is the name of a variable, push its value into the stack.

If the incoming element is an operator, then pop twice to get two numbers and perform the operation; push the result on the stack.

When the expression ends, the number on the top of the stack is a final result.

###Objectives
This program supports multiplication *, integer division / and parentheses (...).
Unary minus operator, should still work.
The program will stop when the user enters the /exit command.
Note that a sequence of + (like +++ or +++++) is an admissible operator that is interpreted as a single plus. A sequence of - (like -- or ---) is also an admissible operator and its meaning depends on the length. If the user enters a sequence of * or /, the program prints a message that the expression is invalid.
The power operator ^ that has a higher priority than * and /.
Examples
The greater-than symbol followed by a space (>) represents the user input

2^2
4
22^3
16
8 * 3 + 12 * (4 - 2)
48
2 - 2 + 3
3
4 * (2 + 3
Invalid expression
-10
-10
a=4
b=5
c=6
a2+b3+c(2+3)
53
1 +++ 2 * 3 -- 4
11
3 *** 5
Invalid expression
4+3)
Invalid expression
/command
Unknown command
/exit
Bye!
