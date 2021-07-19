# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:19:24 2021

@author: Admin
"""

def partition(nums, low, high):
    # Chúng ta chọn phần tử ở giữa để làm trục. Một số triển khai chọn
    # phần tử đầu tiên hoặc phần tử cuối cùng. Đôi khi giá trị trung bình trở thành
    # trục xoay hoặc một trục ngẫu nhiên. Có nhiều chiến lược khác có thể
    # đã chọn hoặc đã tạo.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Nếu một phần tử tại i (bên trái trục quay) lớn hơn
        # phần tử tại j (ở bên phải trục quay), sau đó hoán đổi chúng
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Tạo một hàm trợ giúp sẽ được gọi một cách đệ quy
    def _quick_sort(items, low, high):
        if low < high:
            # Đây là chỉ mục sau trục xoay, nơi danh sách của chúng ta được phân chia
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)



random_list_of_nums = [22, 5, 1, 18, 99]
quick_sort(random_list_of_nums)
print(random_list_of_nums)