import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

sign = 0

global board
board = [["" for  x in range(3)]for y in range(3)]
#Lógica para o vencedor
def winner(b, l):
    return((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
          (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
          (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
          (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
          (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
          (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
          (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
          (b[0][2] == l and b[1][1] == l and b[2][0] == l)
          )
def gettext(i, j, gb, l1, l2):
    global sign
    if board[i][j] == '':
        if sign %2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "x"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "o"
        sign += 1
        Button[i][j].config(text=board[i][j])
        if winner(board, "x"):
            gb.destroy()
            box = messagebox.showinfo("Parabens", "O 1° Jogador ganhou a partida")
        elif winner(board, "o"):
            gb.destroy()
            box = messagebox.showinfo("Parabens", "O 2° Jogador ganhou a partida")
        elif(isfull()):
            gb.destroy()
            box = messagebox.showinfo("Empate", "Jogue denovo rapaz ")
#Verificar se o jogador pode apertar o botão ou não
def isfree(i, j):
    return board[i][j] == " "
#Verificar se o tabuleiro esta cheio
def isfull():
    flag = True
    for i in board:
        if(i.count('') > 0):
            flag = False
    return flag
#O GUI
def gameboard_pl(game_board, l1, l2):
    global Button
    Button = []
    for i in range(3):
        m = 3+i
        Button.append(i)
        Button(i) = []
        for j in range(3):
            n = j
            Button[i].append(j)
            get_t = partial(gettext, i, j, game_board, l1, l2)
            Button[i][j] = Button(game_board,bd=5, command=get_t, height=4, width=8)
            Button[i][j].grid(row=N,column=n)
    game_board.mainloop()