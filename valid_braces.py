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


with open('input/valid_braces_input.txt', 'r') as f:
    conteudo = f.read()

conteudo = conteudo.split(sep='\n')

with open('output/valid_braces_out.txt', 'w') as file:
    for i in range(0, 5):
        if solution(conteudo[i]) == True:
            file.write(f"{conteudo[i]} --> True\n")
        else:
            file.write(f"{conteudo[i]} --> False\n")