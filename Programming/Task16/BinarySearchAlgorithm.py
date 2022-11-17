from random import randint

left = 0
right = 100000
x=randint(left,right)

#метод последовательного перебора
count = 0
for i in range(0,101):
    count+=1
    if i==x:
        print("Число найдено!")
        break
print(f"Искомое число - это {x} и было найдено методом последовательного перебора за {count} итераций")

#метод случайного отгадывания
count = 1
y=randint(left,right)
while x!=y:
    y=randint(left,right)
    count+=1
print(f"Искомое число - это {x} и было найдено методом случайного отгадывания за {count} итераций")

#метод бинарного поиска 1
count = 1
print(f"Давай начнем игру - угадай число от {left} до {right}")
y = right // 2
z = y // 2
while x != y:
    if x < y: y = y - z
    else: y = y + z
    if z > 1: z = z // 2
    count+=1
print(f"Искомое число - это {x} и было найдено методом бинарного поиска 1 за {count} итераций")

#метод бинарного поиска 2
count = 1
print(f"Давай начнем игру - угадай число от {left} до {right}")
mid = (left + right) // 2
while x != mid:
    if x < mid: right = mid - 1
    else: left = mid + 1
    mid = (left + right) // 2
    count+=1
print(f"Искомое число - это {x} и было найдено методом бинарного поиска 2 за {count} итераций")

# def binary_search(list_for_search, search_namber):
#     count = 0
#     start_list = 0
#     stop_list = len(list_for_search) - 1
#     while start_list <= stop_list:
#         count += 1
#         middle = ((start_list + stop_list) // 2)
#     if list_for_search[middle] == search_namber:
#         return (middle, list_for_search[middle], count)
#     elif list_for_search[middle] > search_namber:
#         stop_list = middle - 1
#     else:
#         start_list = middle + 1
#     return None


# def binary_search_recursion(list_for_search, search_namber, start_list, stop_list):
#     if start_list > stop_list:
#         return None
#     else:
#         middle = ((start_list + stop_list) // 2)
#     if list_for_search[middle] == search_namber:
#         return middle, list_for_search[middle]
#     elif list_for_search[middle] > search_namber:
#         return binary_search_recursion(list_for_search, search_namber, start_list, middle - 1)
#     else:
#         return binary_search_recursion(list_for_search, search_namber, middle + 1, stop_list)


# def binary_search_recursive(array, element, start, end):
#     if start > end:
#         return -1
#     mid = (start + end) // 2
#     if element == array[mid]:
#         return mid
#     if element < array[mid]:
#         return binary_search_recursive(array, element, start, mid-1)
#     else:
#         return binary_search_recursive(array, element, mid+1, end)


# def binarySearch(a, key):
#     low = 0
#     high = a.length - 1
#     while (low <= high):
#         mid = (low + (high - low) // 2)
#         midVal = a[mid]
#         if (midVal < key):
#             low = mid + 1
#         elif (midVal > key):
#             high = mid - 1
#         else:
#             return mid   #key found
#     return -(low + 1)   #key not found.


