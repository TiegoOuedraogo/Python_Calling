message = 'The stock market for tech is:'
print(id(message)," This is for the first message")
price = "$1000"
print(message + " " + price)
# manipulating
new_message = message + " " + price
print(new_message)
# string are imunable look what is going on here
message = message + " " + price
print(id(message)," This is for the second message") #this message is totality from different from the messgae on top
