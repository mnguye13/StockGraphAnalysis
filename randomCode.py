#Minh Nguyen
#7/30/2018
#Final Project
#randomCode.py
#File for random-generated access code & PIN
import random

#Function to generate access code and PIN
#and save the codes as users.dat
def keyGenerator():
    a_code = random.sample(range(0,99999),20)
    pin = random.sample(range(1000,1020),20)

    keygen_dict = dict(zip(a_code, pin))
    print ("20 new keys generated")

    #print (keygen_dict)

    keygen_tuple = list(zip(a_code, pin))


    #print (keygen_tuple)

    file = open("users.dat", "a")

    for item in keygen_tuple:
        file.write("%s\n" % str(item))
    file.close()
    
#Function to retrive key
def retriveKey():
    file = open("users.dat", "r")
    contents = file.readlines()
    code = []
    pin = []
    key = []
    for i in contents:
        i = i.strip('\n')
        i = i.strip('(')
        i = i.strip(')')
        i = i.split(',')
        code.append(i[0])
        pin.append(i[1])
        key.append(i)

    #print (key)

    #print(random.choice(key))
    
    file.close()
    #return random.choice(key)
    return key

#keyGenerator()
#retriveKey()

    
