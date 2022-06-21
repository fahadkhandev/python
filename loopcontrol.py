# for i in range(0,11):
#     if(i==6):
#         continue
#     print(i)

# for i in range(0,11):
#     if(i==4):
#         break
#     print(i)

# for i in range(0,21):
#     if(i%2==0):
#         continue
#     print(i)
# for i in range(0,21):
#     if(i%2!=0):
#         continue
#     print(i)
n=int(input("ENter number : "))
check=0
for i in range(2,n):
    if(n%i==0):
        check+=1
if(check==0):
    print("prime ")
else:
    print("not prime ")