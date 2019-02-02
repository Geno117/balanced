#!/usr/bin/python
def balanced(a):
	x=0
	y=0
	for i in a:
		if(i=='x'):
			x+=1
		elif(i=='y'):
			y+=1
	if (x==y):
		print("True")
		return True
	print('False')
	return False

ls=['xxxyyy','yyyxxx','xxxyyyy','yyxyxxyxxyyyyxxxyxyx','xyxxxxyyyxyxxyxxyy','','x']

for l in ls:
	balanced(l)

def optbalance(a):
	if a == '':
		print('True')
		return True
	dictls = {}
	for i in a:
		if i in dictls:
			dictls[i]+=1
		else:
			dictls[i]=1
	ls = dictls.values()
	for x in range(len(ls)-1):
		if ls[x]!=ls[x+1]:
			print("False")
			return False
	print("True")
	return True

print("optbalance")
for l in ls:
	balanced(l)