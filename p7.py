#7.To read a card as input and output if the card is lucky or not.

print("You Won , if your have number 234567, 777777, 121212, 990909 \n ")

number=int(input("Enter Your Card Number : "))


if len(number)==6:
    if number=="234567" or number=="777777" or number=="121212" or number=="990909":
        print("Congratulations Your Are Select in Lucky Draw.")
    else:
        print("Better Luck Next Time.")
else:
    print("Pls Enter Valid Card.!!")