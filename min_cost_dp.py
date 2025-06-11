import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

INF = float('inf')
dp = [[[INF, INF] for _ in range(m)] for _ in range(n)]

dp[0][0][1] = a[0][0]

for j in range(1, m):
    dp[0][j][1] = dp[0][j - 1][1] + a[0][j]

for i in range(1, n):
    # First pass: left-to-right (right movement)
    for j in range(m):
        min_from_above = min(dp[i - 1][j][0], dp[i - 1][j][1])
        if j > 0:
            dp[i][j][1] = min(dp[i][j - 1][1], min_from_above) + a[i][j]
        else:
            dp[i][j][1] = min_from_above + a[i][j]

    for j in reversed(range(m)):
        min_from_above = min(dp[i - 1][j][0], dp[i - 1][j][1])
        if j < m - 1:
            dp[i][j][0] = min(dp[i][j + 1][0], min_from_above) + a[i][j]
        else:
            dp[i][j][0] = min_from_above + a[i][j]

print(dp[n - 1][m - 1][1])
