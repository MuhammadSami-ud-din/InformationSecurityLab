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


def print_zigzag(text, key):
    cleanText = text.replace(" ", "")
    
    if key <= 1:
        print(cleanText)
        return

 
    grid = [[" " for _ in range(len(cleanText))] for _ in range(key)]
    
    direction = 1
    rail = 0
    

    for col, char in enumerate(cleanText):
        grid[rail][col] = char
        
        if rail == 0:
            direction = 1
        elif rail == key - 1:
            direction = -1
            
        rail += direction
        
   
    print("\n--- Visual Zigzag Structure ---")
    for row in grid:
        print(" ".join(row))

    



print("\n----------------------Decryption-------------------")
text = input("Enter the message to decrypt: ")
key = int(input("Enter the Key: "))

decrypted = rail_fence_decrypt(text, key)
print("\n\nDecrypted Text:" , decrypted )

print_zigzag(decrypted , key)

print("\n--------------------------------------------------\n")