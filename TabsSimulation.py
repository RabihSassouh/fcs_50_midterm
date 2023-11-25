#importing libraries necessary for web scraping
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

tabs=[]
#OpenTab
#
#
def OpenTab():
    print("Please enter the title of your website: ")
    title=input("")
    print("Please enter the URL of the website: ")
    URL=input("")
    dic={"Title":title,"URL":URL}
    tabs.append(dic)
    print("You have just added a new website, ",title,"",URL)
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
        elif choice==9:
            print("Thank you for using our tabs simulation browser.")
MainMenu()