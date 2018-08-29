#Ques1

f=open('file1.txt','r')
new=f.read()
print(new)
f.close()
print()


#Ques2

f=open("file1.txt",'r')
data=f.read()
word=data.split()
dict={}
for x in word:
    dict[x]=word.count(x)
print(dict)
print()


#Ques3

with open('file1.txt', 'r') as f1:
    with open('file2.txt', 'w') as f2:
        f2.write(f1.read())


#Ques4

str1=[]
str2=[]
s=str()
with open('file1.txt','r') as f1:
    with open('file2.txt','r') as f2:
       str1+=f1.readlines()
       str2+=f2.readlines()
       for x,y in zip(str1,str2):
           print(x)
           print(y)
           s+=x+y
with open('file3.txt','w') as f3:
      f3.write(s)



#ques5
with open('file4.txt','w') as f:
   for i in range(10):
      x=int(input("Enter number: "))
      f.write("%d "%(x))

with open('file4.txt','r') as f:
   data=f.readlines()
   for no in data:
       a=no.split()
   a.sort()

with open('file5.txt','w') as f:
   for i in a:         
      f.write("%s "%(i))
