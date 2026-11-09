#number challenge
print("-------NUMBER CHALLENGE--------")
fix_number=18
attempts=0
while True:
    num=int(input("Please enter the number between 1 to 100 "))
    if num<1 or num>100:
        print("Enter the number between 1 to 100")
        continue
    attempts=attempts+1
    if num==fix_number:
        print("\nCongrajulations!!!")
        print(f"You found the number in {attempts} attempts")
        break
    elif num<fix_number:
        print("YOUR NUMBER IS LOW!! (HINT)")
    else:
        print("YOUR NUMBER IS HIGH!! (HINT)")
        
    print("GAME OVER")
