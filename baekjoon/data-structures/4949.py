while True:
    str = input()

    if str == ".":
        break

    stack = []

    for s in str:
        if s == '[' or s == '(':
            stack.append(s)
        elif s == ']' or s == ')':
            if stack:
                top = stack.pop()
                if (s == ']' and top != '[') or (s == ')' and top != '('):
                    print("no")
                    break
            else:
                print("no")
                break
    else:
        if stack:
            print("no")
        else:
            print("yes")
