    #OpenTab
#
#
def OpenTab():
    print("Please enter the title of your website: ")
    title=input("")
    print("Please enter the URL of the website: ")
    URL=input("")
    print("You have just added a new website, ",title,"",URL)
    
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
        elif choice==9:
            print("Thank you for using our tabs simulation browser.")
MainMenu()