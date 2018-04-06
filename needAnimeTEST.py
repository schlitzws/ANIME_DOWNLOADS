import time

while(True):
    init_input = input("Please input what you would like to do next, h for the help.")
    if(init_input == "h"):
        print("""
           h key - Display this menu.
           l key - Displays a list of anime depending on the args supplied.
           d key - Downloads the anime from the target anime that you input.
           w key - Watches the anime from the target anime that you input.
           q key - To quit the program.
        """)
    elif(init_input == "d"):
        download()
    elif(init_input == "q"):
        print("Exiting program..")
        time.sleep(3)
        quit()
    elif(init_input == ""):
        print("Please input a specic key per the help menu, press h key for help")
