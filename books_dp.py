n, S = map(int, input().split())
packages = []
for _ in range(n):
    data = list(map(int, input().split()))
    sz = data[0]
    costs = data[1:]
    packages.append((sz, costs))

dp = [-1] * (S + 1)
dp[0] = 0

# path[i][j]: وقتی به پکیج i رسیدیم و پول j داشتیم، چی انتخاب کردیم: 0/1/2
from collections import defaultdict
prev = [None] * (S + 1)
choice = [None] * (S + 1)

for idx, (sz, costs) in enumerate(packages):
    new_dp = dp[:]
    new_prev = prev[:]
    new_choice = choice[:]
    min_one = min(costs)
    total_all = sum(costs)

    for money in range(S + 1):
        if dp[money] == -1:
            continue

        # Option 0: skip
        if dp[money] > new_dp[money]:
            new_dp[money] = dp[money]
            new_prev[money] = money
            new_choice[money] = (idx, 0)

        # Option 1: buy one
        if money + min_one <= S:
            if dp[money] + 1 > new_dp[money + min_one]:
                new_dp[money + min_one] = dp[money] + 1
                new_prev[money + min_one] = money
                new_choice[money + min_one] = (idx, 1)

        # Option 2: buy all
        if money + total_all <= S:
            if dp[money] + sz > new_dp[money + total_all]:
                new_dp[money + total_all] = dp[money] + sz
                new_prev[money + total_all] = money
                new_choice[money + total_all] = (idx, 2)

    dp = new_dp
    prev = new_prev
    choice = new_choice

# Find max value
max_toys = max(dp)
s = dp.index(max_toys)

# Reconstruct choices
res = [0] * n
while s != 0:
    idx, c = choice[s]
    res[idx] = c
    s = prev[s]

print(max_toys)
print(''.join(map(str, res)))
