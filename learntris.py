# this is learntris.py

# Classes and starting variables
class Tetris:
    def __init__(self):
        self.matrix = [['.' for i in range(10)] for j in range(22)]
    def print_matrix(self):
      for row in self.matrix:
          print(' '.join(row))
      print()
      

tetris = Tetris()
while True:
    user_input = input()
    if user_input == 'p':
        tetris.print_matrix()
    elif user_input == 'q':
        print('Goodbye!')
        break  # Exit the loop and terminate the program
    else:
        print('Command {} not recognized'.format(user_input))
