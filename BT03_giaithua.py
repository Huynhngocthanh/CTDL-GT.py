# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:05:59 2021

@author: Admin
"""

n = int(input("Nhập số cần tính giai thừa: "))
 
def giaithua(n):
    if n == 0:
        return 1
    return n * giaithua(n - 1)
 
print(giaithua(n))