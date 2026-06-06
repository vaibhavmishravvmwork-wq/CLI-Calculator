class Calculator:
    def __init__(self):
        print('''       
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
Starting Calculator ......
              ''')
    
    def menu(self):
        
        
        print("Options Menu ____")
        
        print("\t1. Addition")
        print("\t2. Subtraction")
        print("\t3. Multiplication")
        print("\t4. Division")
        print("\t5. Exit")

    def start(self):
        # print("Starting Calculator ......")
        while True:
            self.menu()
            try:
                choice = int(input("Enter Your Choice : "))
            except:
                print("Hey you dumb!!! what the hell are you entering????")
            
            if choice == 1:
                self.addition()
            elif choice == 2:
                self.subtraction()
            elif choice == 3:
                self.multiplication()
            elif choice == 4:
                self.division()
            elif choice == 5:
                print("Thanks for using the Calculator!!!")
                break
            else:
                print("Invalid Choice !!!")
           

    def addition(self):
        print("\nADDITION__________")
        result_addition = 0
        num_lst = []
        inps = 'y'
        while inps == 'y':
            num = int(input("\tEnter number : "))
            num_lst.append(num)
            inps = input("Enter 'y' to add more : ")
        else:
            for i in num_lst:
                result_addition += i
            print(f"Result : \n\t{' + '.join(map(str,num_lst))} = {result_addition}\n")

    def subtraction(self):
        print("\nSUBTRACTION__________")
        num_lst = []
        inps = 'y'
        while inps == 'y':
            num = int(input("\tEnter number : "))
            num_lst.append(num)
            inps = input("Enter 'y' to subtract more : ")
        else:
            result_subtraction = num_lst[0]
            for i in range(1,len(num_lst)):
                result_subtraction -= num_lst[i]
            print(f"Result : \n\t{' - '.join(map(str,num_lst))} = {result_subtraction}\n")

    def multiplication(self):
        print("\nMULTIPLICATION__________")
        num_lst = []
        inps = 'y'
        while inps == 'y':
            num = int(input("\tEnter number : "))
            num_lst.append(num)
            inps = input("Enter 'y' to multiply more : ")
        else:
            result_multiplication = num_lst[0]
            for i in range(1,len(num_lst)):
                result_multiplication *= num_lst[i]
            print(f"Result : \n\t{' x '.join(map(str,num_lst))} = {result_multiplication}\n")

    def division(self):
        print("\nDIVISION__________")
        num_lst = []
        inps = 'y'
        while inps == 'y':
            num = int(input("\tEnter number : "))
            num_lst.append(num)
            inps = input("Enter 'y' to divide more : ")
        else:
            result_division = num_lst[0]
            for i in range(1,len(num_lst)):
                result_division /= num_lst[i]
            print(f"Result : \n\t{' / '.join(map(str,num_lst))} = {result_division}\n")



if __name__ == "__main__":
    c = Calculator()
    c.start()