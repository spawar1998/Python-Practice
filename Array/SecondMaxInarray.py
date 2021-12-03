import array as arr
a = arr.array('i',[-1,0,2,3,0,0])
max = smax = min = a[0]
for i in range(0,len(a)):
    if a[i]>max:
        smax = max
        max = a[i]
    if a[i]<min:
        min=a[i]
print(smax-min)