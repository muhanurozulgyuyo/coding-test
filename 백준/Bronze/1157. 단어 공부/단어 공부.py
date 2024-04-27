#1157 단어 공부

S = input()

S = S.upper()

unique_S = ''.join(set(S))

cnt = {}

for u_s in unique_S:
    cnt[u_s] = 0
    
for s in S:
    cnt[s] += 1
    
li = []
mx = []

for key in cnt:
    li.append(cnt[key])
    
for i in li:
    if i == max(li):
        mx.append(i)
        
if len(mx) > 1:
    print('?')
else:
    for key in cnt:
        if cnt[key] == mx[0]:
            print(key)