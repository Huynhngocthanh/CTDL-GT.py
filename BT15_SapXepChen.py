# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:19:24 2021

@author: Admin
"""

def insertion_sort(nums):
    # Bắt đầu trên phần tử thứ hai vì chúng tôi giả sử phần tử đầu tiên đã được sắp xếp
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Và giữ một tham chiếu về chỉ mục của phần tử trước đó
        j = i - 1
        # Di chuyển tất cả các mục của phân đoạn đã sắp xếp về phía trước nếu chúng lớn hơn
        # mục để chèn
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Chèn mục
        nums[j + 1] = item_to_insert


# Xác minh nó hoạt động
random_list_of_nums = [9, 1, 15, 28, 6]
insertion_sort(random_list_of_nums)
print(random_list_of_nums)