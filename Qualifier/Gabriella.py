"""
file: Gabriella.py
author: Anthony Prestia
problem: Gotta go your own way (obvious HSM reference, IE the file name)
description: maze problem
"""
def moves(grid,move_string):
    new_move = ''
    for letter in move_string:
        if letter == 'E':
            new_move += 'S'
        else:
            new_move += 'E'
    return new_move

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        p = input()
        print("Case #",i+1,': ',moves(n,p), sep = '')
main()