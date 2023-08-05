data = input("Enter the data to be encrypted: ")
key = input("Enter the key: ")

original_data = data.replace(" ", "")
data_characters = list(original_data)
#print(data_characters)

if len(data_characters) > len(key):
    #print(len(data_characters)// len(key) +1)
    key = key * (len(data_characters) // len(key) + 1)
    #print(key)

elif len(data_characters) < len(key):
    key = key[:len(data_characters)]
    #print(key)
    
key_characters = list(key)

print ("The encrypted data is: ", end="")

for i in range(len(data_characters)):
    if data_characters[i] == " ":
        print(" ", end="")
    elif 65 <= ord(data_characters[i]) <= 90:
        if ord(data_characters[i]) + ord(key_characters[i]) - 65 > 90:
            print(chr(ord(data_characters[i]) + ord(key_characters[i]) - 65 - 26), end="")
        else:
            print(chr(ord(data_characters[i]) + ord(key_characters[i]) - 65), end="")
            
    elif 97 <= ord(data_characters[i]) <= 122:
        if ord(data_characters[i]) + ord(key_characters[i]) - 97 > 122:
            print(chr(ord(data_characters[i]) + ord(key_characters[i]) - 97 - 26), end="")
        else:
            print(chr(ord(data_characters[i]) + ord(key_characters[i]) - 97), end="")