# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:21:43 2021

@author: Admin
"""

def heaps(arr, n, i):
    largest = i  # Khởi tạo lớn nhất dưới dạng root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # Xem liệu left child của root có tồn tại và lớn hơn root hay không
    if l < n and arr[largest] < arr[l]:
        largest = l

    # Xem liệu right child của root có tồn tại và lớn hơn root hay không
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Thay đổi root, nếu cần
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Xử lý root.
        heaps(arr, n, largest)


# Hàm chính để sắp xếp một mảng có kích thước nhất định


def heapSort(arr):
    n = len(arr)

    # Xây dụng 1 maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heaps(arr, n, i)

    # Từng phần tử trích xuất một
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heaps(arr, i, 0)


# Mã 
arr = [1, 50, 138, 25, 17, 89]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i])