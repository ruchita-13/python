# num=int(input("Enter the number:"))
# sum=0 
# while(num<=100 and num!=0):
#     print(num)
#     temp=num%10
#     sum=sum*10+temp
#     num=num//10
#     print(sum)

# num=100
# fact=1
# while(num<=100 and num>0):
#     print(num)
#     fact=fact*num
#     num=num-1
# print(fact) 

#Neon number(multiple of number amd then addition of that equal to that number...) 
# num=int(input("Enter the number:"))
# sum=0
# dig=0
# sq=num*num
# while(sq!=0):
#     temp=sq%10
#     dig=dig+temp
#     sq=sq//10
# if(num==dig):
#     print("it is neon num")
# else:
#     print("not neon")


#Neon in for loop
# num=8
# sq=num*num
# sum=0
# for i in range(num):
#     temp=sq%10
#     sum=sum+temp
# print(sq)
# print(sum)
# if num==sum:
#     print("neon")
# else:
#     print("not neon")
    

#spy number(multi and addition should be same)
# num=int(input("Enter the number:"))
# sum=0 
# temp=1
# while(num!=0):
#     dig=num%10
#     sum=sum+dig
#     temp=temp*dig
#     num=num//10
#     print(sum)
#     print(temp)
# if(sum==temp):
#     print("the number is spy")
# else:
#     print("not spy")

#for spy number
# num=5
# sum=0 
# temp=1
# for i in range(num):
#     dig=num%10
#     sum=sum+dig
#     temp=temp*dig
# print(sum)
# print(temp)
# if(sum==temp):
#     print("spy")
# else:
#     print("not")
    
    
# num=22
# sum=0 
# temp=1
# for i in range(num):
#     dig=num%10
#     sum=sum+dig
#     temp=temp*dig
#     num=num//10
# if(sum==temp):
#     print("spy")
# else:
#     print("no")
    
    
#factorial
# num=3
# sum=1
# for i in range(num,0,-1):
#     sum=sum*i
#     print(sum)

#count the no:
# num=526485
# num=str(num)
# count=0 
# for i in num:
#     count=count+1
#     print(count)


#palindrome no:
# num=323
# num=str(num)
# reverse=""
# for i in num:
#     reverse=i+reverse
# if(num==reverse):
#     print("the number",num,"is palindrome")
# else:
#     print("the number",num,"not palindrome")

#reverse no:
# num=789
# num=str(num)
# reverse=""
# for i in num:
#     reverse=i+reverse
#     print(reverse)


# maximum = int(input(" Please Enter the Maximum Value : "))
# for num in range(1, maximum):
#     temp = num
#     reverse = 0
#     while(temp > 0):

#         Reminder = temp % 10

#         reverse = (reverse * 10) + Reminder

#         temp = temp //10

#         if(num == reverse):

#             print(num)

# for i in range(-10,0,1):
#     print(i)

# for i in range(1,10):
#     print(i)
# else:
#     print("done")

#armstrong no
# num=407
# sum=0 
# num=str(num)
# for i in num:
#     sum=sum+int(i)**3
# if(sum==int(num)):
#     print("The armstrong")
# else:
#     print("Not")

    
# num=407
# sum=0
# num=str(num) 
# slen=len(num)
# while(int(num)>0):
#     temp=int(num)%10
#     sum=sum+temp**slen
#     num=int(num)//10
#     if(sum==int(num)):
#         print("yes")
#     else:
#         print("no")

#odd and even numbers
# maxnum=int(input("Enter the maxnum:"))
# minnum=int(input("Enter the minnum:"))
# sum=0
# for num in range(1,maxnum,minnum):
#     print(num)
#     temp=num
#     if(temp%2==0):
#         print("even numbers")
#     else:
#         print("odd number")
        
        

#prime number
# lower=1 
# upper=100
# for Number in range(lower,upper+1):
#         if Number>1:
#             for i in range (2, Number):  
#                 if (Number % i) == 0:  
#                     break  
#             else:  
#                 print (Number)  

#sum of the odd numbers    
# end=5
# start=1
# total=0
# for i in range(start,end+1):
#     if i%2!=0:
#         total=total+i
# print(total)

#sum of even numbers
# end=10
# start=2
# total=0
# for i in range(start,end+1):
#     if i%2==0:
#         total=total+i
# print(total)

#Patterns.........
# *****
# *****
# *****
# *****
# *****
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end="")
#     print()


# *
# **
# ***
# ****
# *****    
# for i in range(1,6):
#     for j in range(1,-1):
#         print("*",end="")
#     print()

# 12345
# 12345
# 12345
# 12345
# 12345    
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end="")
#     print()

# 11111
# 22222
# 33333
# 44444
# 55555   
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end="")
#     print()

# 1
# 12
# 123
# 1234
# 12345
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()



# for i in range(1,6):    
#     for j in range(i):    
#         print(i, end=' ')      
#     print()    

# for i in range(5,0,-1):
#     for j in range(0,i):
#         print(i,end="")
#     print()
    

# n=int(input("Enter the number of rows"))
# for i in range(n):
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()

# num=int(input("Enter the number:"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(i*2-1,end=" ")
#     print()

#     5
#    55
#   555
#  5555
# 55555        
# num=5
# for i in range(num):
#     for j in range(num-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(num,end="")
#     print()

# num=6
# for i  in range(num,0,-1):
#     for j in range(num-i-1):
#         print(" ",end="")
#     for j in range(0,i):
#         print(num,end="")
#     print()
# 12345
#  2345
#   345
#    45
#     5    
# num=5
# for i in range(num):
#     for j in range(i+1):
#         print(" ",end = "")
#     for j in range(i,num): 
#         print(j+1,end = "") 
#     print()

# 7777777
#  666666
#   55555
#    4444
#     333
#      22
#       1
# num=7
# for i in range(num,0,-1):
#     for j in range(num-i+1):
#         print(" ",end="")
#     for j in range(0,i):
#         print(i,end="")
#     print()

# 11111
#  2222
#   333
#    44
#     5
# num=5
# for i in range(1,num+1):
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(num-i+1):
#         print(i,end="")
#     print()

# 54321
#  5432
#   543
#    54
#     5
# num=5
# for i in range(num+1):
#     for j in range(i+1):
#         print(" ",end = "")
#     for j in range(num,i,-1): 
#         print(j,end ="") 
#     print()

# num=5
# for i in range(num-1,-1,-1):
#     for j in range(num-i+1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(num-j,end=" ")
#     print()

# num=5
# for i in range(num):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(num-i):
#         print(i+1,end=" ")
#     print()

# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# num=7
# for i in range(num):
#     for j in range(i+1):
#       print("*",end=" ") 
#     print()  
        
        
        
#            *
#           **
#          ***
#         ****
#        *****
#       ******
#      *******
#     ********
#    *********
#   **********
# num=10
# for i in range(num):
#     for j in range(num-i+1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()


#            * 
#           * *
#          * * *
#         * * * *
#        * * * * *
#       * * * * * *
#      * * * * * * *
#     * * * * * * * *
#    * * * * * * * * *
#   * * * * * * * * * *
# num=10
# for i in range(num):
#     for i in range(num-1,-1,-1):
#         for j in range(num-i+1):
#             print(" ",end="")
#         for j in range(i+1):
#             print("*",end=" ")
#         print()



#   * * * * * * * * * *
#    * * * * * * * * *
#     * * * * * * * *
#      * * * * * * *
#       * * * * * *
#        * * * * *
#         * * * *
#          * * *
#           * *
#            *
# num=10
# for i in range(num-1,-1,-1):
#     for j in range(num-i+1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# * * * * * * * 
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# num=7
# for i in range(num):
#     for j in range(num-i):
#         print("*",end=" ")
#     print()


# * * * * * * * 
#   * * * * * *
#     * * * * *
#       * * * *
#         * * *
#           * *
#             *
# num=7
# for i in range(num):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(2*num-i):
#         print("*",end=" ")
#     print()

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15
# num=5
# temp=0
# for i in range(1,num+1):
#     for j in range(i):
#         temp=temp+1
#         print(temp,end=" ")
#     print()

# 1 
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25    
# num=5 
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(i*j,end=" ")
#     print()



# num=5
# temp=1
# for i in range(1,num):
#     for j in range(1,i+1):
#         print((j**2-1),temp,end=" ")
#     print()
    

# num=5
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print((num)*(-1)+j,end=" ")
#     print()
    
# num= 5

# 1 
# 1 2
# 1 2 4
# 1 2 4 7
# 1 2 4 7 11
# num=5
# for i in range(num):
#     temp = 1
#     print(temp,end=" ")
#     for j in range(1, i +1):
#         temp=temp+ j
#         print(temp, end=' ')
#     print()

# num= 5
# for i in range(1,num+1):
#     for j in range(1, i + 1):
#         print(j**2-1,end=' ')
#     print()

# for i in range(20,0,-2):
#     print(i)


