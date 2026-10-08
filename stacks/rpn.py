def evalRPN(tokens: list[str]) -> int:
    '''
    reverse the tokens so that it becomes a proper stack

    pop until you get a arithmetic operation

    keep the poped items in a list

    perform the arithmetic operation on the last two items

    put the result back in pop list

    add the elements in the poplist back to the stack
    '''

    def perform_arithmetic(pop_list):
        print(f'pop_list before: {pop_list}')
        if not pop_list:
            return []
        operation = pop_list.pop()
        a = int(pop_list.pop())
        b = int(pop_list.pop())
        if operation == "+":
            pop_list.append(b+a)
        elif operation == "-":
            pop_list.append(b-a)
        elif operation == "*":
            pop_list.append(b*a)
        elif operation == "/":
            pop_list.append(b // a)

        return pop_list

    i, j = 0, len(tokens) - 1

    while i < j:
        tokens[i], tokens[j] = tokens[j], tokens[i]
        i += 1
        j -= 1
    pop_list = []
    while tokens:
        pop_list.append(tokens.pop())
        if pop_list[-1] in ["+","-","*","/"]:
            pop_list = perform_arithmetic(pop_list)
            print(f'pop_list after: {pop_list}')
            print("---------------------------")
            while pop_list:
                tokens.append(pop_list.pop())

    return pop_list[-1]

print(f'result: {evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])}')
