
def desPermutedChoice1(key):
    pc1_table = [
        57, 49, 41, 33, 25, 17,  9,
         1, 58, 50, 42, 34, 26, 18,
        10,  2, 59, 51, 43, 35, 27,
        19, 11,  3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
         7, 62, 54, 46, 38, 30, 22,
        14,  6, 61, 53, 45, 37, 29,
        21, 13,  5, 28, 20, 12,  4
    ]



    pc1_56 = "".join(key[pos-1] for pos in pc1_table)

    return pc1_56


text  = input("Enter the text:  ")
block = desPermutedChoice1(text)

print("Block: " , block )