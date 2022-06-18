
## 방법 1. 이진 탐색을 이용
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if(array[mid] == target):
            return True

        elif(array[mid] > target):
            end = mid - 1

        else:
            start = mid + 1

    return False


N = int(input())
array = list(map(int, input().split()))
array.sort()

M = int(input())
customer_list = list(map(int, input().split()))

check = True
for i in customer_list:
    if binary_search(array, i, 0, len(array) - 1):
        print("yes", end=' ')
    else:
        print("no", end=' ')


## 방법 2. 계수 정렬을 이용
N = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())

customer_list = list(map(int, input().split()))

for i in customer_list:
    if array[i] == 1:
        print("yes", end=' ')
    else:
        print("no", end=' ')


## 방법 3. 집합 자료형 이용
N = int(input())

array = set(map(int, input().split()))

m = int(input())
customer_list = list(map(int, input().split()))

for i in customer_list:
    if i in array:
        print("yes", end=' ')
    else:
        print("no", end=' ')