
#There are two methods to write in a file.
#Method 1

f1 = open('File IO/data.txt' , 'w')  # 'w' represent 'write mode'.
f1.write('Hi, I am Taaha')
f1.close()   

#Method 2

with open('File IO/data.txt','w') as f2:
    f2.write('Assalamoalaikum')
# Method 2 doesn't requires file closing