def get_next_letters(word):
    result = {}
    length = len(word)

    for i, char in enumerate(word):
        key = f"{char}_{i}"  # distinguish same letters by index
        next_letters = set(word[j] for j in range(i + 1, length))
        result[key] = next_letters

    return result

def rec(w1, w2, visited=None):
    if visited is None:
        visited = set()

    if (w1, w2) in visited or not w1 or not w2:
        return
    visited.add((w1, w2))

    next_letters_w1 = get_next_letters(w1)
    next_letters_w2 = get_next_letters(w2)

    w1_f = ""
    for key1 in next_letters_w1:
        for key2 in next_letters_w2:
            char1, i = key1.split('_')
            char2, j = key2.split('_')
            if char1 == char2:
                i = int(i)
                j = int(j)
                w1_f = w1[i+1:]
                rec(w1[i+1:], w2[j+1:], visited)

    if w1[0] != w1_f:
        print(str(w1[0]) + "    " + w1_f)
        print(str(w1)    + "    " + str(w2))
        print("*******************")

    return

w1 = input()
w2 = input()

w1_next_letter = []
for i in range(len(w1)):
    w1_next_letter.append(w1[i:])

rec(w1, w2, visited=set())

            


            
            
