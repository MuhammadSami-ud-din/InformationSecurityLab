def rail_fence_encrypt(text, key):
    cleanText = text.replace(" " , "")

    if key <= 1 or key >= len(cleanText):
        return text

    rails = [[] for _  in range(key)] 

    direction = 1
    rail = 0

    for char in cleanText:
        rails[rail].append(char)

        if rail == 0:
            direction = +1
        elif rail == key-1:
            direction =  -1

        rail += direction



    return "".join("".join(rail) for rail in rails)   


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



print("\n----------------------Encryption-------------------")
text = input("Enter the message to Encrypt: ")
key = int(input("Enter the Key: "))


print("\n\nEncrypted Text:" , rail_fence_encrypt(text, key) )


print_zigzag(text , key)

print("\n--------------------------------------------------\n")
                





