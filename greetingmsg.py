placeholder='[name]'
with open('guestlist','r') as name_list:
    names=name_list.readlines()

    #print(names)

with open ('message.txt','r') as guest_msg:
    msg=guest_msg.read()
    for name in names:
        stripname=name.strip('\n')
        nam=msg.replace(placeholder,stripname)

        with open(stripname,'w')as file:
            file.write(nam)
        #print(nam)






