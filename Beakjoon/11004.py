import sys

count, cnt = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
print(num[cnt - 1])
