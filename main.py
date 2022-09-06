## This is a test script that just prints out the Inputted First and Last Name


## gets Names


def getName():
    firstName = input("Please Enter Your first Name: \n")
    lastName = input("Please Enter Your Last Name: \n")
    return [firstName, lastName]

#main Process
def main():
    name = getName()
    print(f"Hello {name[0]} {name[1]}!")

if __name__ == '__main__':
    main()
