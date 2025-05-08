n = int(input())
songs = list(map(int, input().split()))

seen = set()
left = 0
max_len = 0

for right in range(n):
    while songs[right] in seen:
        seen.remove(songs[left])
        left += 1
    seen.add(songs[right])
    max_len = max(max_len, right - left + 1)

print(max_len)
