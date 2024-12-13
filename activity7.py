miner = input("Please put your name --> ")
gold = 0
miner_action = input("Did you mine any gold today? Yes or No? ")

if miner_action.lower() == "yes" :
	gold += 1
	print(f"Hi {miner}, Today you have a total of {gold} gold")
elif miner_action.lower() == "no" :
	print(f"Hi {miner}, Today you have a total of {gold} gold")
else :
	print("You have type a different word that is not yes or no.. Try Again..")

print("\nBy Joshua Ezekiel A. Agawin,\nFrom BSIT_1C\nDate Created : 09/16/2024\nThank you!")