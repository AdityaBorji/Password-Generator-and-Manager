import string
import random
import time

def user_response():
    response_of_user=input('''Press 1: To create a new Password
Press 2: To retreive a password
Press 3: To just enjoy and explore the range of Passwords
Press q: To quit           
#  ''')
    
    if response_of_user==("q" or "Q"):
        print("Thankyou for using this Application.")
        exit()

    if response_of_user=="1":
        plen = int(input("Pls enter the length of Password: "))
        New_password(plen, 0)

    elif response_of_user=="2":
        retreival()
    
    elif response_of_user=="3":
        while True:
            plen1 =(input("Pls enter the length of Password:\nOR Press q to quit:\t "))
            if plen1=="Q" or plen1=="q":
                exit()
            if plen1.isdigit():
                plen=int(plen1)
                instant_password=(New_password(plen, 1))
                print(instant_password)
                check=input("\nPress Y to use this password:\nOR\nPress N to continue strolling: \n")
                if check=="y" or check=="Y":
                    Encoder(instant_password, 0)
                


    else:
        print("Invalid literal\nKindly choose and enter a number from 1, 2 and 3  or  press q to Quit")
        while (response_of_user!=("1" or "2" or "3" or "q" or "Q")):
            user_response()



def New_password(plen, indication):
    passw=""
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    random.shuffle(s)
    for i in range(plen):
        passw+=s[i]
    if indication==1:
        return passw

    print(f"Recommended {plen} letter Password is:\t{passw}")
    response=input("Do you wish to save the Password:\nPress Y for Yes\nPress N for No\n ")
    if response=="Y" or response=="y":
        Encoder(passw, 0)
    elif response=="n" or response=="N":
         exit()
    else:
        exit()

def if_present(password, task):
    sum=0
    with open("Passwords.txt", "r") as f:
        line=f.readlines()
        for i in range(len(line)):
            if task in line[i]:
                sum=1
                break
        if sum==1:
            m=input("The password for this keyword is already present.\nDo you wish to overwrite it\nPress Y for Yes\nPress n for No")
            if m=="N" or m=="n":
                exit()

            if m=="Y" or m=="y":
                with open("Passwords.txt", "r") as f:
                    length_of_pass=password
                    line=f.readlines()
                    print(line)
                    string1 = task + "    "+ length_of_pass+ "\n"
                    for i in range(len(line)):
                        if task in line[i]:
                            line[i] = string1
                print(line)
                with open("passwords.txt", "w") as f:
                    f.writelines(line)
                print("The password has been overwritten and saved")
                exit()
        elif sum==0:
            return 0


        # data=True
        # sum=0
        # line_number=0
        # while data:
        #     line_number+=1
        #     data=f.readline()
        #     if task in data:
        #         m=input("The password for this keyword is already present.\nDo you wish to overwrite it\nPress Y for Yes\nPress n for No")
        #         with open("Passwords.txt", "w") as f:
        #             for i in range(1,line_number+2):
        #                 f.writeline(data)
        #                 if i==line_number:
        #                     f.readline
                    

                # if m=="Y" or "y":
                #     length_of_pass=int(input("Pls enter the length of the new password which you want to replace the previous one with:"))
                #     data[line_number]=New_password(length_of_pass, 1) + "    "+ task
                #     with open("Passwords.txt", "w", encoding='utf-8') as f:
                #         f.write(data)
                    # break
        

        

def Encoder(password, carry):
            # if carry==0:
            #     Task=input("Where do you wish to use this password: ").lower()
            #     if_present(password,Task)
            
            

            blueprint=['C', '?', "'", '{', '8', '>', '|', 'Z', '9', '5', 'U', 'q', 'J', '~', 'b', 'A', '1', ';', 'u', '2', 'h', 'X', 's', '4', 'K', '0', '6', 'S', 'c', 'e', ')', 'm', 'i', '*', 'd', 'E', 'Y', '!', 'B', 'a', 'o', 'r', 'N', '''\\''', 't', '"', '[', '&', 'M', 'g', ':', 'f', 'k', 'z', '$', 'y', 'x', '7', ',', 'V', 'D', '(', '3', 'j', 'L', '@', 'W', '%', ']', 'T', 'R', '+', '`', '=', 'P', '<', 'H', '^', '}', '-', 'F', 'p', '.', 'w', 'G', 'v', 'I', 'O', 'l', 'Q', 'n', '_', '#', '/']
            list1=[]
            # new=[]
            list1.extend(password)
            
            for i in range(len(list1)):
                for j in range(len(blueprint)):
                    if blueprint[j]==list1[i]:
                        list1[i]=blueprint[(len(blueprint))-1-j]
                        break


            Encoded_Password=""
            for i in range(len(list1)):
                Encoded_Password+=list1[i]
            if carry==1:
                return Encoded_Password
            if carry==0:
                Task=input("Where do you wish to use this password: ").lower()
                if_present(Encoded_Password,Task)
    

            if carry==0:
                list_of_Pass_Task=""
                list_of_Pass_Task= Task +"    "+ Encoded_Password               # 4 spaces
                with open("Passwords.txt", "a") as f:
                        f.write(f'''{list_of_Pass_Task}\n''')
                print("Password and the Place have been saved.")
                exit()
    

def retreival():
     content=True
     number=0
     print("These are the options available:\n")
     with open("Passwords.txt", "r") as f:
         while content:
            content=f.readline()
            if content==False:
                break
            number+=1
            listx=[]
            listy=[]
            dummy=0
            stringx=""
            listx.extend(content)
    
            for i in range(len(listx)):
                if listx[i]==" " and listx[i+1]==" " and listx[i+2]==" " and listx[i+3]==" ":
                    n=i
                    listy=listx[0:n]
                    break
            for i in range(len(listy)):
                stringx+=listy[i]
            if stringx=="":
                break
            print(f"{number}. {stringx}")

     print("\nPls type the option for which password is to be retreived.")    
     to_retreive=input("\nWhich password Do you want to retreive: ").lower()
     data=True
     with open("Passwords.txt", "r") as f:
        sum=0
        while data:
            data=f.readline()
            if to_retreive in data:
                sum=1
                break
            else:
                sum=0
        if sum==0:
            print("Password for this particular keyword not available")
            exit()
        retreived=data.replace((to_retreive + "    "), "")
        print(retreived)
        print(f"The password for {to_retreive} is {Encoder(retreived, 1)}")
        


user_response()

        
    
