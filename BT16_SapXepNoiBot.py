# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:19:24 2021

@author: Admin
"""

def bubble_sort(nums):
    # Chúng ta đặt hoán đổi thành True để vòng lặp chạy ít nhất một lần
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Hoán đổi các phần tử
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Đặt cờ thành True để chúng ta lặp lại
                swapped = True


random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)