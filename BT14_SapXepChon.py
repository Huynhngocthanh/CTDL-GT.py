# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:15:08 2021

@author: Admin
"""

def selection_sort(nums):
    # Giá trị này của tôi tương ứng với số lượng giá trị đã được sắp xếp
    for i in range(len(nums)):
        # Chúng tôi giả định rằng mục đầu tiên của phân đoạn chưa được sắp xếp là mục nhỏ nhất
        lowest_value_index = i
        # Vòng lặp này lặp lại các mục chưa được sắp xếp
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Hoán đổi các giá trị của phần tử chưa được sắp xếp thấp nhất với phần tử chưa được sắp xếp đầu tiên
        # thành phần
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


# Xác minh nó hoạt động
random_list_of_nums = [12, 8, 3, 20, 11]
selection_sort(random_list_of_nums)
print(random_list_of_nums)