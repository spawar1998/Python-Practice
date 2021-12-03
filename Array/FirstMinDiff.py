import array as arr
a = arr.array('i',[8,15,16,8,10,15,9])
min = smin = a[0]
for i in range(0,len(a)):
    if min>a[i]:
        smin=min
        min=a[i]
print(smin-min)  