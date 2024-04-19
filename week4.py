msg=str(input("enter your message:"))
count=0
for i in msg:
    if i== 'a'or i=='e' or i=='i' or i=='o' or i=='u':
        count +=1
        print(count)