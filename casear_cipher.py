alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encryption(text,shift):
    cipher = ""
    for char in text :
        if char in alphabets:
            position = alphabets.index(char)
            new_pos = (position + shift)%26
            cipher += alphabets[new_pos]
        else :
            cipher+= char
    print(f"new Text after encryption is : {cipher}")

def decryption(text,shift):
    lst = ""
    for char in text :
        if char in alphabets:
            position = alphabets.index(char)
            new_pos = (position - shift)%26
            lst += alphabets[new_pos]
        else :
            cipher+=char
    print(f"new Text after encryption is : {lst}")

want = False
while not  want:
    w = input("Type 'encrypt' for Encription and 'decrypt' for Decryption :" )
    text = input("Type Your Text :")
    shift= int(input("Enter shift key :"))

    if w == "encrypt":
        encryption(text,shift)
    elif w == "decrypt":
        decryption(text,shift)
    play_more = input("Do You Want MOre Type YES Or NO! :")
    if play_more == 'NO':
        want = True
        print("Thank you Have Nice Day! BYE ")