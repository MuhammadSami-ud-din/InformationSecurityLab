def rail_fence_decrypt(cipher, key):
    cleanText = cipher.replace(" " , "")

    grid = [["" for _ in range(len(cleanText))] for _ in range(key)]


    if key <= 1 or key >= len(cleanText):
        return cleanText

    rail = 0 
    direction = 1

    for col in range(len(cleanText)):
        grid[rail][col] = "*"

        if rail == 0:
            direction = 1
        elif rail == key - 1:
            direction = -1


        rail += direction

    cipher_index = 0
    for r in range(key):
        for c in range(len(cleanText)):
            if grid[r][c] == "*" and cipher_index < len(cleanText):  
                grid[r][c] = cleanText[cipher_index]
                cipher_index += 1

    plain_text = []
    rail = 0
    direction = 1             

    for col in range(len(cleanText)):
         plain_text.append(grid[rail][col])
         if rail == 0:
                    direction = 1
         elif rail == key - 1:
                    direction = -1
        
        
         rail += direction

    return "".join(plain_text)
    



def decrypt_brute_force(text ):
     cleanText = text.replace(" " , "")
     result = []

     for key in range(2 , len(text)):
          decrypted =  rail_fence_decrypt(cleanText , key)
          result.append((key , decrypted))
          print("Key: " , key , "\n" , "Decrpyted text: " , decrypted)
     return result



print("\n----------------------Decryption-------------------")
text = input("Enter the message to decrypt: ")
decrypt_brute_force(text)




print("\n--------------------------------------------------\n")