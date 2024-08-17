N = int(input())
a = set(map(int, input().split()))	
M = int(input())
b = map(int, input().split())

for i in b:				
    print(1) if i in a else print(0)	