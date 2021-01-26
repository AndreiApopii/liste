x=[5,7,9,0,-3,-9,1]
print('conținutul listei',x)
x1=sorted(x)
print('lista sortată în ordine crescătoare',x1)
x3=x
x3.sort(reverse=True)
print('lista sortată în ordine descrescătoare',x3)
print('numărul de elemente din listă',len(x))
print('elementul MAX=',max(x))
print('elementul MIN=',min(x))
x4=x.extend([111])
print(x4)
x5=x.insert(2,222)
print(x5)
