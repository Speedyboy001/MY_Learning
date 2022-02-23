#Phone Book
phonebook = {}
def add():
    y = str(input("Enter the name: "))
    z = int(input("Enter the number: "))
    phonebook[y] = z
def show():
    if len(phonebook) == 0:
            print("Phone book is empty add some numbers")
            
    else:
        y = str(input("Enter the name:\n"))
        print(phonebook[y])
        
while True:
    
    print("1 - Add")
    print("2 - View")
    print("3 - Quit")
    x = int(input("Enter the choice: "))
    if x == 1:
        add()
    elif x ==2:
        show()
    elif x ==3:
        print("--Exiting--")
        break
    else:
        print("Andha hai bey sahi se dekh fir select kr")
