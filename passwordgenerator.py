import random


alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numeric=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','+']

print("welcome to the password generator")
print(r''' 
       ooo,    .---.
      o`  o   /    |\________________
     o`   'oooo()  | ________   _   _)
     `oo   o` \    |/        | | | |
       `ooo'   `---'         "-" |_|''')


num_alpha=int(input("Enter how many alpahabets you need??? \n"))  
num_number=int(input("Enter how many numbers you need??? \n"))  
num_char=int(input("Enter how many special characters you need??? \n"))  


easypassword=[]


for i in range (0,num_alpha):
    easypassword+=random.choice(alpha)
for i in range (0,num_number):
    easypassword+=random.choice(numeric)
for i in range(0,num_char):
    easypassword+=random.choice(symbols)
random.shuffle(easypassword)
password=""
for i in easypassword:
    password+=i
print(f"here is your password !!! {password}")


