import os
data ={ }

def check(n):
    highest = 0
    winner=""
    for bidder in data:
        current_price = n[bidder]
        if(current_price>highest):
            highest = current_price
            winner = bidder
    print(data)
    print(f"The winner is {winner} with a bid of {highest}")  



flag = False
while not flag :
    name = input("Enter the Name :")
    bid_price = int(input("Enter the bid price :"))

    data[name]=bid_price
    want = input("Do you Want to Bid ? type 'yes' or 'no':").lower()
    if want == "no":
        flag = True
    elif want == "yes":
        os.system('cls')
check(data)            
