

#x = int(input("enter number :"))

#if x==1:
#   print ("monday")    
#elif x == 2:
#    print ("tuesday")
#elif x ==3:
#    print ("wed")
#elif x == 4:
#    print ("thur")
#elif x == 5:
#    print ("fri")
#elif x == 6:
#    print("saturdar")
#elif x==7:
#    print("sunday")
#else :
#    print("invalid ")
# a = int(input("enter first number : "))
# b = int(input("enter second number : "))
# mul = a*b
# print(mul)
# print (a*b)

#print ('name', 'is', 'james',sep = "**")
# num=8
# print('%o'% nu
 
# a=2
# b=3
# # print(a+b)

# a = 9
# if a>0 :
#     print ("positive")
# else :
#     print ("neg")

# s = "john"
# print(s)
# print(s[2])
# s = " \*sjfegf\\nbh\trr\nrs*\"
# print (s)
# def dets(name,city,skill,age):
#     print(name,city,age,skill)

# dets(city="BHOPAL",Skill="PYTHON",name="john",age=12)
# def sum(a,b):
#     s = a+b
#     print(s)
# sum(1,2)

# sum = lambda a,b : a+b
# print(sum(1,2))

#iterative ques
# 1 ACCEPT AN INTEGER AND PRINT HELLO WORLD N TIME
# a = int(input("please give me the number:"))

# for i in range(a):
#     print ("hello world")

# 5 TABLE
# for i in range(5,51,5):
#     print(i)

# 10 TABLE
# for i in range(10,101,10):
#     print(i)

# table user input
# a = int(input("please tell your number"))
# for i in range(a,(a*10)+1,a): #a*10 +1  == n-1 tak chalta h
#     print(i)

# a = int(input("please tell your number:"))
# n =10             #ostel me 
# for i in range(a,(a*n)+1,a):
#     n = 

# table in proper manner
# a = int(input("please tell your number:"))
# for i in range(1,11):
#     print(f"{a} * {i} = {a*i}")

#
# a = int(input("please tell your number:"))
# b =int(input("till where you want to print:"))
# for i in range(1,b+1):
#     print(f"{a} * {i} = {a*i}")

# Q7. condirional statement

# a = int(input("enter first number : "))
# b = int(input("enter second number : "))
# c = int(input("enter third number : "))

# if a==b and b==c:
#     print("all are equal")
# elif a==b or a==c:
#     print("any two are equal")
# else :
#     print("not equal")

# Q8. 

# a = int(input("enter first number:"))
# b = int(input("enter second number:"))

# if a>b:
#     print("a is greater")
# elif a<b:
#     print("b is greater ")
# else:
#     print("both are equal")

# Q9,10.
# a = input("enter F or f for female and enter M or m for male: ")

# if a=="F" or a=="f":
#     print("GOOD MORNING MAM!!!")
# elif a=="M" or a=="m":
#     print("GOOD MORNING SIR!!!")
# else:
#     print("input is not matching")

# Q11.
# a = int(input("enter number : "))
# if a%2==0:
#     print("number is even")
# else:
#     print("number is odd ")

#Q12.

# name = input("enrer your name :")
# age = int(input("enter ypur age : "))

# if age >=18:
#     print(f"Hello {name} , you are valid voter")
# else:
#     print(f"Sorry {name} , you cant vote")


#Q14. leap yesar or not leap year

# year = int(input("please give your year : "))

# if year % 4 == 0 and year % 100 !=0:
#     print("leap year")
# elif year % 100 == 0 and year % 400 == 0:
#     print("leap year")
# else :
#     print("not a leap year")

#Q13. compound interest

# p = int(input(" please enter your p : "))
# t = int(input(" please enter your t : "))
# r = int(input(" please enter your r : "))

# ci = p*(1+(r/100))**t
# print(ci)

# 15) Accept an english alphabet from user and check if it is a consonent or a vowel;
# x=input("enter alphabet:")

# if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'): 
#     print("vowel")
# else:
#     print("consonant")



#iterative ques
# 1 ACCEPT AN INTEGER AND PRINT HELLO WORLD N TIME
# a = int(input("please give me the number:"))

# for i in range(a):
#     print ("hello world")

# 5 TABLE
# for i in range(5,51,5):
#     print(i)

# 10 TABLE
# for i in range(10,101,10):
#     print(i)

# table user input
# a = int(input("please tell your number"))
# for i in range(a,(a*10)+1,a): #a*10 +1  == n-1 tak chalta h
#     print(i)

# a = int(input("please tell your number:"))
# n =10             #ostel me 
# for i in range(a,(a*n)+1,a):
#     n = 

# table in proper manner
# a = int(input("please tell your number:"))
# for i in range(1,11):
#     print(f"{a} * {i} = {a*i}")

#
# a = int(input("please tell your number:"))
# b =int(input("till where you want to print:"))
# for i in range(1,b+1):
#     print(f"{a} * {i} = {a*i}")

# Q2
# n = int(input("enter number:"))

# for i in range (1,n+1):
#     print(i)

#Q3
# n = int(input("enter number:"))

# for i in range (n,0,-1):
#     print(i)

#Q4 
# n = int(input("enter number:"))

# for i in range(1,11):
#     print(f"{n}*{i} = {n*i}")


# Q5
# n = int(input("enter number:"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

#Q6  factorial

n = int(input("enter number : "))
multi = 1

for i in range(1,n+1):
    multi=multi * i
print(multi)

#Q7 even and odd

# n = int(input("enter number :"))

# odd = 0 
# even = 0

# for i in range(1,n+1):
#     if i%2==0:
#         even = even + i
#     else :
#         odd = odd + i
# print(f"sum of even numbers are : {even} \n sum of odd number are : {odd}")



# i = 20
# while i > 10:
#     print("hello")



#Q8. print all the numbers which are either divisible by 3 or 5 in a range  
# n = int(input("enter your number:"))

# for i in range(1,n+1):
#     if i%3==0 or i%5==0:
#         print(i)
        
#Q9. Print all the factors of a number.
# n = int(input("enter your number:"))

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)


# Q10. Print the sum of all factors of a number
# n = int(input("enter your number:"))
# sum = 0
# for i in range(1,n+1):
#     if n%i==0:
#         sum = sum + i 
# print(sum)


#Q11. Accept a number and check if it a perfect number or not. agar number ka factor equal wahi number aa jayega

# n = int(input("enter number:"))
# sum = 0
# for i in range(1,n):
#     if n%i==0:
#         sum = sum + i
# if sum == n:
#     print("perfect number")
# else:
#     print("not perfect")
        

# Q27.  Seprate each digit of a number and print it on the new line

# a = 123
# while a>0:
#     z = a%10
#     print(z)
#     a = a//10

#Q. reverse number
 
# a = int(input("enter number : ")) 
# rev=0
# while a>0:
#     z = a%10
#     rev = rev*10 + z 
#     a = a//10
# print(rev)

# pallindrome

# a = int(input("enter numer : "))
# copy = a
# rev=0
# while a>0:
#     z = a%10
#     rev = rev*10 + z
#     a = a//10
    
# if  rev == copy:
#     print("pallindrome")
# else:
#     print("no a pallindrome")+



# check whether number is prime or not

# n = int(input("enter numer :" ))
# count = 0
# for i in range (1,n+1):
#     if n%i==0:
#         count = count + 1
# if count == 2 :
#     print("prime")
# else : 
#     print("not")


# n = int(input("enter number : "))
# for i in range(2,(n//2)+1):
#     if n%i==0:
#         print("not a prime number")
#         break
# else:
#         print("prime number")


# print all the prime number

# n=int(input("enter number : "))
# for i in range(2,n+1):
#     count = 0
#     for j in range(1,i+1):
#         if i%j==0:
#             count = count + 1
#     if count == 2:
#         print(i)

# ###
# for i in range(2,101):
#     a=i
#     count=0

### for finding how many prime number in a given range.
# count=0
# for i in range(1,1001):
# 

## STRING

# Q31. Print string in reverse,its length,in uppercase,lowercase and copy into another string.
##reverse method 1
# a = "harsh"
# b = ""
# for i in range(4,-1,-1):
#     b = b+a[i]
# print(b)

##method 2
# a ="harsh"
# print(a[::-1])

##length
# a= "harsh"
# print(len(a))

##uppercase
# a= "harsh"
# print(a.upper())

##lower case
# a= "HARsh"
# print(a.lower())

##copy into another string
#1. a= "harsh"
#   b=a

#2. a= "harsh"
#   b=a.copy()

## string iterative
# a= "harsh"
# for i in a:
#     print(i)
# or
# a= "harsh"
# for i in range(0,len(a)):
#     print(i)
# # or
# a= "harsh"
# for i in range(0,len(a)):
#     print(a[i])

# 32) Arrange string characters such that lowercase letters should come first.
      #method 1
# a = "HelloWoRLD"
# lowerstr=""
# upperstr=""

# for i in a:
#     if i.islower():
#         lowerstr=lowerstr+i
#     else:
#         upperstr=upperstr+i
# print(lowerstr+upperstr)
 
     #method 2

# a = "HelloWoRLD"
# lowerstr=""
# upperstr=""

# for i in a:
#     if i.islower():
#         lowerstr=lowerstr+i
#     else:
#         upperstr=upperstr+i
# newstr=lowerstr+upperstr
# print(newstr)


# 33) Count all letters, digits, and special symbols from a given string
#     Given: str1 = "P@#yn26at^&i5ve"
#     Expected Outcome:
#     Total counts of chars, digits, and symbols
#     Chars = 8
#     Digits = 3
#     Symbol = 4

#solution
# a = "P@#yn26at^&i5ve"
# alpha=0
# number=0
# spchar=0 

# for i in a:
#     if i.isdigit():
#         number=number+1
#     elif i.isalpha():
#         alpha=alpha+1
#     else:
#         spchar=spchar+1
# print(f"characters = {alpha}\nnumber = {number}\nspecial characters = {spchar}")


# 34) Compare two strings without using inbuilt functions.
# a="hello"
# b="elohl"
# if len(a)!=len(b):
#     print("not similar")
# else:
#     flag=0
#     for i in a:
#         if i in b:
#             continue
#         else:
#             print("not similar")
#             flag=1
#             break
#     if flag == 0 :
#         for i in b:
#             if i in a:
#                 continue
#             else:
#                 print("not similar")
#             break
#         else:
#             print("similar")

# 35) Count Vowels from given string

# a = "my name is ayushi"
# count=0
# for i in a:
#     if i in "aeiouAEIOU":
#         count=count+1
# print(count)

#36) Reverse a string
# a= "hello"
# print(a[::-1])

# a= "hello"
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev=rev+a[i]
# print(rev)


#37 Check string is Pallindrome or not**
# a="malayalam"
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev=rev+a[i]

# if rev==a:
#     print("pallindrome")
# else:
#     print("not pallindrome")


## LIST

#38) Accept List elements and reprint it

# l=[]
# n=int(input("please tell how many number you want : "))
# for i in range(n):
#     z=int(input("please tell your numbers : "))
#     l.append(z)
# print(l)

#Q. fabbinacci series
# a=0
# b=1
# v=int(input("how many numbers you want : "))
# for i in range(v):
#     c=a+b
#     print(c)
#     a=b
#     b=c

# #Q. fabbinacci series by list
# a=0
# b=1
# l=[0,1]
# v=int(input("how many numbers you want : "))
# for i in range(v-2):
#     c=a+b
#     l.append(c)
#     a=b
#     b=c

# Q. another way of list of fabbinacci series 

# a=[0,1]
# n=int(input("how many numbers you want : "))
# for i in range(n):
#     a.append(a[len(a)-1]+a[len(a)-2])
# print(a)


#Q. print table in list
# l=[]
# a = int(input("please tell your number"))
# for i in range(a,(a*10)+1,a): 
#     l.append(i)
# print(l)


# l=[]
# positive=[]
# negative=[]
# n=int(input("enter your lenght :"))
# for i in range(n):
#     z=int(input("tell your number : "))
#     l.append(z)
# for i in l:
#     if i>=0:
#       positive.append(i)
#     else:
#       negative.append(i)
# print(f"total positive numbers are {positive}")
# print(f"total negative numbers are {negative}")
# print(f"total positive elements are {len(positive)}")
# print(f"total negative elements are {len(negative)}")


# l=[34,54,-34,8,-99,-97,77,65]
# neg=[i for i in l if i>=0]
# pos=[i for i in l if i<0]
# print(neg)
# print(pos)


#Q42. Accept size n from user and create a n size List then take n inputs into the and finally .Print the sum of all elements in the List

# a=[56,78,90,12,34,56]
# sum=0
# for i in range(len(a)):
#     if i ==len(a)-1:
#         print(f"{a[i]} = " , end = " ")
#     else:
#         print(f"{a[i]} +" , end = " ")
#     sum=sum+a[i]
# print(sum)


#Q43. Mean of List elements.

# a=[34,54,2,12]
# sum=0
# for i in a:
#     sum=sum+i
# print(f"mean is {sum/len(a)}")


#Q44) Find the greatest element and print its index too.

# a=[56,78,90,12,34,56]
# max=0
# for i in a:
#     if i>max:                       // for max only
#       max=i
# print(max)


# a=[12,2432,546,15,987654,12345,7654]
# max=0
# index=0
# for i in range(len(a)):
#     if a[i]>max:                   // for max and index 
#         max=a[i]
#         index=i
# print(max)
# print(index)
# 
### FIND GREATEST NUMBER BY FUNCTION
# def maxfinder(a):
#     max=0
#     for i in a:
#         if i>max:
#             max=i
#     print(max)                 

# l=[23,654,123,6543,234,76543,345]
# d=[123,2345,6543,23456,76543,234567]
# maxfinder(l)
# maxfinder(d)


# ## AVERAGE
# l=[6,8,3,4,0,2,1]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum/len(l))
# print(f"mean is {sum/len(l)}")


## Q) Fnd the second greatest element for sorted element.
# l=[1,4,7,8,17,25]
# max=0
# max2=0
# for i in l:
#     if i>max:
#         max2=max
#         max=i
# print(max2)


## Q.46) Fnd the second greatest element .
# l=[1,4,7,8,17,25,24]
# max=0
# max2=0
# for i in l:
#     if i>max:
#         max2=max              // only values
#         max=i
#     elif i>max2:
#         max2=i
# print(max)
# print(max2)



# a=[1,4,7,8,17,25,24]
# max=0
# max2=0
# index1=0
# index2=0
# for i in range(0,len(a)):
#     if a[i]>max:
#         max2=max           #   // values and index
#         max=a[i]
#         index2=index1
#         index1=i

#     elif a[i]>max2:
#         max2=a[i]
#         index2=i
# print(max,index1)
# print(max2,index2)


##linear search
# a=[1,4,3,2443,34,23,4,23,543]
# v=int(input("which number you want to find : "))
# for i in range(len(a)):
#     if a[i]==v:
#         print(f"your number {v} found at index {i}")
#         break
# else : 
#     print("your number doesn't exist")



## BUBBLE SORT
# a=[2,4,3234,54,23,6,2]
# for j in range(len(a)):         #(or for j in l:)
#     for i in range(0,len(a)-1):
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
# print(a)



# a=[2,4,3234,54,23,6,2]
# for j in range(len(a)):
#     for i in range(0,len(a)-j-1):            // for decreasing the time complexity in this by doing -j we donot need to go again and again
                                            # //    at the last number bbecause the last element is already largest.
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
# print(a)



## Q.47) Check if List is sorted or not.
# a=[1,2,3,4,5]
# for i in range(0,len(a)-1):
#         if a[i]<a[i+1]:
#                 continue
#         else:
#             print("not sorted")
#             break
# else:
#     print("sorted")


## above question in function
# def checkkar(a):
#     for i in range(0,len(a)-1):
#         if a[i]<a[i+1]:
#                 continue
#         else:
#             print("not sorted")
#             break
#     else:
#         print("sorted")

# checkkar([1,23,432,1234,54312])


## by using return
# def checkkar(a):
#     for i in range(0,len(a)-1):       
#         if a[i]<a[i+1]:
#                 continue
#         else:
#             return("not sorted")
#             break
#     else:
#         return("sorted")

# print (checkkar([1,23,432,1234,54312]))


## Q.48) Pallindromic List - Write a program to check if elements of an List are same or not it read from front or bacExample : arr= [2,3,15,15,3,2]

# l=[2,3,4,5,4,3,2]
# v=[]
# for i in range(len(l)-1,-1,-1):
#     v.append(l[i])                         #  // (space complexity = n2 and time complexity = n )
# if v==l:
#     print("pallindrome")
# else:
#     print("pallindrome")



# l=[2,3,4,5,4,3,2]
# z=len(l)-1
# for i in range(0,(len(l)//2)):
#     if l[i]==l[z]:                              # // (space complexity = n  and time complexity = n/2)
#         z=z-1
#         continue     
#     else:
#         print("not pallindrome")
#         break
# else:
#     print("pallindrome")



# l=[2,3,4,5,4,3,2]
# for i in range(0,(len(l)//2)):
#     if l[i]==l[(len(l)-1)-i]:                              # // (space complexity = n  and time complexity = n/2)
#         continue     
#     else:
#         print("not pallindrome")
#         break
# else:
#     print("pallindrome")


# def pallindrome(l):
#        for i in range(0,(len(l)//2)):
#              if l[i]==l[(len(l)-1)-i]:                            
#                    continue     
#              else:
#                   return("not pallindrome")
      
#        else:
#          eturn("pallindrome")

# print(pallindrome([1,3,1,234,234,234]))




#### DICTIONARY (hash map) questions


# a ={1:23,2:34,3:344}
# b={4:765,5:54,6:1}
# a.update(b)
# print(a)


# a ={1:23,2:34,3:344}
# b={3:765,5:54,6:1}
# a.update(b)
# print(a)


# a ={1:23,2:34,3:344}
# a.update({4:32})
# print(a)

# a ={1:23,2:34,3:344}
# a[4] = 54
# print(a)

## Q.49) Write a Python program to iterate over dictionaries using for loops



## Q. 50) Write a Python script to merge two Python dictionaries.(merging)
# a={1:21,2:34,3:234}
# b={4:32,5:654,6:23}
# a.update(b)
# print(a)


# a={1:21,2:34,3:234}
# b={3:32,5:654,6:23}
# a.update(b)
# print(a)


# a={1:21,2:34,3:234}
# b={3:32,5:654,6:23}
# for i in b.keys():
#     a[i]=b[i]
# print(a)


## Q.51) Write a Python program to sum all the values in a dictionary.

# a={1:21,2:34,3:234}
# sum=0
# for i in a.values():
#     sum=sum+i

# print(sum)



## Q.52) Convert a list to dictionary  and  53) count the frequency of each elements.
# dict={}
# a=[1,2,1,2,3,2,3,1,3,1,1,1,2,2,3,4,3,2,1,4,3,4]
# for i in a:
#       if i in dict.keys():
#             dict[i]=dict[i]+1
#       else :
#             dict[i]=1
# print(dict)


## Q.54) Write a Python program to combine two dictionary by adding values for common keys.

# a={1:21,2:34,3:234}
# b={3:32,5:654,6:23}
 
# for i in b.keys():
#       if i in a.keys():
#           a[i]=a[i]+b[i]
#       else:
#            a[i]=b[i]
# print(a)

## Q. rotation of list
# l=[1,2,3,4,5,6]
# n=int(input("enter how many times you want to rotate : "))
# for i in range(n):          
#       v=l[0]
#       for i in range(0,len(l)-1): 
#           l[i]=l[i+1]
#       l[len(l)-1]=v
# print(l)



# a=[1,2,3,4,5,6]
# n=int(input("enter how many times you want to rotate : "))
# l=n%len(a)
# for i in range(len(a)-l):
#      a[i],a[i+l]=a[i+l],a[i]
# print(a)



## EXCEPTION HANDLING

#TRY EXCEPT
# try:
#     print(10/0)
# except Exception as a:
#     print(f"bhai zero ke alawa kuch bhi de de warna {a} aa jayega!!!!!!!!!!!")


# TRY EXCEPT FINALLY
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("cannot divide bu zero")
# except Exception as e:
#     print(f"an error occured : {e}")
# finally:
#     print("this will be executed no matter what")


# TRY EXCEPT ELSE FINALLY
# try:
#     result = 10/2
# except ZeroDivisionError:
#     print("cannot divide bu zero")
# except Exception as e:
#     print(f"an error occured : {e}")
# else:
#     print("no exception occured")
# finally:
#     print("this will be executed no matter what")


# # # print("what do you want to do")
# # # print("press1 for creating a file")
# # # print("press2 for reading a file")
# # # print("press3 for updating a file")

# # # a=input("tell your input : ")
# # # if a=="1":
# # #     name = input("please tell your file name with extension")
# # #     file=open(name,'w')
# # #     file.write(input("tell your file name : "))
# # # elif a=="2":
# # #     name=input("tell your file name")
# # #     try:
# # #         file = open(name,"r")
# # #         print(file.read())
# # #     except Exception as e:
# # #         print("sorry your file does not exist")

# # # elif a == "3":
# # #     name = input("tell your file name")
# # #     try:
# # #         file=open(name,"a")
# # #         data = input("tell what you want to update  : ")
# # #         file.write(" " + data)

# # #     except Exception as e:
# # #         print("sorry your file does not exist")


# `def check(s1, s2):
    
#     if(sorted(s1)== sorted(s2)):
#         print("The strings are anagrams.")
#     else:
#         print("The strings aren't anagrams.")        
        
# s1 = input("Enter string1: ")
# # input1: "listen"
# s2 = input("Enter string2: ")
# # input2: "silent"
# check(s1, s2)`
# Output: the strings are anagrams.