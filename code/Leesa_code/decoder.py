message = input("enter a mesaage")
key = eval(input("enter key value from 1 to 26"))
message = message.lower()
output = ""
for letter in message:
    if letter.islower():
        value = ord(letter)+key
        letter = chr(value)
        if not letter .islower():
            value = 26
            letter = chr(value)
        output += letter
print("output message:", output)



