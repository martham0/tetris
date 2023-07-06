# this is learntris.py
# import argparse
import sys
# Classes and starting variables
class Tetris:
    def __init__(self):
        self.matrix = [['.' for i in range(10)] for j in range(22)]

    def print_matrix(self):
      for row in self.matrix:
          print(' '.join(row))
      # print('space')

tetris = Tetris()
# Create an ArgumentParser object
# parser = argparse.ArgumentParser(description='Tetris')

# Add flags/arguments
# parser.add_argument('-p', action='store_true', help='print matrix')
# parser.add_argument('-q', action='store_true', help='quit program')
# parser.add_argument('--flag2', type=int, help='Description of flag 2')

# Parse the command-line arguments
# args = parser.parse_args()


# Access the flag values
# if args.p:
#     print(tetris.print_matrix())
#     # print('test')
# elif args.q:
#     # print('Goodbye')
#     sys.exit()
    
    

user_input = input()
if user_input == 'p':
    tetris.print_matrix()
    user_input = input()
elif user_input == 'q':
    sys.exit()
else:
    print('Command {} not recognized'.format(user_input))
    user_input = input()
