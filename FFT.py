from math import e
from math import pi
from math import floor

def fft(xv,av):
    if len(av)==1:
        return [xv[0]*av[0]]
    b=[]
    c=[]

    for i in range(len(av)):
        if i%2==0:
            b.append(av[i])

        else:
            c.append(av[i])
    temp=floor(len(av)/2)
    b=xv[0:temp]
    d=[x**2 for x in b]
    p=fft(d,b)
    q=fft(d,c)
    v=[]
    for i in range(len(p)):
        v.append(p[i]+xv[i]*q[i])
    for i in range(len(p)):
        v.append(p[i]+xv[i+len(p)]*q[i])
    return v

def getroot(av):
    root=[]
    length=len(av)
    for i in range(length):
        root.append(e**(pi*2*1j*i/length))
    return root


def main():
    p=[]
    for i in range(2**20):
        p.append(i)
    print(fft(getroot(p),p))


main()




