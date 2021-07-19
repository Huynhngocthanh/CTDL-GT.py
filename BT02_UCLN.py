# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:05:13 2021

@author: Admin
"""

a = int(input('nhap a = '))
b = int(input('nhap b = '))

def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);
print('UCLN của',a,'và',b,'là:',uscln(a,b))