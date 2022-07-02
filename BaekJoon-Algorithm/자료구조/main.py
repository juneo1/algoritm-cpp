# ⭐⭐⭐ 자료구조: 우선순위 큐, 스택, 트리

# [뼈대문제] 백준 10828번. 스택
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys

stack = []
count = int(input())

for i in range (count):
    list = sys.stdin.readline().split()
    command = list[0]
    if command == "push":
        stack.append(int(list[1]))
    elif command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(1 if len(stack) == 0 else 0)
    elif command == "top":
        print(stack[-1] if len(stack) > 0 else -1)



# [뼈대문제] 백준 10845번. 큐
# [뼈대문제] 백준 10866번. 덱