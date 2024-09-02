#(13).Exact change: Given a price identify if you have exact change summing up to that price?
#(Count all combinations of coins to make a given value sum.)

price = int(input('Enter Price: '))

currency1 = int(input("Enter Currency 1: "))
currency2 = int(input("Enter Currency 2: "))
currency3 = int(input("Enter Currency 3: "))


combination_count = 0

print(f"{currency1}-{currency2}-{currency3}")

# Loop through possible counts of each currency to find combinations that sum up to the price
for count1 in range(price // currency1 + 1): #10 to 0-11 exe
    for count2 in range(price // currency2 + 1): #20 to 0-5 exe
        for count3 in range(price // currency3 + 1): #50 to 0-2
            total = count1 * currency1 + count2 * currency2 + count3 * currency3
            if total == price:
                print(count1,count2,count3)
                combination_count += 1

print(f"Total combinations found: {combination_count}")




