# greedy로 풀어야 할듯?

n = int(input())
count = 0

while n > 0:
	if n == 1 or n == 2:
		count = -1
		break
	if n % 5 == 0: 
		count += n // 5
		break
	else:
		n -= 3
		count += 1
	
print(count)