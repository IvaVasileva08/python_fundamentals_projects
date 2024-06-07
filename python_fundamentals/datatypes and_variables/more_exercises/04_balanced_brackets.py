number_string = int(input())
str_open = 0
verification = ''

for i in range(1, number_string + 1):
    stringer = str(input())
    if stringer == '(':
        for j in range(i + 1, number_string):
            stringer = str(input())
            str_open += 1
            if stringer == '(':
                verification = 'UNBALANCED'
                break
            elif stringer == ')':
                verification = 'BALANCED'
                break
    elif stringer == ')':
        verification = 'UNBALANCED'
        break
    if i + str_open != number_string:
        continue
    break
print(verification)