#Minh Nguyen
#7/30/2018
#Final Project
#AccountStorage.py
#File for database control and manipulation 
import sqlite3

#conn = sqlite3.connect('Accounts.db')
#print ("Opened database successfully");
#Function to create user account table
def createTable():
    conn = sqlite3.connect('Accounts.db')
    print ("Opened database successfully");
    with conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS UserAccount")
        cursor.execute("CREATE TABLE UserAccount(id INTEGER PRIMARY KEY,u_name TEXT, u_pass TEXT,f_name TEXT, l_name TEXT,a_code TEXT, pin TEXT)")
        conn.commit()
        print ("Create table successfully");

#Function to clear user account table
def clear_table():
    conn = sqlite3.connect('Accounts.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM UserAccount")
    print ("Refresh main table successfully");
    
#Function to insert user account 
def insert_account(u_name,u_pass,f_name,l_name,a_code,pin):
    conn = sqlite3.connect('Accounts.db')
    with conn:
        cursor = conn.cursor()
        insert_stmt = ("INSERT INTO UserAccount (u_name,u_pass,f_name,l_name,a_code,pin) VALUES (?,?,?,?,?,?)")
        cursor.execute(insert_stmt,(u_name,u_pass,f_name,l_name,a_code,pin))
        conn.commit()

#Function to load user account        
def load_account():
    conn = sqlite3.connect('Accounts.db')
    data = []
    with conn:
        cursor = conn.cursor()
        load_stmt = ("SELECT * FROM UserAccount")
        cursor.execute(load_stmt)
        rows = cursor.fetchall()
        for row in rows:
            data.append(row)
        conn.commit()
        return data
    
