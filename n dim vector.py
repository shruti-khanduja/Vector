class Vectors:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        str1=''
        j=1
        for i in self.vec:
            if j==1 or i<0:
                str1+=f'{(i)}v{j} '
            elif i>0:
                str1+=f'+{(i)}v{j} '
            j+=1
        return str1
    def __add__(self,v2):
        add=[]
        if len(self.vec)>len(v2.vec):
            for x in range(len(self.vec)-len(v2.vec)):
                v2.vec.append(0)
        else:
            for x in range(len(v2.vec)-len(self.vec)):
                self.vec.append(0)
        for i in range(len(self.vec)):
                add.append(self.vec[i]+v2.vec[i])
        return Vectors(add)
    def __mul__(self,v2):
        s=self.vec
        v=v2.vec
        dot=0
        if len(s)>len(v):
            for x in range(len(s)-len(v)):
                v.append(0)
        else:
            for x in range(len(v)-len(s)):
                s.append(0)
        for i in range(len(s)):
                dot+=s[i]*v[i]
        return dot

n=int(input(f"Enter dimension of the vector 1 "))
v=[]
for i in range(n):
    a=int(input(f"Enter v{i+1} "))
    v.append(a)
v1=Vectors(v)
n=int(input(f"Enter dimension of the vector 2 "))
v=[]
for i in range(n):
    a=int(input(f"Enter v{i+1} "))
    v.append(a)
v2=Vectors(v)
print(v1)
print(v2)
print(v1+v2)
print(v1*v2)

# num=int(input("How many vectors do you wish to operate on "))
# array=[]
# for i in range(num):
#     n=int(input(f"Enter dimension of the vector {i+1} "))
#     v=[]
#     for i in range(n):
#         a=int(input(f"Enter v{i+1} "))
#         v.append(a)
#     array.append(v)
# for i in range(num):
#     Vectors(array)
    

