# with open('file.txt','r') as file:
#     for line in file:
#         print(line.strip())

# list=['\nTridib','\nSrija','\nUnmesh','\nSayon']
# with open('file.txt','a') as file:
#     file.writelines(list)

with open('file.txt','w+')as file:
    file.write('Hello world\n')
    file.write('This is a new line \n')
    
    file.seek(2)
    content=file.read()
    print(content)
