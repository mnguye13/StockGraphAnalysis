#Minh Nguyen
#7/30/2018
#Final Project
#pytest.py
#Main file for data analysis and graphing

#Import necessary module
import json,requests

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import statistics
import hashlib, uuid
import json as simplejson
import random
import randomCode
import os
import AccountStorage
import csv


class StockApp(object):
    #Function to initialize app
    def __init__(self, parent):
        
        """Constructor"""
        self.root = parent
        self.root.title("Stock Analysis v1 ")

        
        self.frame = Frame(parent)
        self.frame.pack()
 
        btn = Button(self.frame, text="Login with existing account", command=self.buildLogin)
        btn2 = Button(self.frame,text=" Create new account  ", command = self.createAccount)
        btn3 = Button(self.frame,text=" Exit Program  ", command = self.exitApp)
        btn.pack()
        btn2.pack()
        btn3.pack()
        if os.path.exists("users.dat") is False:
            randomCode.keyGenerator()
        if os.path.exists("Accounts.db") is False:
            AccountStorage.createTable()
            
        
    #Function to hide frame
    def hide(self):
        """"""
        self.root.withdraw()

    #Function to build login frame
    def buildLogin(self):
        global username, password, PIN, code
        self.hide()
        master = Tk()

        #modify root window
        master.title("Stock Analysis Login")
        master.geometry("300x300")

        frame1 = Frame(master)
        frame1.pack()


        Label(frame1, text="Username:").grid(row=0, column=0, sticky=W)
        username = StringVar(master)
        user = Entry(frame1, textvariable=username)
        user.grid(row=0, column=1, sticky=W)

        Label(frame1, text="Password:").grid(row=1, column=0, sticky=W)
        password = StringVar(master)
        pas = Entry(frame1, textvariable=password)
        pas.grid(row=1, column=1, sticky=W)
        pas.config(show="*")

        Label(frame1, text="PIN:").grid(row=2, column=0, sticky=W)
        PIN = StringVar(master)
        pin = Entry(frame1, textvariable=PIN)
        pin.grid(row=2, column=1, sticky=W)
        pin.config(show="*")

        frame1 = Frame(master)       # add a row of buttons
        frame1.pack()

        btn1 = Button(frame1,text=" OK  ", command = self.verifyLogin)
        btn2 = Button(frame1,text=" Create new account  ", command = self.createAccount)

        btn1.pack(side=LEFT);
        btn2.pack(side=LEFT);

        frame1 = Frame(master)       # add a row of buttons
        frame1.pack()
        btn3 = Button(frame1,text=" Back ",command = lambda: self.goBack(master))
        btn4 = Button(frame1,text=" Exit ",command = self.exitApp)
        

        btn3.pack(side=LEFT);
        btn4.pack(side=LEFT);

        
        
        
        #btn3.pack(side=BOTTOM);
        

        return master
    #Function to verify login credentials
    def verifyLogin(self):
        global store_account, store_code
        global store_id, store_uname, store_pass,store_fname,store_lname, store_acode, store_pin
        store_id = []
        load_account = []
        store_account = []
        #store_uname = ''
        #store_fname = ''
        #store_lname = ''
        #store_hpass = ''
        store_code = ''
        #store_pin =''
        valid = False

        temp_PIN = '  '+PIN.get()
        hash_get_password = ' '+(hashlib.md5(password.get().encode())).hexdigest()

        new_temp_PIN = ' '+PIN.get()
        new_hash_get_password = (hashlib.md5(password.get().encode())).hexdigest()
        
        
        print ("verifying...")
        ####
        #print (AccountStorage.load_account())
        loadAccount = AccountStorage.load_account()
        for i in loadAccount:
            store_id = i[0]
            if (username.get() == i[1]  and new_hash_get_password == i[2] and new_temp_PIN == i[6]) :
                store_code = ' '+i[5]
                print("Accpeted")
                valid = True
                messagebox.showinfo("Success","Login Success! \nWelcome %s "%username.get())
                self.buildFrame()
        if username.get() == 'admin' and password.get() == 'admin' and PIN.get() == '0000':
            print("Accpeted")
            valid = True
            messagebox.showinfo("Success","Login Success!\nWelcome %s "%username.get())
            store_code = ' 0000'
            self.buildFrame()
            
            


        ####
        '''
        #print (PIN.get())
        if os.path.exists("userAccount.txt"):
            #valid = False
            f = open('userAccount.txt','r')
            contents = f.readlines()
            for i in contents:
                i = i.strip('\n')
                i = i.strip('[')
                i = i.strip(']')
                i = i.strip('"')
                i= ''.join(i for i in i if i not in '"')
                i = i.split(',')
                #print (i)
                store_account.append(i)
            if username.get() == 'admin' and password.get() == 'admin' and PIN.get() == '0000':
                print("Accpeted")
                valid = True
                messagebox.showinfo("Success","Login Success!")
                store_code = ' 0000'
                self.buildFrame()
                
            for i in range(len(store_account)):
                #print (username.get(),'----',store_account[i][0],'and',hash_get_password,'---',store_account[i][1],'and',temp_PIN,'---',store_account[i][5])
                if (username.get() == store_account[i][0] and hash_get_password == store_account[i][1] and temp_PIN == store_account[i][5]):
                    store_code = store_account[i][4]
                    print("Accpeted")
                    valid = True
                    messagebox.showinfo("Success","Login Success!")
                    self.buildFrame()
        else:
            print("Fail to load users data")'''
        ###

        if valid is not True:
            print("Denied")
            messagebox.showwarning("Denied","Incorrect Credentials!")

        #print (store_account)
        #print (store_code)
            






        
        
    #Function to buid registration frame   
    def createAccount(self):
        global user_new, pass_new, pass2_new, f_name, l_name
        master = Toplevel()

        #modify root window
        master.title("Stock Analysis Account Registration")
        master.geometry("300x300")

        frame1 = Frame(master)
        frame1.pack()


        Label(frame1, text="Username:").grid(row=0, column=0, sticky=W)
        user_new = StringVar(master)
        user = Entry(frame1, textvariable=user_new)
        user.grid(row=0, column=1, sticky=W)

        Label(frame1, text="Password:").grid(row=1, column=0, sticky=W)
        pass_new = StringVar(master)
        pas = Entry(frame1, textvariable=pass_new)
        pas.grid(row=1, column=1, sticky=W)
        pas.config(show="*")

        Label(frame1, text="Confirmed Password:").grid(row=2, column=0, sticky=W)
        pass2_new = StringVar(master)
        pas2 = Entry(frame1, textvariable=pass2_new)
        pas2.grid(row=2, column=1, sticky=W)
        pas2.config(show="*")

        Label(frame1, text="First Name").grid(row=3, column=0, sticky=W)
        f_name = StringVar(master)
        first = Entry(frame1, textvariable=f_name)
        first.grid(row=3, column=1, sticky=W)

        Label(frame1, text="Last Name").grid(row=4, column=0, sticky=W)
        l_name = StringVar(master)
        last = Entry(frame1, textvariable=l_name)
        last.grid(row=4, column=1, sticky=W)

        
        

        frame1 = Frame(master)       # add a row of buttons
        frame1.pack()

        btn1 = Button(frame1,text=" OK  ", command = lambda: self.storeAccount(master))
        btn2 = Button(frame1,text=" Back ",command = lambda: self.goBack(master))
        
        btn1.pack(side=LEFT); btn2.pack(side=LEFT)

        return master

    #Function to create and store new credentials to database
    def storeAccount(self, otherFrame):
        global userNum
        checkNum = 0
        existAccount = []
        exist = False
        userNum = 0


        new_existAccount = AccountStorage.load_account()

        userNum = len(new_existAccount)

        for i in new_existAccount:
            if(user_new.get() == i[1]):
                exist = True
        checkNum = userNum
        if checkNum >= 20:
            checkNum = 0
            randomCode.keyGenerator()
            
        '''   
        if os.path.exists("userAccount.txt"):
            f = open('userAccount.txt','r')
            contents = f.readlines()
            for i in contents:
                i = i.strip('\n')
                i = i.strip('[')
                i = i.strip(']')
                i = i.strip('"')
                i= ''.join(i for i in i if i not in '"')
                i = i.split(',')
                #i = i.strip('"')
                #print(i)
                existAccount.append(i)
                userNum += 1
                checkNum +=1
            print (checkNum)
            if(checkNum >= 20):
                checkNum = 0
                randomCode.keyGenerator()
            #print (existAccount[0][1])
        else:
            userNum = 0

        for i in range(len(existAccount)):
            if(user_new.get() == existAccount[i][0]):
                      exist = True'''
        if exist is True:
            messagebox.showwarning("Username Unavailable","Try different username!")
            user_new.set('')
            pass_new.set('')
            pass2_new.set('')
            f_name.set('')
            l_name.set('')
        else:
            print (userNum)
        
            #if os.stat("userAccount.txt").st_size == 0:
                #userNum = 0
            
            temp_key = randomCode.retriveKey()
            #print(temp_key[userNum])
            temp_account = []
            temp_a_code = temp_key[userNum][0]
            temp_pin = temp_key[userNum][1]
            if not user_new.get() or not pass_new.get() or not pass2_new.get() or not f_name.get() or not l_name.get():
                 messagebox.showwarning("Missing field(s)","1 or more fields is/are missing!")
            else:
                if pass_new.get() == pass2_new.get():
                    #print (user_new.get(),pass_new.get(),pass2_new.get(),f_name.get(),l_name.get())
                    hashed_password = hashlib.md5(pass_new.get().encode())
                    #print (hashed_password.hexdigest())
                    AccountStorage.insert_account(user_new.get(),hashed_password.hexdigest(),f_name.get(),l_name.get(),temp_a_code,temp_pin)
                    #temp_account.extend((user_new.get(),hashed_password.hexdigest(),f_name.get(),l_name.get(),temp_a_code,temp_pin))
                    userNum += 1
                    messagebox.showinfo("Access Code","Your PIN is: %s \nYour access code is: %s"%(temp_pin,temp_a_code))
                    otherFrame.destroy()
                else:
                    messagebox.showwarning("Password Unmatched","Confirm password again!")
            #print (userNum)

            #print (temp_account[4])
            ###
    
            ###
            
            ####
            '''

            file = open('userAccount.txt','a')
            simplejson.dump(temp_account, file)
            file.write("\n")
            file.close()'''

            #f = open('users.dat','w')
            #simplejson.dump(keygen_dict, f)
            #f.close()
    #Function to go back frame
    def goBack(self, otherFrame):
        self.show()
        otherFrame.destroy()

    #Function to show frame
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()
    #Function to exit app
    def exitApp(self):
        if (messagebox.askokcancel(title='Exit', \
    	    message="Do you want to exit?") == 1) :
              os._exit(1)
    #Function to open image files
    def OpenFile(self):
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                          filetypes=(("png files", "*.png"), ("all files", "*.*")))
    #Function to view app description 
    def About(self):
        print("Stock analysis program v1 \nDeveloped by Minh Nguyen in 2018")
        messagebox.showinfo("About","Stock Analysis v1 \nDeveloped by Minh Nguyen")
    
    #Function to build analysis frame
    def buildFrame(self):
        global dayVar, monthVar, yearVar,c_date,CODE
        global dates, prices, date_price, YEAR, MONTH
        global whole_date,whole_date_2016,whole_date_2017,whole_date_2018,whole_date
        global whole_price,price_2016,price_2017,price_2018
        global month_2016, month_2017, month_2018
        global day_2016, day_2017, day_2018
        global month_date_2016 ,month_date_2017 ,month_date_2018
        



        
        dates=[]
        prices=[]
        date_price = {}

        whole_date = []
        whole_date_2016 = []
        whole_date_2017 = []
        whole_date_2018 = []

        month_2016 = []
        month_2017 = []
        month_2018 = []
        
        day_2016 = []
        day_2017 = []
        day_2018 = []

        month_date_2016 = []
        month_date_2017 = []
        month_date_2018 = []

        whole_price = []
        price_2016 = []
        price_2017 = []
        price_2018 = []
        #create the window
        root = Tk()
        
        #modify root window
        root.title("Stock Analysis")
        root.geometry("300x300")
        ###

        # Insert a menu on the main window
        menu = Menu(root)
        root.config(menu=menu)# display menu
        # Create a menu button labeled "File" that brings up a menu
        filemenu = Menu(menu)
        # allow submenu items
        menu.add_cascade(label="File", menu=filemenu)
        # Create entries in the "File" menu
        filemenu.add_command(label="Open Image", command=self.OpenFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exitApp)

        # Create a menu button labeled "Help" that brings up a menu
        helpmenu = Menu(menu)
        # allow submenu items
        menu.add_cascade(label="Help", menu=helpmenu)

        # Create entries in the "Help" menu
        helpmenu.add_command(label="About", command=self.About)
        ###

        dayVar = StringVar()
        monthVar = StringVar()
        yearVar = StringVar()

        frame1 = Frame(root)
        frame1.pack()


        Label(frame1, text="Day:").grid(row=0, column=0, sticky=W)
        dayVar = StringVar(root)
        day = Entry(frame1, textvariable=dayVar)
        day.grid(row=0, column=1, sticky=W)

        Label(frame1, text="Month:").grid(row=1, column=0, sticky=W)
        monthVar = StringVar(root)
        month = Entry(frame1, textvariable=monthVar)
        month.grid(row=1, column=1, sticky=W)

        Label(frame1, text="Year:").grid(row=2, column=0, sticky=W)
        yearVar = StringVar(root)
        year= Entry(frame1, textvariable=yearVar)
        year.grid(row=2, column=1, sticky=W)

        Label(frame1, text="Access Code:").grid(row=3, column=0, sticky=W)
        CODE = StringVar(root)
        #CODE.set(store_code)
        code= Entry(frame1, textvariable=CODE)
        code.grid(row=3, column=1, sticky=W)
        code.config(show="*")

        dayVar.set('##')
        monthVar.set('##')
        yearVar.set('##')



        



        frame1 = Frame(root)       # add a row of buttons
        frame1.pack()
        b_frame = Frame(root)
        b_frame.pack( side = BOTTOM )
        
       
        btn1 = Button(frame1,text=" Predict", command = self.predict)
        btn2 = Button(frame1,text=" Histogram  ", command = self.graphHistogram)
        #btn3 = Button(frame1,text=" Line", command = self.graphLine)
       
        
        btn1.pack(side=LEFT); btn2.pack(side=LEFT)
        #btn3.pack(side=LEFT); 

        frame1 = Frame(root)       # add a row of buttons
        frame1.pack()

        YEAR = StringVar(root)

        Radiobutton(frame1, text='2016', variable = YEAR, value = '2016').pack(side = LEFT)
        Radiobutton(frame1, text='2017', variable = YEAR, value = '2017').pack(side = LEFT)
        Radiobutton(frame1, text='2018', variable = YEAR, value = '2018').pack(side = LEFT)
        Radiobutton(frame1, text='All', variable = YEAR, value = 'all').pack(side = LEFT)

        YEAR.set(None)


        frame1 = Frame(root)       # add a row of buttons
        frame1.pack()

        MONTH = StringVar(root) 
        
        Radiobutton(frame1, text='Jan', variable = MONTH, value = 'JAN').pack(side = LEFT)
        Radiobutton(frame1, text='Feb', variable = MONTH, value = 'FEB').pack(side = LEFT)
        Radiobutton(frame1, text='Mar', variable = MONTH, value = 'MAR').pack(side = LEFT)
        Radiobutton(frame1, text='Apr', variable = MONTH, value = 'APR').pack(side = LEFT)
        Radiobutton(frame1, text='May', variable = MONTH, value = 'MAY').pack(side = LEFT)
        Radiobutton(frame1, text='Jun', variable = MONTH, value = 'JUN').pack(side = LEFT)
        
        frame1 = Frame(root)       # add a row of buttons
        frame1.pack()
        
        Radiobutton(frame1, text='Jul', variable = MONTH, value = 'JUL').pack(side = LEFT)
        Radiobutton(frame1, text='Aug', variable = MONTH, value = 'AUG').pack(side = LEFT)
        Radiobutton(frame1, text='Sep', variable = MONTH, value = 'SEP').pack(side = LEFT)
        Radiobutton(frame1, text='Oct', variable = MONTH, value = 'OCT').pack(side = LEFT)
        Radiobutton(frame1, text='Nov', variable = MONTH, value = 'NOV').pack(side = LEFT)
        Radiobutton(frame1, text='Dec', variable = MONTH, value = 'DEC').pack(side = LEFT)

        MONTH.set(None)

        frame1 = Frame(root)       # add a row of buttons
        frame1.pack()

        Radiobutton(frame1, text='All', variable = MONTH, value = 'ALL').pack(side = LEFT)

        




        
        frame1 = Frame(root)       # add a row of buttons
        frame1.pack()

        btn4 = Button(frame1,text=" OK  ", command = self.submitOK)
        btn5 = Button(frame1,text=" Exit ", command = self.exitApp)
        btn4.pack(side=LEFT)
        btn5.pack(side=LEFT)


        self.dataScraping()

        return root

        




       


        #kick off the event loop
        #root.mainloop();
    #Function supports predict button and trigger analysis function
    def predict(self):
        temp_code = ' '+CODE.get()
        if (temp_code == store_code):
            self.dataGraph(dates,prices)
        else:
            messagebox.showwarning("Invalid Code","Enter valid access code!")
        
    #Function supports OK button and trigger graphs function
    def submitOK(self):
        print (YEAR.get())
        if YEAR.get() == '2016':
            self.graph2016(date_price,price_2016,month_date_2016)
        elif YEAR.get() == '2017':
            self.graph2017(date_price,price_2017,month_date_2017)
        elif YEAR.get() == '2018':
            self.graph2018(date_price,price_2018,month_date_2018)
        elif YEAR.get() == 'all':
            self.graphAll(whole_date,whole_price)
            
        
            
        print ("Submit")
        
            
        
        """
        ###
        #get data
        rsp = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=aapl&apikey=AJXWVVW0CXFUR23F')

        data = rsp.json() #create data dict.

        #store data into lists for observation
        dates=[]
        prices=[]

        for k,v in data["Weekly Time Series"].items():
            #split data into tokens
            tokens = int(k.split('-')[0])
            if tokens >2015:
                '''
                split data by date 
                idx 0  => yyyy
                idx 1  => mm
                idx 2  => dd
                '''
                dates.append(int(k.split('-')[0]))
                prices.append(float(v['1. open']))

        print ("Dates:",dates)
        print ("Prices:",prices)

        #Convert to 1d Vector for later plottings
        dates = np.reshape(dates, (len(dates), 1))
        prices = np.reshape(prices, (len(prices), 1))



        # Define Linear Regressor Object
        regressor = LinearRegression()
        regressor.fit(dates, prices)

        print(len(dates))
        #Predict Price on Given Date (y, m or d)
        date = c_date
        predicted_price =regressor.predict(date)
        #display summary stats
        print("Predicted price",predicted_price[0][0])
        print("Confidence ( % ) of data fit", regressor.score(dates,prices))


        #set simple names for graphing

        x=dates
        y=prices
        # Visualize Results
        plt.scatter(x, prices, color='#0343df', label='Actual Price')  # plotting the initial datapoints
        plt.plot(x, regressor.predict(x), color='red', linewidth=3,
             label='Predicted Price')  # plotting the line made by linear regression
        plt.title(' Price over Time')
        plt.legend()
        plt.xlabel('Date Spread')
        plt.show()"""
        


    #Function to scrap data
    def dataScraping(self):
        ###
        try:
            
            
           
            #get data
            rsp = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=aapl&apikey=AJXWVVW0CXFUR23F')

            data = rsp.json() #create data dict.

            #store data into lists for observation

            for k,v in data["Weekly Time Series"].items():
                #split data into tokens
                tokens = int(k.split('-')[0])
                '''
                if 2015 < tokens < 2017:
                    whole_date_2016.append(k)
                    price_2016.append(float(v['1. open']))
                if 2016 < tokens < 2018:
                    whole_date_2017.append(k)
                    price_2017.append(float(v['1. open']))
                if 2017 < tokens:
                    whole_date_2018.append(k)
                    price_2018.append(float(v['1. open']))'''
                if tokens >2015:
                    '''
                    split data by date 
                    idx 0  => yyyy
                    idx 1  => mm
                    idx 2  => dd
                    '''
                    
                    #whole_date.append(k)
                    #whole_price.append(float(v['1. open']))
                    dates.append(int(k.split('-')[0]))
                    prices.append(float(v['1. open']))
                    date_price.update({k:float(v['1. open'])})

                    
            


            for k,v in sorted(date_price.items()):
                if(int(k.split('-')[0]) == 2016):
                    month_date_2016.append(k.split('-')[1] + '.' + k.split('-')[2])
                    price_2016.append(v)
                if(int(k.split('-')[0]) == 2017):
                    month_date_2017.append(k.split('-')[1] + '.' + k.split('-')[2])
                    price_2017.append(v)
                if(int(k.split('-')[0]) == 2018):
                    month_date_2018.append(k.split('-')[1] + '.' + k.split('-')[2])
                    price_2018.append(v)
                if(int(k.split('-')[0]) > 2015):
                    whole_date.append(k)
                    whole_price.append(v)
                
            
            #print (dates)
            #print (sorted(date_price))

            #print (date_price.values())
            #print (date_price.keys())

            #for w in sorted(date_price, key=date_price.get, reverse=True):
                #print (w, date_price[w])

            #print (dates)
            ###

            '''
            x1=whole_date_2016
            y1=price_2016

            plt.plot(x1, y1)
            plt.scatter(x1, y1, color='#ff0000', label='Actual Price')  # plotting the initial datapoints
            plt.xlabel('Year')
            plt.ylabel('Prices')
            plt.title('Prices over time in 2016')
            plt.grid(True)
            plt.show()
        

            x2=whole_date_2017
            y2=price_2017

            plt.plot(x2, y2)
            plt.scatter(x2, y2, color='#ff0000', label='Actual Price')  # plotting the initial datapoints
            plt.xlabel('Year')
            plt.ylabel('Prices')
            plt.title('Prices over time in 2017')
            plt.grid(True)
            plt.show()
            '''
            ###
            self.dataAnalysis(dates,prices,date_price)
        except:
            print ("Connection fail! Fail to retrive data")
            messagebox.showerror("Connection Error","Fail to retrive data")
        try:
           with open('prices_data_2016-2018.csv', 'w') as csv_file:
               writer = csv.writer(csv_file)
               for key, value in date_price.items():
                   writer.writerow([key, value])
        except:
            print ("Write fail! Fail to save csv data")
        
    ##Function to analysis data
    def dataAnalysis(self,dates,prices,date_price):

        
        max_k = max(date_price, key=date_price.get)
        min_k = min(date_price, key=date_price.get)
        print("Median of data points: ",np.median(prices))
        print("Mean of data points: ",np.mean(prices))
        print("Highest open value: ",max(prices),"on",max_k)
        print("Lowest open value: ",min(prices),"on",min_k)

        messagebox.showinfo("Data Analysis (Opening Prices)","Median of data points: %s\nMean of data points: %s\nHighest open value: %s on %s\nLowest open value: %s on %s"%(np.median(prices),np.mean(prices),max(prices),max_k,min(prices),min_k))

        
        
    #Function to graph 2016 data
    def graph2016(self,date_price,price_2016,month_date2016):
        #x=whole_date_2016
        try:
        
            x=month_date_2016
            y=price_2016
            month = ''
            
            #new_date_price = sorted(date_price)
            if MONTH.get()=='ALL':
                x = month_date_2016
                y = price_2016
                plt.title('Prices over time in 2016')
            else:
                if MONTH.get()=='JAN':
                    self.checkMonth(date_price,'6','0','1')
                if MONTH.get()=='FEB':
                    self.checkMonth(date_price,'6','0','2')
                if MONTH.get()=='MAR':
                    self.checkMonth(date_price,'6','0','3')
                if MONTH.get()=='APR':
                    self.checkMonth(date_price,'6','0','4') 
                if MONTH.get()=='MAY':
                    self.checkMonth(date_price,'6','0','5')
                if MONTH.get()=='JUN':
                    self.checkMonth(date_price,'6','0','6')
                if MONTH.get()=='JUL':
                    self.checkMonth(date_price,'6','0','7')
                if MONTH.get()=='AUG':
                    self.checkMonth(date_price,'6','0','8')
                if MONTH.get()=='SEP':
                    self.checkMonth(date_price,'6','0','9')
                if MONTH.get()=='OCT':
                    self.checkMonth(date_price,'6','1','0')
                if MONTH.get()=='NOV':
                    self.checkMonth(date_price,'6','1','1')
                if MONTH.get()=='DEC':
                    self.checkMonth(date_price,'6','1','2')
                ###
                x1 = month_date
                y1 = month_price

                x2 = month_date_2016
                y2 = price_2016

                plt.subplot(2,1,1)
                plt.plot(x1, y1)
                plt.title('Prices over time in %s, 2016'%MONTH.get())
                plt.xlabel('Date')
                plt.ylabel('Prices')
                plt.scatter(x1, y1, color='#ff0000', label='Actual Price')
                plt.grid(True)
                plt.legend()
                plt.subplots_adjust(bottom=0.15, hspace = 0.5)

                plt.subplot(2,1,2)
                plt.plot(x2, y2)
                plt.title('Prices over time in 2016')
                plt.xlabel('Date')
                plt.ylabel('Prices')
                plt.scatter(x2, y2, color='#ff0000', label='Actual Price')
                plt.grid(True)
                plt.xticks(x2,rotation='vertical', fontsize = 8)
                plt.legend()
                        

                plt.show()
                
            ###
            
            
          


            
            x_range = len(x)
            plt.plot(x, y)
            plt.scatter(x, y, color='#ff0000', label='Actual Price')  # plotting the initial datapoints
            plt.xlabel('Date')
            plt.ylabel('Prices')
            plt.grid(True)
            plt.xticks(np.arange(0,x_range, step = 1),x,rotation='vertical', fontsize = 8)
            plt.legend()
            plt.savefig('./img/2016.png')
            plt.show()
        except:
            messagebox.showwarning("Invalid","Please choose a year and a specific month or all")
        
    #Function to split month
    def checkMonth(self,date_price,y,m1,m2):
        global month_date, month_price
        month_date = []
        month_price = []
        for k,v in sorted(date_price.items()):
                #print (k[3])
                if(k[3] == y and k[5] == m1 and k[6] == m2):
                    month_date.append(k.split('-')[1] + '.' + k.split('-')[2])
                    month_price.append(v)
        
    #Function to graph 2017 data
    def graph2017(self,date_price,price_2017,month_date_2017):
        #x=whole_date_2017
        x=month_date_2017
        y=price_2017
        month =''
        try:
            if (MONTH.get()=='ALL') :
                x = month_date_2017
                y = price_2017
                plt.title('Prices over time in 2017')
            else:
                if MONTH.get()=='JAN':
                    self.checkMonth(date_price,'7','0','1')
                if MONTH.get()=='FEB':
                    self.checkMonth(date_price,'7','0','2')
                if MONTH.get()=='MAR':
                    self.checkMonth(date_price,'7','0','3')
                if MONTH.get()=='APR':
                    self.checkMonth(date_price,'7','0','4')
                if MONTH.get()=='MAY':
                    self.checkMonth(date_price,'7','0','5')
                if MONTH.get()=='JUN':
                    self.checkMonth(date_price,'7','0','6')
                if MONTH.get()=='JUL':
                    self.checkMonth(date_price,'7','0','7')
                if MONTH.get()=='AUG':
                    self.checkMonth(date_price,'7','0','8')
                if MONTH.get()=='SEP':
                    self.checkMonth(date_price,'7','0','9')
                if MONTH.get()=='OCT':
                    self.checkMonth(date_price,'7','1','0')
                if MONTH.get()=='NOV':
                    self.checkMonth(date_price,'7','1','1')
                if MONTH.get()=='DEC':
                    self.checkMonth(date_price,'7','1','2')
                ###
                x1 = month_date
                y1 = month_price

                x2 = month_date_2017
                y2 = price_2017

                plt.subplot(2,1,1)
                plt.plot(x1, y1)
                plt.title('Prices over time in %s, 2017'%MONTH.get())
                plt.xlabel('Date')
                plt.ylabel('Prices')
                plt.scatter(x1, y1, color='#ff0000', label='Actual Price')
                plt.grid(True)
                plt.legend()
                plt.subplots_adjust(bottom=0.15, hspace = 0.5)

                plt.subplot(2,1,2)
                plt.plot(x2, y2)
                plt.title('Prices over time in 2017')
                plt.xlabel('Date')
                plt.ylabel('Prices')
                plt.scatter(x2, y2, color='#ff0000', label='Actual Price')
                plt.grid(True)
                plt.xticks(x2,rotation='vertical', fontsize = 8)
                plt.legend()
                        

                plt.show()
                
            ###
            
            x_range = len(x)

            plt.plot(x, y)
            plt.scatter(x, y, color='#ff0000', label='Actual Price')  # plotting the initial datapoints
            plt.xlabel('Date')
            plt.ylabel('Prices')
            plt.grid(True)
            plt.xticks(np.arange(0,x_range, step = 1),x,rotation='vertical', fontsize = 8)
            plt.legend()
            plt.savefig('./img/2017.png')
            plt.show()
        except:
            messagebox.showwarning("Invalid","Please choose a year and a specific month or all")
            
    #Function to graph 2018 data
    def graph2018(self,date_price,price_2018,month_date_2018):
        #x=whole_date_2018
        x=month_date_2018
        y=price_2018
        month =''
        try:
            if MONTH.get()=='ALL':
                x = month_date_2018
                y = price_2018
                plt.title('Prices over time in 2018')
            else:

                if MONTH.get()=='JAN':
                    self.checkMonth(date_price,'8','0','1')
                if MONTH.get()=='FEB':
                    self.checkMonth(date_price,'8','0','2')
                if MONTH.get()=='MAR':
                    self.checkMonth(date_price,'8','0','3')
                if MONTH.get()=='APR':
                    self.checkMonth(date_price,'8','0','4')
                if MONTH.get()=='MAY':
                    self.checkMonth(date_price,'8','0','5')
                if MONTH.get()=='JUN':
                    self.checkMonth(date_price,'8','0','6')
                if MONTH.get()=='JUL':
                    self.checkMonth(date_price,'8','0','7')
                if MONTH.get()=='AUG':
                    self.checkMonth(date_price,'8','0','8')
                if MONTH.get()=='SEP':
                    self.checkMonth(date_price,'8','0','9')
                if MONTH.get()=='OCT':
                    self.checkMonth(date_price,'8','1','0')
                if MONTH.get()=='NOV':
                    self.checkMonth(date_price,'8','1','1')
                if MONTH.get()=='DEC':
                    self.checkMonth(date_price,'8','1','2')
            ###
                x1 = month_date
                y1 = month_price

                x2 = month_date_2018
                y2 = price_2018

                plt.subplot(2,1,1)
                plt.plot(x1, y1)
                plt.title('Prices over time in %s, 2018'%MONTH.get())
                plt.xlabel('Date')
                plt.ylabel('Prices')
                plt.scatter(x1, y1, color='#ff0000', label='Actual Price')
                plt.grid(True)
                plt.legend()
                plt.subplots_adjust(bottom=0.15, hspace = 0.5)

                plt.subplot(2,1,2)
                plt.plot(x2, y2)
                plt.title('Prices over time in 2018')
                plt.xlabel('Date')
                plt.ylabel('Prices')
                plt.scatter(x2, y2, color='#ff0000', label='Actual Price')
                plt.grid(True)
                plt.xticks(x2,rotation='vertical', fontsize = 8)
                plt.legend()
                        

                plt.show()
                
            ###
            
            x_range = len(x)

            plt.plot(x, y)
            plt.scatter(x, y, color='#ff0000', label='Actual Price')  # plotting the initial datapoints
            plt.xlabel('Date')
            plt.ylabel('Prices')
            plt.grid(True)
            plt.savefig('./img/2018.png')
            plt.xticks(np.arange(0,x_range, step = 1),x,rotation='vertical', fontsize = 8)
            plt.subplots_adjust(bottom=0.15, hspace = 0.5)
            plt.legend()
            plt.show()
        except:
            messagebox.showwarning("Invalid","Please choose a year and a specific month or all")
            
        
    #Function to graph all 3 years data
    def graphAll(self,whole_date,whole_price):
        x=sorted(whole_date)
        y=whole_price
        
        x_range = len(x)

        plt.plot(x, y)
        plt.scatter(x, y, color='#ff0000', label='Actual Price')  # plotting the initial datapoints
        plt.xlabel('Dates')
        plt.ylabel('Prices')
        plt.title('Prices over time in 2016-2018')
        plt.grid(True)
        plt.xticks(np.arange(0,x_range, step = 1),x,rotation='vertical', fontsize = 5)
        plt.legend()
        plt.savefig('./img/2016-2018.png')
        plt.show()
        
        
    #Function to predict data
    def dataGraph(self,dates,prices):
        try:
            print ("Graph")
            c_date = int(yearVar.get()) + int(monthVar.get())*0.07692307+ int(dayVar.get())*0.002564102
            print ("Data point: ",c_date)
            #Convert to 1d Vector for later plottings
            new_dates = np.reshape(dates, (len(dates), 1))
            new_prices = np.reshape(prices, (len(prices), 1))


            



            # Define Linear Regressor Object
            regressor = LinearRegression()
            regressor.fit(new_dates, new_prices)

            #print(len(dates))
            #Predict Price on Given Date (y, m or d)
            date = c_date
            predicted_price =regressor.predict(date)
            #display summary stats
            print("Predicted price",predicted_price[0][0])
            print("Confidence ( % ) of data fit", regressor.score(new_dates,new_prices))
            #
            compareDate = yearVar.get()+'-'+monthVar.get()+'-'+dayVar.get()
            real_price = '...'
            error = '...'
            for k,v in date_price.items():
                if k == compareDate:
                    real_price = v
                    error = ((predicted_price[0][0]-v)*100)/(v)
                    print ("Real price on %s is %s"%(k,v))
                    print ("Error ( % ) of data is ",(error))

                
            #
            messagebox.showinfo("Result","On date: %s \n-------------\nPredicted price: %s \nConfidence (%%) of data fit: %s \nReal Price: %s \nError (%%) of data is: %s"%(compareDate,predicted_price[0][0],regressor.score(new_dates,new_prices),real_price,error))


            #set simple names for graphing

            x=new_dates
            y=new_prices
            
            # Visualize Results
            #plt.plot(x, y)
            plt.scatter(x, new_prices, color='#0343df', label='Actual Price')  # plotting the initial datapoints
            plt.plot(x, regressor.predict(x), color='red', linewidth=3,
                 label='Predicted Price')  # plotting the line made by linear regression
            plt.title(' Prices over 3 Years (2016-2018)')
            plt.legend()
            plt.xlabel('Date Spread')
            plt.show()
        except:
            messagebox.showerror("Error","Please enter correct date in format DD/MM/YYYY")
            

    #Function to graph histogram chart
    def graphHistogram(self):
        x = prices
        num_bins = 10
        n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
        plt.title('Prices vs Frequency 2016-2018')
        plt.xlabel('Prices')
        plt.ylabel('Frequency')
        plt.show()
        
if __name__ == "__main__":
    root = Tk()
    root.geometry("300x300")
    app = StockApp(root)
    root.mainloop()









