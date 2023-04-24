
#There are two methods to append in a file.
#Method 1

f1 = open('File IO/data.txt' , 'a')  # 'a' represent 'write mode'.
f1.write('Hi, I am Taaha')
f1.close()   

#Method 2

with open('File IO/data.txt','a') as f2:
    f2.write(' \nI am appending this statement')
# Method 2 doesn't requires file closing

