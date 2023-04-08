while(True):
    print("press q to quit")
    a = input("enter a number : " )
    if a == 'q' :
        break
    try:
        a = int(a)
        if a > 6 :
            print("you enterd a number greater then 6")
    except Exception as e:
        print(f"your input resulted in an error : {e}")

print("Thanks for playing this game")







