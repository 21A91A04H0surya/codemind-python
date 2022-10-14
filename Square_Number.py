num=int(input())
i=1
for i in range(1,num+1,1):
    d=i*i
    i=i+1
    if d==num:
      print("True")
      break
if(d!=num):
    print("False")
    