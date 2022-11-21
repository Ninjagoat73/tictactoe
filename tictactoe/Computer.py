from math import inf as infinity
from random import choice
from os import system
import tkinter as tk
from tkinter import *
from tkinter import messagebox

turns = 0
HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def evaluate(state):
    """
    Trial and Error módon rangsorolja az összes lépést

    param state: a tábla jelenlegi állapota
    return: +1 ha a gép nyer; -1 ha az ember nyer; 0 ha döntetlen
    """

    global score
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0
    return score


def wins(state,player):
    """
    Teszteli az összes lehetséges nyerő állást. Lehtőségek:
    * Három sor    [X X X] or [O O O]
    * Három oszlop    [X X X] or [O O O]
    * Kettő kereszt [X X X] or [O O O]

    param state: a tábla éppeni állapota
    param player: ember vagy gép

    return: True, ha a player nyer
    """

    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    Teszteli hogy a gép vagy az ember nyer

    param state: a tábla éppeni állapota
    return: True, ha nyer a gép vagy az ember
    """

    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    """
    Minedn üres kocka hozzáadódik egy listához

    param state: a tábla éppeni állapota
    return: üres cellákból álló listát
    """

    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    return cells


def valid_move(x, y):
    """
    Ha a kocka benne van az empty_cells-ben akkor lehetséges lépés
    
    param x: x koordináta
    param y: y koordináta

    return: True, ha a board[x, y] üres
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Ha lehetséges a lépés átváltja a játékmezőt
    
    param x: x koordináta
    param y: y koordináta
    param player: ember vagy gép
    """

    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    """
    Gépnek függvény, hogy megtalálja a legjobb lépést

    param state: a tábla éppeni állapota
    param depth: "gondolkodás" mélysége
    param player: ember vagy gép

    return: listát [legjobb sor, legjobb oszlop, legjobb pontozás]
    """

    if player == COMP:
        best = [-1, +1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value
    return best

def ai_turn():
    """
    Ha a depth(mélység) kisebb mint 9 hívja a minimax függvényt
    ha nem akkor random választ kockát

    global variables: turns
    """

    global turns

    ## Depth = hány kör van a játékból és mennyit kell ellőre néznie
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    ## Ha a depth == 9 akkor random választ kockát
    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    ## Ha nem akkor a minimax funkciót használja
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]
    ## Beírjuk a játékmezőbe a lépést
    set_move(x, y, COMP)
    if x == 0 and y == 0:
        b1['text'] = 'O'
    elif x == 0 and y == 1:
        b2['text'] = 'O'
    elif x == 0 and y == 2:
        b3['text'] = 'O'
    elif x == 1 and y == 0:
        b4['text'] = 'O'
    elif x == 1 and y == 1:
        b5['text'] = 'O'
    elif x == 1 and y == 2:
        b6['text'] = 'O'
    elif x == 2 and y == 0:
        b7['text'] = 'O'
    elif x == 2 and y == 1:
        b8['text'] = 'O'
    elif x == 2 and y == 2:
        b9['text'] = 'O'
    turns = turns+1
    var.set("It is turn:" + str(turns))



def human_turn(b,r,c):

    """
    Kört átadja a gépnek és kitölti a játék mezőt.
    Ellenörzi, hogy nyert-e valaki
    
    global váltaozók: turns, player_label
    param b: a gomb amit megnyomunk és változtatunk
    param r: a játék mező sora
    param c: a játékmező oszlopa
    """

    global turns
    global player_label

    if b['text'] == "":
        if turns%2 == 0:
            b['text']='X'
            playerlabelvar.set("It's your turn!")
            board[r][c]=HUMAN   
    else: 
        messagebox.showerror("Error","This box is already filled")
        human_turn()
    turns = turns + 1         
    var.set("It is turn:" + str(turns))
    if game_over(board) == True:
        pass
    else:
        ai_turn()
    
    if wins(board, HUMAN):
        winwindow("YOU")
    elif wins(board, COMP):
        winwindow("THE AI")
    elif turns >= 9:
        winwindow("NOBODY")

def winwindow(winner):

    """
    A nyertest kiíró ablak

    param winner: A nyertes játékos
    """

    global wwindow

    wwindow = Toplevel(window)
    wwindow.title("This is the winner window")
    wlabel = tk.Label(wwindow,text="THE WINNER IS:")
    wlabel.grid(row=0, column=1)
    wlabel2 = tk.Label(wwindow,text=winner)
    wlabel2.grid(row=1,column=1)
    wbutton = tk.Button(wwindow,text='Leave Game',command=window.destroy)
    wbutton.grid(row=2,column=1)
    wbutton2 = tk.Button(wwindow,text='Return to Menu',comman=window.destroy)
    wbutton2.grid(row=2,column=2)


def main():
    """
    Játék grafika

    global variables: window, b1-b9,player_laber, var, playerlabervar
    """
    global window
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7    
    global b8
    global b9
    global player_label
    global playerlabelvar
    global var

    window = tk.Tk()
    playerlabelvar = StringVar()
    playerlabelvar.set("You start the game!")
    var = StringVar()
    var.set("The game begins!")
    window.resizable(True,True)
    window.title("A fun game of Tic Tac Toe againts an AI")


    player_label = tk.Label(window, textvariable = playerlabelvar, font=('Times', 15))
    player_label.grid(row=0,column=0)

    turn_label = tk.Label(window, textvariable = var,  font=('Times', 15))
    turn_label.grid(row=4,column=1)

    quit_button = tk.Button(window, text="Quit Game", font=('Times', 15), command=quit)
    quit_button.grid(row=0,column=2)

    b1 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: human_turn(b1,0,0))
    b2 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: human_turn(b2,0,1))
    b3 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: human_turn(b3,0,2))
    b4 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: human_turn(b4,1,0))
    b5 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: human_turn(b5,1,1))
    b6 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: human_turn(b6,1,2))
    b7 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: human_turn(b7,2,0))
    b8 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: human_turn(b8,2,1))
    b9 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: human_turn(b9,2,2))

    b1.grid(row=1,column=0)
    b2.grid(row=1,column=1)
    b3.grid(row=1,column=2)
    b4.grid(row=2,column=0)
    b5.grid(row=2,column=1)
    b6.grid(row=2,column=2)
    b7.grid(row=3,column=0)
    b8.grid(row=3,column=1)
    b9.grid(row=3,column=2)

    window.mainloop()

if __name__ == '__main__':
    main()