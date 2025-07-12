def ChekNum(Num):
    if(Num%2==0):
        print("Number is even")
    else:
        print("Number is odd")

def main():
    print("Enter the number :")
    Number=int(input())

    ChekNum(Number)

if __name__=="__main__":
    main()
