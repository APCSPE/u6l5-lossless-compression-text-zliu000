# this function takes a string message as a parameter,
# performs Run Length Encoding on the string,
# and returns a new string representing the compressed message.
def RLE_compress(message):
    compressed = ""
    counter = 1
    list_message = list(message)

    if len(list_message)-1 > 0:
        for i in range(len(list_message)-1):
            initial_letter = list_message[i]
            if initial_letter == list_message[i+1]:
                counter += 1
            else: 
                compressed = compressed + initial_letter + str(counter)
                counter = 1

        if list_message[-1] == list_message[-2]:
            compressed = compressed + initial_letter + str(counter)
        else: 
            counter = 1
            compressed = compressed + initial_letter + str(counter)

    else:
        compressed = compressed + list_message[0] + str(counter)
    
    return(compressed)


        



# TEST CODE:
print(RLE_compress("AABBBAAAABBBBBAAAAAABBBBBBB"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFF"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFD"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFDD"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFDDD"))
print(RLE_compress("ABCDEF"))
print(RLE_compress("FFFFFFFFFFFFFFFFFFF"))
print(RLE_compress("F"))
print(RLE_compress("F????"))
print(RLE_compress("Mmmmmmmmmm sooooo goooooood!"))
print(RLE_compress("Booooooooooooo, hisssssssss"))
