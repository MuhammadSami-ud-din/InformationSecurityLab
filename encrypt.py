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
    text = text.upper().replace('J' , 'I')
    filtered_text = [c for c in text if c.isalpha()]

    Pairs = []
    i = 0
   
    while i < len(filtered_text):
             a = filtered_text[i]

             if (i+1) < len(filtered_text):
                 b = filtered_text[i+1]

                 if ( a == b ):
                     Pairs.append(a + 'X')
                     i += 1
                 else:
                     Pairs.append(a + b)
                     i += 2

             else:
                 Pairs.append(a + 'X')
                 i += 1


    return Pairs


def get_position (matrix , char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r , c



def encryption(key , Plaintext):
    matrix = preparekey(key)   
    Pairs = prepare_text(Plaintext)
    cipherText = ""

    for a , b in Pairs:
        r1 , c1 = get_position(matrix , a)
        r2 , c2 = get_position(matrix , b)

        if (r1 == r2):
            cipherText += matrix[r1][(c1+1) % 5]
            cipherText += matrix[r2][(c2+1) % 5]

        elif (c1 == c2):
                cipherText += matrix[(r1+1) % 5][c1]
                cipherText += matrix[(r2+1) % 5][c2]

        else:
            cipherText += matrix[r1][c2]
            cipherText += matrix[r2][c1]


    return cipherText




                
print('\n --------------------Encryption Here----------------------\n')
key = input("Enter the Key for Your text: ")
Text = input("Enter the Plain Text: ")
print("Plain text:" + Text + '\n' + "Ciphered: " + encryption( key , Text) )
print('\n ---------------------------------------------------------\n')
                

# print(encryption( 'EXPLANATION' , 'Information security is a “MUST” to learn.'))


print('\n --------------------Matrix and Pairs here----------------------\n')
matrix = preparekey(key)
print('Matrix: \n')
for row in matrix:
    print( row )
print("\nPairs: " )
print( prepare_text(Text))

print('\n ---------------------------------------------------------\n')              

                







