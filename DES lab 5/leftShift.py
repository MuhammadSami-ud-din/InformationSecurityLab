def desLeftShift(block , roundNo):

 if roundNo in [1 , 2 , 9 , 16]:
  leftshift = 1
 else:
  leftshift = 2 

 shifted_block = block[leftshift:] + block[:leftshift] 

 return shifted_block


text  = input("Enter the block:  ")


print("Shifted Block(3rd round): " , desLeftShift(text , 3) )
print("Shifted Block(2nd round): " , desLeftShift(text , 2) )
