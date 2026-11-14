data ={ }

def check(n):
    highest = 0



flag = False
while not flag :
    name = input("Enter the Name :")
    bid_price = int(input("Enter the bid price :"))

    data[name]=bid_price
    want = input("Do you Want to Bid ? type 'yes' or 'no':").lower
if want == 'no':
    flag = True
    check(data)            
