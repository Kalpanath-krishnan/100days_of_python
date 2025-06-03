print("welcome to the tip caculator \n")
amnt=int(input("what is the total bill amount \n"))
tip= int(input("what percentage do you want to tip \n"))
people= int(input("how many persons are there \n"))
tip_amount=(amnt*(tip/100))/people
print(f" you are {people} people so your tip amonunt is {tip_amount} for each person")
