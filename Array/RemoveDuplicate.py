# Write a Python program to remove all duplicate elements from a given array and returns a new array.
# Original array: 1 3 5 1 3 7 9
# After removing duplicate elements from the said array: 1 3 5 7 9

import array as arr
a = arr.array('i',[1,3,5,1,3,7,9])
l=[]
# print(len(a))
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i] not in l:
            l.append(a[i])
            print(a[i],end=' ')