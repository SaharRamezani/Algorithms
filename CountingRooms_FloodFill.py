# Credits to my professor - UniGe

from itertools import count
 
n, m = [int(x) for x in input().split()]
row = m + 1  # 1 border to avoid moving from left to right
 
map = {i + j for i in range(0, n * row, row) for j, c in enumerate(input().
 span class="pln">strip()) if c == '.'}
 
for i in count():
    try:
        queue = [map.pop()]
    except KeyError:
        print(i)
        break
    while queue:
        x = queue.pop()
        enqueued = map & {x - row, x + row, x - 1, x + 1}
        queue.extend(enqueued)
        map.difference_update(enqueued)

