import tkinter
import os

adetails = open('details.txt', 'a') # use a.write(" ")
rpdetails = open('details.txt', 'r+')

def add_detail(detail):
    adetails.write("\n" + detail)
    return adetails.close()

def create_file(name):
    file = open('%s_file.txt' % (name), 'a')
    cont = True
    while cont == True:
        decision = input("Would you like to write to the file? (y/n)")
        if decision == 'y':
            write = input("Input here...")
            file.write("\n" + write)
            decision2 = input("Continue?")
            if decision2 == 'y':
                decision == 'y'
            elif decision2 == 'n':
                cont = False
        elif decision == 'n':
            cont = False
    return

def view_file(filename):
    file = open('%s_file.txt' % (filename), 'r')
    return print(file.read())

def write_file(text):
    file = open('%s_file.txt' % (filename), 'a')
    return file.write(text)

def create_account(u, p):
    os.makedirs(u)
    ufile = open('%s\%s_details.txt' % (u, u), 'a')
    ufile.write(u + "\n" + p)
    return "Successful"

def login(u, p):
    ufile = open('%s\%s_details.txt' % (u, u), 'r+')
    for line in ufile.readlines():
        check = line.split()
        if u == check[0] and p == check[1]:
            print("Login successful")
        else:
            print("Login failed")
    return
    
# So far all functional except login function. other functions created for future use, although may not be needed. 
