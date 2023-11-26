#importing libraries necessary for url validation
from urllib.parse import urlparse, urlsplit
#importing libraries necessary for web scraping
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
#importing json
import json
#importing libraries necessary to check file path
import os.path
import pathlib
#importing librarie necessary to display nested tabs as hierarchy
import itertools

tabs=[]
tabs_unsorted=[]

#OpenTab
#params:none
#the function that permits the user to add a new tab
def OpenTab(): #O(n*m)
    while True:
        print("Please enter the title of your website: ")
        title=input("")
        if not all([letter.isalpha() or letter.isspace() for letter in title]): #O(n),where n is the len(title)
            print("The title of a tab can only consists of letters and spaces!")
            continue           
        else: #O(n)
            print("Please enter the URL of the website: ")
            URL=input("")
            parsed_url= urlparse(URL)
            if parsed_url.scheme and parsed_url.netloc: #O(m), where m is the len(URL)
                global dic
                dic={"Title":title,"URL":URL, "NestedTabs":[]}
                tabs.append(dic)    #O(1)
                tabs_unsorted.append(dic)   #O(1)
                print("You have just added a new website,",title,"",URL)   #O(1)
            else:
                print("Please enter a valid URL!")  #O(1)
            break
    print(tabs)

#CloseTab
#params:none
#the function that permits the user to close a tab
def CloseTab(): #O(n)
    if len(tabs)==0:    #O(1)
        print("there is no tabs to close!")
    else:
        print("Please enter the index of the tab you wish to close: ")
        index=int(input(""))-1
        if 0<=int(index)<len(tabs): #O(n),where n is the len(tabs)
            tabs.pop(index)
            print("You have just closed the tab ",index+1)
            print(tabs)
        else:
            tabs_unsorted.pop()
            print("The index you entered is not available, the last opened tab has been closed!")
            print(tabs_unsorted)

#SwitchTab
#params:none
#the function that permits the user to display the contents of the desired tab
def SwitchTab(): #O(n*m)
        print("Please enter the index of the tab that you want to display it's content: ")
        display=int(input(""))-1
        if len(tabs)==0:
            print("There is no tabs to display!")
        elif 0<=int(display)<len(tabs): #O(n), where n is the len(tabs)
            url_displayed=tabs[display]['URL']
            reqs= requests.get(url_displayed)
            soup= BeautifulSoup(reqs.text, 'html.parser')
            for link in soup.find_all():    #O(m)
                print('Content of the website\n', reqs.content[:2000])
        else:   #O(n)
            url_displayed=tabs_unsorted[-1]['URL']
            reqs= requests.get(url_displayed)
            soup= BeautifulSoup(reqs.text, 'html.parser')
            for link in soup.find_all():    #O(m)
                print('Content of the website\n', reqs.content[:2000])
                    
#DisplayAll
#params:none
#the function that permits the user to display the titles of all opened tabs
def DisplayAll():
    for i in range(len(tabs)):
        print(tabs[i]['Title'])
        #I found the function flatten_hierarchy on https://stackoverflow.com/questions/44236188/python-create-hierarchy-file-find-paths-from-root-to-leaves-in-tree-represent
        def flatten_hierarchy(relations, parent=tabs):
            try:
                children= relations[parent]
            except KeyError:
                return None
            result=[]
            for child in children:
                sub_hierarchy= flatten_hierarchy(relations, child)
                try:
                    for element in sub_hierarchy:
                        result.append(tuple(itertools.chain([parent],element)))
                except TypeError:
                    result.append(parent,child)
            print(result)

#OpenNested
#params:none
#the function that permits the user to add a nested tab inside a main tab
def OpenNested(): #O(n*m*k)
    print("Please enter the index of the tab that you want to add a nested tab to: ")
    index=int(input(""))-1
    while 0>index or index>=len(tabs):  #O(n), where n is len(tabs)
        print("Please enter a valid index!")
    else:
        while True:
            print("Please enter the title of the nested tab you want to add: ")
            title1=input("")    
            if not all([letter.isalpha() or letter.isspace() for letter in title1]):    #O(m), where m is len(title1)
                print("The title of a tab can only consists of letters and spaces!")
                continue
            else:   #O(m)
                print("Please enter the contents of: ",title1)
                url1=input("")
                parsed_url= urlparse(url1)
                if parsed_url.scheme and parsed_url.netloc: #O(k)
                    tabs[index-1]["NestedTabs"].append(dic)
                    print("You have just added a new nested tab") #O(1)
                    print(dic)
                else:
                    print("Please enter a valid URL!")
                break
            
#SortAll
#params:none
#the function that helps the user to sort all the tabs by the title's of the tab alphabatical order 
def SortAll():  #O(m*n**2)
    border=0
    while border<len(tabs)-1:   #O(n), where n is len(tabs)
        minindex=border
        for i in range(border+1,len(tabs)): #O(n)
            tabs[i]['Title']=tabs[i]['Title'].lower()
            if tabs[i]['Title']<tabs[minindex]['Title']:#O(m) , where m is len(Title)
                minindex=i
        temp=tabs[border]['Title'] 
        tabs[border]['Title']=tabs[minindex]['Title']
        tabs[minindex]['Title']=temp
        border+=1
    print(tabs)
    
#SaveTabs
#params:none
#the function that permits the user to save the tabs to a file path as json file
def SaveTabs(): #O(n**2)
    print("Please provide the file path you want to save your tabs in it: ")
    file_path=input("")
    tabs_json=json.dumps(tabs)
    if os.path.exists(file_path): #O(n) where n is the len(file_path)
        with open(file_path,"w") as outfile: #O(n)
            outfile.write(tabs_json)
            print("Saved")
            print(tabs_json)
    else:
        print("The file path you entered doesn't exist! Please enter a valid file path.")
        
#ImportTabs
#params:none
#the function that permits the user to import tabs from a file path where they are saved before as json file
def ImportTabs():   #O(n*m)
    print("Please provide the file path you want to load tabs from it: ")
    file_path=input("")
    if os.path.exists(file_path):   #O(n), where n is len(file_path)
        with open('midterm.json',"r") as f: #O(m) 
            tabs_json=json.load(f)
        print(tabs_json)
        print("File loaded")
    else:
        print("The file path you entered doesn't exist! Please enter a valid file path.")
#MainMenu
#params: none
#the function that will run the main page
def MainMenu():
    choice=0
    while choice != 9:
        print("""Hello, please enter:
              1- Open tab.
              2- Close tab.
              3- Switch tab.
              4- Display all tabs.
              5- Open nested tab.
              6- Sort all tabs.
              7- Save tabs.
              8- Import tabs.
              9- Exit
              """)
        choice=int(input(""))
        if choice==1:
            OpenTab()
        elif choice==2:
            CloseTab()
        elif choice==3:
            SwitchTab()
        elif choice==4:
            DisplayAll()
        elif choice==5:
            OpenNested()
        elif choice==6:
            SortAll()
        elif choice==7:
            SaveTabs()
        elif choice==8:
            ImportTabs()
        elif choice==9:
            print("Thank you for using our tabs simulation browser.")
try:
    MainMenu()
except:
    print("invalid input!")