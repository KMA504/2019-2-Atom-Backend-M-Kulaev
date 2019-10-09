"""
modules
"""
import numpy as np
from tabulate import tabulate

class Game:
    """
    Game class
    """
    def __init__(self, dim):
        """
        init
        """
        self.dim = dim
    def start(self):
        """
        Game launcher
        """
        a_a = np.chararray((self.dim, self.dim), unicode=True)
        a_a[:] = ''
        print('Let\'s start! X goes first!')
        print('\n')
        print('Your field:')
        self.printer(a_a)
        var = 'X'
        j = 0
        while True:
            a_a = self.invite(a_a, var)
            #import pdb
            #pdb.set_trace()
            if isinstance(a_a, str):
                print('Finish!')
                print('Winner is '+a_a)
                break
            self.printer(a_a)
            j += 1
            if j == self.dim**2:
                print('Draw!')
                break
            if var == 'X':
                var = 'O'
            else:
                var = 'X'
    def printer(self, a_a):
        """
        Printer of the game field
        """
        hds = range(self.dim)
        print(tabulate(a_a, showindex='always', headers=hds, stralign='center', tablefmt='grid'))
        return
    def invite(self, a_a, var):
        """
        One action
        """
        #dim = a.shape[0]
        print('\n')
        print(var+', continue!')
        try:
            print('Enter coordinates - horizontal and vertical!')
            hor, ver = map(int, input().split())
        except ValueError:
            print('Bad, try again!')
            a_a = self.invite(a_a, var)
            return a_a
        if hor >= self.dim or ver >= self.dim or hor < 0 or ver < 0:
            print('Bad, our space is finite!')
            a_a = self.invite(a_a, var)
            return a_a
        a_a = self.step(a_a, ver, hor, var)
        return a_a
    def step(self, a_a, x_x, y_y, var):
        """
        Game step in action
        """
        if a_a[x_x][y_y] == '':
            a_a[x_x][y_y] = var
            res = self.check_winner(a_a, var)
            if res == 'continue':
                return a_a
            return var
        print('Bad, this cell is occupied!')
        a_a = self.invite(a_a, var)
        return a_a
    def check_winner(self, a_a, var):
        """
        Check the final or not
        """
        #dimer = a.shape[0]
        for i in range(self.dim):
            if ''.join(a_a[i]) == var*self.dim or ''.join(a_a[:, i]) == var*self.dim \
            or ''.join(a_a.diagonal()) == var*self.dim:
                return var
            if ''.join(np.fliplr(a_a).diagonal()) == var*self.dim:
                return var
        return 'continue'

print('Enter the dimensionality of field.')
GAMER = Game(int(input()))
GAMER.start()
