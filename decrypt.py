def preparekey (key):
    key = key.upper().replace('J' , 'I')
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    combined = key + alphabet

    unique_letters = []
    for char in combined:
        if char.isalpha() and char not in unique_letters:
            unique_letters.append(char)

    matrix = [unique_letters[i:i+5] for i in range(0 , 25 , 5)] 
    return matrix


def prepare_text(text):

    Pairs = []
    i = 0
    
    while i < len(text):
             a = text[i]

             if (i+1) < len(text):
                 b = text[i+1]
                 Pairs.append(a+b)
                 i+=2
             else:
                 Pairs.append(a + 'X')
                 i += 1


    return Pairs


def get_position (matrix , char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r , c



def decryption(key , cipherText):
    matrix = preparekey(key)   
    Pairs = prepare_text(cipherText)
    DecipheredText = ""

    for a , b in Pairs:
        r1 , c1 = get_position(matrix , a)
        r2 , c2 = get_position(matrix , b)

        if (r1 == r2):
            DecipheredText += matrix[r1][(c1-1) % 5]
            DecipheredText += matrix[r2][(c2-1) % 5]

        elif (c1 == c2):
                DecipheredText += matrix[(r1-1) % 5][c1]
                DecipheredText += matrix[(r2-1) % 5][c2]

        else:
            DecipheredText += matrix[r1][c2]
            DecipheredText += matrix[r2][c1]


    return DecipheredText

print('\n --------------------Decryption Here----------------------\n')
key = input("Enter the Key for Your Ciphered text: ")
CipheredText = input("Enter the Ciphered Text: ")
                

print("Cipher:" + CipheredText + '\n' + "Deciphered: " + decryption( key , CipheredText) )
print('\n ---------------------------------------------------------\n')

print('\n --------------------Matrix and Pairs here----------------------\n')
matrix = preparekey(key)
print('Matrix: \n')
for row in matrix:
    print( row )
print("\nPairs: " )
print( prepare_text(CipheredText))

print('\n ---------------------------------------------------------\n')                  







