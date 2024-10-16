answer = ''
s = input().split()
print(s)
for word in s:
    new_word = word[0].upper() + word[1:].lower()
    answer.append(new_word)
print(' '.join(answer))