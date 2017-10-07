import cmath
import numpy
sx=[[0.,1.],[1.,0.]]
sy=[[0.,complex(0,-1)],[complex(0,1),0.]]
sz=[[1.,0.],[0.,-1.]]
s1=0
s2=3+5j
#r=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#c=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#s=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def tensor(a,b):
    for i in range(4):
        for j in range(4):
            c[i][j]=(a[(i)//2][(j)//2]*b[(i)%2][(j)%2])
    #return c
def sm(x,y):
    for i in range(4):
        for j in range(4):
            s[i][j]=(x[i][j])+(y[i][j]).real
    #return s

tensor(sx,sx)
t1=c.copy()
print(t1[0][0].real)
tensor(sy,sy)
t2=c.copy()
print(t2[0][0].real)
tensor(sz,sz)
t3=c.copy()
l=t1[0][0]+t2[0][0]
print(l)
sm(t1,t2);
s1=s
for i in range(4):
    for j in range(4):
        c[i][j]=t1[i][j]+t2[i][j]
print(c)

#s2=sm(s1,t3,c)
#print(s2)
