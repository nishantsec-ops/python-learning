#variable
 
##container where data is stored
#eg: a,b
# in variable defines with without quotes

name = "nishant"
print(name)

print("hello",name)
##used comma for separating the string and variable and variable can be define in quotes

city = "delhi"
print(city)
    
print("hello",city)

##for numerical data directly define without quotes

c=45
print(c)


#rules for variable 
   #case sensitive

 #  a= 89
#print(a)

##print(A) thi will give error


# variables we can letters , numbers,  _ and &  
# variables can never start with number...
# variables should not be define keywords...
    # -eg a%b=78
    # total 35 reserved keywords in python
    #and, or, not, if, else, elif,
##for, while, break, continue, pass,


import keyword

print(keyword.kwlist)


name="Nishant"
course="certified pyhton programmer"

print("hello",name, "you are enrolled for",name,"course")


## f string 


print(f"hello{name},you are enrolled for {course} course...")


## for seprate

print("hello",name,sep="_")


 #manipulation of data

a="hii"
b = a
print(b)

a = "b"
b = "a"
c  = b

a = "a"
b = "b"

a,b=b,a

print (a)
print(b)



#indentation  , no spaces before the statement


#Data types in python
      #interger : -ve to +ve
      #float : decimal values
      #complex : real and imaginary values, 45 + 7i
       #iota defines with j in python
# to check the data type of variable we can use type() fun.....

# Boolean data type: True or False
# String data type : collelction of character defined in single or double quotes
# for multiple line string we can use triple quotes ''' or """" 
 

 #indexing


x = "nishant"

print(x[1])    
 # that can be in -ve and -ve


 #slicing



#x[start:end]

print(x[0:6])

#step in slicing

print(x[0:6:2])

#reverse 
name = "nishant"
print(name[5::-1])

#input()

name = input("")
print(f"hello{name}")

name = input("Enter your name:")
#print(name[5::-1])
#print(name[::-1])
print(name[-1::-1])
#print(f"hello{name}")



#...........Today topic covered
#varibles , keywords, datatypes , indexing , slicing , input(), f string, indentation


