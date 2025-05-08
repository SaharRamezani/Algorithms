import sys
def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    A = {'A':0,'C':1,'G':2,'T':3}
    inv = ['A','C','G','T']
    # build next-occurrence table
    nxt = [[n]*4 for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for c in range(4):
            nxt[i][c] = nxt[i+1][c]
        nxt[i][A[s[i]]] = i

    # dp[i]=length of shortest absent subseq in s[i:]
    dp = [0]*(n+1)
    dp[n] = 1
    for i in range(n-1, -1, -1):
        best = n+1
        for c in range(4):
            j = nxt[i][c]
            if j == n:
                best = 1
                break
            else:
                if dp[j+1]+1 < best:
                    best = dp[j+1]+1
        dp[i] = best

    # reconstruct
    res = []
    i = 0
    while i <= n:
        for c in range(4):
            j = nxt[i][c]
            if j == n:
                res.append(inv[c])
                print(''.join(res))
                return
            if dp[i] == dp[j+1] + 1:
                res.append(inv[c])
                i = j+1
                break

if __name__ == "__main__":
    main()
