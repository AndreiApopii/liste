with open('prenume.ani.txt','r') as f:
    x=f.readline()
    z=f.readline()
    prenume=x.split()
    varsta=z.split()
    for i in range(0,len(prenume)):
        for j in range(0,len(varsta)):
           print(prenume[i],'are varsta de',varsta[j],'ani'.)
    prenume.append(['Andreea','Ioan'])
    varsta.append([34,23])
    print(prenume,varsta,sep='\n')
    print(prenume[0:3])
    print(prenume[::-1])
    print(prenume[2],varsta[2])
    print(prenume[4],varsta[4])
    print(prenume[:5],varsta[:5])
    