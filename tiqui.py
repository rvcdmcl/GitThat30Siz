# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 14:20:05 2022

@author: Rovic Dimacali
"""

def computePay(hr, rt):
    if hr > 40:
        ans = (40*rt) + ((hours - 40) * ((rt/2) + rt))
        return ans
    elif hr <= 40:
        ans = hr * rt
        return ans

x = input("Enter Hours: ")
y = input("Enter Rate: ")

hours = int (x)
rate = float (y)

output = computePay(hours, rate)
print("Hours: ", hours)
print("Rate: ", rate)
print("Pay: ", output)