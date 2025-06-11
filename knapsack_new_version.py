n, cap_lit = map(int, input().split())
cap_lit_s = cap_lit
dict_v_h = {}

for i in range(n):
    h, v = map(int, input().split())
    h_v = h / v
    dict_v_h[h_v] = v

res = 0
for h_v in sorted(dict_v_h, reverse=True):
    if cap_lit == 0:
        break
    v = dict_v_h[h_v]
    if cap_lit - v < 0:
        res = res + h_v * cap_lit
        cap_lit = 0
    else:
        res = res + h_v * v
        cap_lit = cap_lit - v
        
print(res)