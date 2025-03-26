string = "hello"
soma = 0

for i in range(len(string)):
    if i == len(string)-1:
        break
    else:
        print(ord(string[i]), ord(string[i+1]))
        soma += abs(ord(string[i]) - ord(string[i+1]))

print(soma)
