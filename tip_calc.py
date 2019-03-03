good = float(.20)
fair = float(.15)
bad = float(.10)

bill = float(input("Total bill amount?: "))
service = (input("Level of service, good,fair or bad?: "))

if service == "good":
    print("Tip amount " + str(bill * .20))
elif service == "fair":
    print("Tip amount " + str(bill * .15))
elif service == "bad":
    print("Tip amount " + str(bill * .10))



if service == "good":
    final_tip = (good * bill) + bill
elif service == "fair":
    final_tip = (fair * bill) + bill
elif service == "bad":
    final_tip = (bad * bill) + bill

print("Total amount " + str(final_tip))