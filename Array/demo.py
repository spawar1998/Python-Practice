import array as arr
str = "vaibhav"
l=list(str)
a = arr.array('i',[0]*130)
for i in range(0,len(l)):
	a[ord(l[i])]+=1
for i in range(0,len(l)):
	if a[ord(l[i])]>0:
		print(l[i]," = ",a[ord(l[i])])
		a[ord(l[i])]=0
	
	