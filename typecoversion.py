#IMPLICIT TYPE CONVERSION 
#Python automatically converts a smaller data type to a larger data type to prevent data loss.
x = 10  # int
y = 2.5  # float
z = x + y
print(z, type(z))  # 12.5, <class 'float'>


#EXPLICIT TYPE CONVERSION 
#Manually converting data types using functions like int(), float(), str().
i="5" #STRING
y= (int)i #string to integer
print(y,type(y))  #5, <class 'int'>
