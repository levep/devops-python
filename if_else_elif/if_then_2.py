# Prompt user to enter number / test if even or odd





def main():
    number = int(input("Please enter an integer: "))

    if number % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")

if __name__=='__main__':
       main()