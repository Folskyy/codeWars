def solution(braces):
    stack = []
    for brace in braces:
        if brace in '[({':
            stack.append(brace) # add the openned ones
        elif brace in '])}':
            if not stack:
                return False # if close a brace and the stack is empty -> False
            top = stack.pop() # take the last item added on the list
            if top == '[' and brace != ']' or top == '{' and brace != '}' or top == '(' and brace != ')':
                return False # if the braces are not compatible -> False
    return not stack # if the stack is empty -> True

braces = ['([{{})', '(){}[]', '({[})', '{[}]}']

for element in braces:
    print(solution(element))
