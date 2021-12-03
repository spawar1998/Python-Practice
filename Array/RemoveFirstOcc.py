# Write a Python program to remove the first occurrence of a specified element from an array.

import array as arr
a = arr.array('i',[1, 3, 5, 3, 7, 1, 9, 3])
n,cnt=3,0
for i in range(0,len(a)-1):
    if n==a[i]:
        cnt+=1
    if cnt==1:
        a.pop(i)
    print(a[i],end=' ')