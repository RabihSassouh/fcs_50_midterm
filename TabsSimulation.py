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
tabs=[]
#OpenTab
#
#
def OpenTab():
    while True:
        print("Please enter the title of your website: ")
        title=input("")
        if not all([letter.isalpha() or letter.isspace() for letter in title]):
            print("The title of a tab can only consists of letters and spaces!")
            continue           
        else:
            print("Please enter the URL of the website: ")
            URL=input("")
            parsed_url= urlparse(URL)
            if parsed_url.scheme and parsed_url.netloc:
                global dic
                dic={"Title":title,"URL":URL, "NestedTabs":[]}
                tabs.append(dic)
                print("You have just added a new website, ",title,"",URL)
            else:
                print("Please enter a valid URL!")
            break
    print(tabs)

#CloseTab
#
#
def CloseTab():
    if len(tabs)==0:
        print("there is no tabs to close!")
    else:
        print("Please enter the index of the tab you wish to close: ")
        index=input("")
        if 1<=int(index)<=len(tabs):
            tabs.remove(index-1)
            print("You have just closed the tab ",index-1)
        else:
            tabs.popitem()
            print("The index you entered is not available, the last opened tab has been closed!")
    print(tabs)

#SwitchTab
#
#
def SwitchTab():
        print("Please enter the index of the tab that you want to display it's content: ")
        display=int(input(""))-1
        if len(tabs)==0:
            print("There is no tabs to display!")
        elif 0<=int(display)<=len(tabs):
                url_displayed=tabs[display]['URL']
                reqs= requests.get(url_displayed)
                soup= BeautifulSoup(reqs.text, 'html.parser')
                for link in soup.find_all():
                    print(link.get('href'))
                    
#DisplayAll
#
#
def DisplayAll():
    for i in range(len(tabs)):
        print(tabs[i]['Title'])                

#OpenNested
#
#
def OpenNested():
    print("Please enter the index of the tab that you want to add a nested tab to: ")
    index=int(input(""))-1
    while 0>index or index>=len(tabs):
        print("Please enter a valid index!")
    else:
        while True:
            print("Please enter the title of the nested tab you want to add: ")
            title1=input("")
            if not title1.isalpha(): #i should add or if space
                print("The title of a tab can only consists of letters and spaces!")
                continue
            else:
                print("Please enter the contents of: ",title1)
                url1=input("")
                parsed_url= urlparse(url1)
                if parsed_url.scheme and parsed_url.netloc:
                    tabs[index-1]["NestedTabs"].append(dic)
                    print("You have just added a new nested tab")
                    print(dic)
                else:
                    print("Please enter a valid URL!")
                break
            
            
#SortAll
#
#
def SortAll():
    border=0
    while border<len(tabs)-1:
        minindex=border
        for i in range(border+1,len(tabs)):
            tabs[i]['Title']=tabs[i]['Title'].lower()
            if tabs[i]['Title']<tabs[minindex]['Title']:
                minindex=i
        temp=tabs[border]['Title'] 
        tabs[border]['Title']=tabs[minindex]['Title']
        tabs[minindex]['Title']=temp
        border+=1
    print(tabs)
    
#SaveTabs
#
#
def SaveTabs():
    print("Please provide the file path you want to save your tabs in it: ")
    file_path=input("")
    # with open(file_path,"w") as outfile:
    #     outfile.write(tabs_json)
    #     print("Saved")
    # We can check if the path entered by the user exists or not:
    for i in range (len(tabs)):
        tabs_json=json.dumps(tabs[i])
        if os.path.exists(file_path):
            with open(file_path,"w") as outfile:
                outfile.write(tabs_json)
                print("Saved")
                print(tabs_json)
        else:
            print("The file path you entered doesn't exist! Please enter a valid file path.")
        
#ImportTabs
#
#
def ImportTabs():
    print("Please provide the file path you want to load tabs from it: ")
    file_path=input("")
    if os.path.exists(file_path):
        with open('midterm.json',"r") as f:
            tabs_json=json.load(f)
        print(tabs_json)
        print("File loaded")
    else:
        print("The file path you entered doesn't exist! Please enter a valid file path.")
#MainMenu
#
#
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
MainMenu()