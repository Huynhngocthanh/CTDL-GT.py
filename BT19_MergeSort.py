# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:21:43 2021

@author: Admin
"""

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Chúng ta sử dụng độ dài danh sách thường xuyên, vì vậy rất tiện lợi khi tạo các biến
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Chúng ta kiểm tra giá trị nào từ đầu danh sách nhỏ hơn
            # Nếu mục ở đầu danh sách bên trái nhỏ hơn, hãy thêm nó vào
            # vào danh sách đã sắp xếp
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Nếu mục ở đầu danh sách bên phải nhỏ hơn, hãy thêm nó vào
            # vào danh sách đã sắp xếp
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Nếu chúng ta đã đến cuối danh sách bên trái, hãy thêm các phần tử
        # từ danh sách bên phải
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Nếu chúng ta đã đến cuối danh sách bên phải, hãy thêm các phần tử
        # từ danh sách bên trái
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # Nếu danh sách là một phần tử duy nhất, hãy trả về
    if len(nums) <= 1:
        return nums

    # Sử dụng phép chia tầng để lấy điểm giữa, các chỉ số phải là số nguyên
    mid = len(nums) // 2

    # Sắp xếp và hợp nhất từng nửa
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Hợp nhất các danh sách đã sắp xếp thành một danh sách mới
    return merge(left_list, right_list)


random_list_of_nums = [120, 45, 68, 250, 176]
random_list_of_nums = merge_sort(random_list_of_nums)
print(random_list_of_nums)