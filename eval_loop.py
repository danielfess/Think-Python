def eval_loop():
    """Prompts the user for an expression as input, computes the expression
    and prints the answer.  Type 'done' to leave eval_loop and reprint the
    answer to the previous expression.
    """

    result = 'No previous evaluation to print.'
    while True:
        expression = input('Enter mathematical expression.\n')
        if expression == 'done':
            print(result)
            break
        result = eval(expression)
        print(result)

import math
eval_loop()