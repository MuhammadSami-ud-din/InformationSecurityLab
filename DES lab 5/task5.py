def desPermutedChoice2(key):
    pc2_table = [
        14, 17, 11, 24,  1,  5,
         3, 28, 15,  6, 21, 10,
        23, 19, 12,  4, 26,  8,
        16,  7, 27, 20, 13,  2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]



    pc2_48 = "".join(key[pos-1] for pos in pc2_table)

    return pc2_48


text  = input("Enter the text:  ")
block = desPermutedChoice2(text)

print("Block: " , block )