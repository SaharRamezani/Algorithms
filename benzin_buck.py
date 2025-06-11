n, k, l = map(int, input().split())
arr = list(map(int, input().split()))
# add 0 to the beginning of the list
arr.insert(0, 0)
# add l to the end of the list
arr.append(l)

res_list = []
for i in range(1, n):
    if arr[i] - arr[i - 1] > k:
        res_list.append(i - 1)

if (p < l):
    print(-1)
else:
    print(len(res_list))
    for i in res_list:
        print(i, end=' ')