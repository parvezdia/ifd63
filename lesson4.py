"""
For loop
===========

for varin collection :
    statements
        ...
"""


#  for x in [1,2,3,4,5]:
#     print(x,end='\t')


# for x in [1,2,3,4,5]:
#     print(x,end='\t')

# print("\n\n#####################\n\n")
# for x in range(1,102,5):
#     print(x,end='\t') 

# sum=0
# for x in range(5,8+1):
    
#     sum =sum +x**2

# print(sum)


# sum=0
# for x in range(7,12+1):
    
#     sum =sum +x**2

# print(sum)


# fact =1
# num =4
# for x in range(1,num+1):
#     fact = fact * x

# print(f"The factorial of {num} is{fact}")



# Prime Number
# n=14
# for x in range(2,n):
#     if n%x==0:
#         print("Not a prime number")
#         break
#     else:
#         print("Prime number")
#         break

    #  Reverse Number 

rev = 0
num=2345
n = num

while num>0:
    digit = num % 10
    rev = rev * 10 +digit
    num = num // 10

print(rev)    