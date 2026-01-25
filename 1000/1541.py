import sys
input = sys.stdin.readline

expr = input().strip().split('-')
result = sum(map(lambda x: sum(map(int, x.split('+'))), expr[:1]))
for part in expr[1:]:
    result -= sum(map(int, part.split('+')))
print(result)
