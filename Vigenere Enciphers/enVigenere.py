print("Please input the name of your txt file")
print("Use the format abc.txt")
file_name = input()
file = open(file_name, "r")
content = file.read()
file.close()

elements = list(content)
chr_list = []
for ele in elements:
    value = ord(ele)
    if (65 <= value <= 90):
        value -= 65
    elif (97 <= value <= 122):
        value -= 97
    else:
        pass
    chr_list.append(value)
    continue
print("Please enter the secret key")
key = list(input())
key_list = []
exit_val = 0
for elem in key:
    kvalue = ord(elem)
    if (65 <= kvalue <= 90):
        kvalue -= 65
    elif (97 <= kvalue <= 122):
        kvalue -= 97
    else:
        print("Key entered is out of format")
        exit_val = 1
        break
    key_list.append(kvalue)
    continue
if exit_val == 0:
    letter_count = 0
    for val in chr_list:
        if (0<= val <= 25):
            letter_count+=1
        
    txt_length = letter_count
    key_length = len(key_list)
    if txt_length != key_length:
        for j in range(txt_length - key_length):
            val = key_list[j]
            key_list.append(val)

    new_list = []
    key_pos_count = 0
    for k in range(len(chr_list)):
        if (0 <=chr_list[k] <= 25):
            new_val = int(chr_list[k]) + int(key_list[key_pos_count])
            new_val %= 26
            new_list.append(new_val)
            key_pos_count += 1
        else:
            new_list.append(chr_list[k])
    en_ascii_list = []
    eleme = ""
   
    for pos in range(len(new_list)):
        eleme = new_list[pos]
        if (65 <= ord(elements[pos]) <= 90):
            eleme += 65
        elif (97 <=ord(elements[pos])<= 122):
            eleme += 97
        en_value = chr(eleme)
        en_ascii_list.append(en_value)
        

    descript = ""
    for elemen in en_ascii_list:
        descript += elemen

    print("Please give encrypted file a name")
    print("Use the format xyz.txt")
    new_filename = input()
    new_file = open(new_filename, "w")
    new_file.write(descript)
    new_file.close()
