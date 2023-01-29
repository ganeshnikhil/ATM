# atm for bank


print('''
[1]:check the balance of account
[2]:deposite money from account
[3]:delete account 
[4]:withdraw money from account
[5]:create new account
[6]:deposite money from one account to another''')
print('''
[1] check account
[2] deposite account
[3] delete account
[4] withdraw account
[5] create account
[6] transction account
''')
#enter which option you want to choose from 1 to 6
user=int(input('Enter your option:'))
# if user wants to check balance
if user==1:
    #enter you accouts unique id
    id_no=int(input('Enter your id:'))
    #opent the file atm.data add to list
    file=open('atm.dat','r').readlines()
    #iterate through file
    for data in file:
        #split data 
        find_id=data.split(':')
        #if id matches gives account_id
        if int(find_id[0])==id_no:
            #show all information of account
            print(f'id:{find_id[0]}')
            print(f'name:{find_id[1]}')
            print(f'money:{find_id[2]}')
            count=3
#if user want to deposite money ..         
elif user==2:
    #enter you uniqued id 
    id_no=int(input('Ente your id:'))
    #open the file atm.data add to list
    file=open('atm.dat','r').readlines()
    #iterate through list..
    for i in range(len(file)):
        #split data
        find_id=file[i].split(':')
        #check if id matches with give account_id
        if int(find_id[0])==id_no:
            #enter the amount you want to add
            amount=int(input('Enter the amount:'))
            #add the amount 
            total_amount=int(find_id[2])+amount
            #convert it to string and assign it to money
            find_id[2]=str(total_amount)
            #again join the data with colon..
            r=':'.join(find_id)
            file[i]=r+'\n'
            #open file in write mode
            f=open('atm.dat','w')
            #write all data stored in list
            for data in file:
                f.write(data)
            f.close()
            
 #similary all option function ....
elif user==3:
    id_no=int(input('Ente your id:'))
    file=open('atm.dat','r').readlines()
    f=open('atm.dat','w')
    for i in range(len(file)):
        find_id=file[i].split(':')
        if int(find_id[0])==id_no:
            pass
        else:
            f.write(file[i])

elif user==4:
    id_no=int(input('Ente your id:'))
    file=open('atm.dat','r').readlines()
    for i in range(len(file)):
        find_id=file[i].split(':')
        if int(find_id[0])==id_no:
            amount=int(input('Enter the amount:'))
            if amount>int(find_id[2]):
                print('Invalid amount')
            else:
                total_amount=int(find_id[2])-amount
                find_id[2]=str(total_amount)
                r=':'.join(find_id)+'\n'
                file[i]=r
            f=open('atm.dat','w')
            for data in file:
                f.write(data)
            f.close()
elif user==5:
    f=open('atm.dat','r').readlines()
    id=input('Enter id:')
    name=input('Enter your name:')
    amount=input('Enter intial amount:')
    for data in f:
        find_id=data.split(':')
        if id==find_id[0] or name==find_id[1].strip():
            print('Id already exist...')
            quit()
    #
    data= id+':'+name+':'+amount+'\n'
    file=open('atm.dat','a')
    file.write(data)
    file.close()
elif user==6:
    transaction=False
    file=open('atm.dat','r').readlines()
    tran_id=input('Enter the your id:')
    tran_name=input('Enter your name:')
    recv_id=input('Enter reciever id:')
    recv_name=input('Enter reciver name:')
    for i in range(len(file)):
        find_id=file[i].split(':')
        if tran_id==find_id[0]:
            amount=input('Enter the amount of transcation:')
            if int(amount)>int(find_id[2]):
                print('Invalid amount!')
                quit()
            else:
                money=int(find_id[2])-int(amount)
                file[i]=find_id[0]+':'+find_id[1]+':'+str(money)+'\n'
                for i in range(len(file)):
                    find_id=file[i].split(':')
                    if recv_id==find_id[0]:
                        transaction=True
                        d=int(find_id[2])+int(amount)
                        file[i]=find_id[0]+':'+find_id[1]+':'+str(d)+'\n'
                        break
                    #else:
                        #print('Invalid receving id..')
                        #quit()
                if transaction:
                    f=open('atm.dat','w')
                    for data in file:
                        f.write(data)
                    f.close()
                     