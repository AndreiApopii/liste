x=''
with open ('input.txt','r') as f:
	while True:
	   a=f.readline()
	   x+=a
	   if len(a)==0:
		   break
y=list(x.split('\n'))
y.sort()
z=str(y)
with open('lista.txt','w') as f:
   f.write(z)