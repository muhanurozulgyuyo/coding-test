import sys

# 모든 줄을 읽어들여 리스트로 반환
lines = sys.stdin.readlines()

# 각 줄을 출력
for line in lines:
    print(line.strip())  # strip() 함수로 개행 문자 제거
