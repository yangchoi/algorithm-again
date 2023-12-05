num1, num2 = [int(s) for s in input().split()]

set1 = set([int(s) for s in input().split()])
set2 = set([int(s) for s in input().split()])

result1 = set1 - set2
result2 = set2 - set1

print(len(result1) + len(result2))