## 2869 달팽이는 올라가고 싶다

import sys

import math

A, B, V = map(int, input().split())

# 마지막 날 밤에는 B만큼 미끄러지지 않으므로 그냥 올라가기만 하면 됨.
# 즉, 마지막 날 전까지 (V - B)까지 올라가면 되고,
# 이는 (V - B) / (A - B)로 구할 수 있음. (소수점 올림)
days = math.ceil((V - B) / (A - B))

print(days)