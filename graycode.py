def gray_code(n):

    if n == 1:
        return ["0", "1"]
    
    prev = gray_code(n - 1)

    return ["0" + el for el in prev] + \
            ["1" + el for el in reversed(prev)]

n = int(input())
for el in gray_code(n):
    print(el)