S = input().upper()

cnt = {char: 0 for char in set(S)}

for s in S:
    cnt[s] += 1

max_cnt = max(cnt.values())

max_chars = [char for char, count in cnt.items() if count == max_cnt]

if len(max_chars) > 1:
    print('?')
else:
    print(max_chars[0])