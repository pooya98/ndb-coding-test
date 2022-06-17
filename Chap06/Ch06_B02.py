def setting(data):
    return data[1]

N = int(input())

arr = []

for _ in range(N):
    name, grade = input().split()
    grade = int(grade)

    arr.append((name, grade))

arr = sorted(arr, key=setting)

for element in arr:
    print(element[0], end=' ')

