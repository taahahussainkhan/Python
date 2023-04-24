
#There are two methods to read from a file.
#Method 1

f1 = open('File IO/data.txt' , 'r')  # 'r' represent 'read mode'.
s1=f1.read()
f1.close()   
print(s1)
#Method 2

with open('File IO/data.txt','r') as f2:
    s2=f2.read()
    print(s2)
# Method 2 doesn't requires file closing