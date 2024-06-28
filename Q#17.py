# Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500	






balance = 0

while True:
    transaction = input("Enter transaction or ('exit to quit'): ")
    if transaction.lower() == "exit":
        break
    separate = transaction.split(" ")
    if (len(separate) != 2):
        print("Invalid input format.")
        continue
    if "D" in separate:
        balance += int(separate[1])
    elif "W" in separate:
        balance -= int(separate[1])
    else:
        print("Invalid transaction type. Use 'D' for deposit and 'W' for withdrawal.")
print(f"The net balance is: {balance}")
