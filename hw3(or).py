def orOperator(s):
    result_list = []
    for i in s:
        if 'love' in i or 'flower' in i:
            result_list.append(i)
    return result_list

s = []
n = int(input())
for i in range(n):
    s.append(input())
    result = orOperator(s)
print()
print('The results are as follows : ')
print()
if result:
    for i in result:
        print(i)