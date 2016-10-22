"""This is the entry point of the program."""

def create_box(height, width, character):
   result_string = ''
   for i in range(height):
       line = ''
       for j in range (width):
           line += character
       result_string += (line + '\n')
   return result_string

       
if __name__ == '__main__':
  box = create_box(4, 3, '*')    
  print(box)



