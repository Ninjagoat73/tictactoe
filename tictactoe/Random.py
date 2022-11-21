import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np 

def random_turn_change(b,r,c):
    """
    Megváltoztatja a játék mezőt és hívja a gépet
    ha még nem nyert senki

    global variables: turns, player_label
    param b: a gomb amit megnyomunk és változtatunk
    param r: a játék mező sora
    param c: a játékmező oszlopa
    """

    global turns
    global player_label

    if b['text'] == "":
        if turns%2 == 0:
            b['text']='X'
            playerlabelvar.set("It's the AI's turn")
            board[r][c]="X"
        turns = turns + 1        
    else: messagebox.showerror("Error","This box is already filled")    
    var.set("It is turn:" + str(turns))
    if win_check() == True:
        pass
    else:
        random_move()

def random_move():
    """
    A gép kiválaszt egy random sort és oszlopot amíg nem szabad a választott kocka
    és hívja a wincheck()-et

    global váltaozók: turns
    """

    global turns

    unplayable = True
    while unplayable:
        random_row = np.random.randint(3, size=1)
        random_place = np.random.choice(board[random_row[0], :])

        ## Ellenőrizzük a kocka elérthetőségét
        if random_place == 'X' or random_place == 'O':
            pass
            if turns >= 8:
                unplayable = False
        else:
            unplayable = False
    ## Átirjuk a boardot ott ahova a gép rakott jelet
    if random_place == '1':
        b1['text']='O'
        playerlabelvar.set("It's the Player's turn")
        board[0][0]='O'
        turns = turns + 1
    elif random_place == '2':
        b2['text']='O'
        playerlabelvar.set("It's the Player's turn")
        board[0][1]='O'
        turns = turns + 1
    elif random_place == '3':
        b3['text']='O'
        playerlabelvar.set("It's the Player's turn")
        board[0][2]='O'
        turns = turns + 1
    elif random_place == '4':
        b4['text']='O'
        playerlabelvar.set("It's the Player's turn")
        board[1][0]='O'
        turns = turns + 1
    elif random_place == '5':
        b5['text']='O'
        playerlabelvar.set("It's the Player's turn")
        board[1][1]='O'
        turns = turns + 1
    elif random_place == '6':
        b6['text']='O'
        playerlabelvar.set("It's the Player's turn")
        board[1][2]='O'
        turns = turns + 1
    elif random_place == '7':
        b7['text']='O'
        playerlabelvar.set("It's the Player's turn")
        board[2][0]='O'
        turns = turns + 1
    elif random_place == '8':
        b8['text']='O'
        playerlabelvar.set("It's the Player's turn")
        board[2][1]='O'
        turns = turns + 1
    elif random_place == '9':
        b9['text']='O'
        playerlabelvar.set("It's the Player's turn")
        board[2][2]='O'
        turns = turns + 1
    win_check()
    

def win_check():
    """
    Ellenőrzi, hogy nyert e az egyik játékos

    return: True ha egy játékos nyert
    """

    if (
    board[0][0] == board[0][1] == board[0][2] == "X" or board[1][0] == board[1][1] == board[1][2] == "X" or board[2][0] == board[2][1] == board[2][2] == "X" or
    board[0][0] == board[1][0] == board[2][0] == "X" or board[0][1] == board[1][1] == board[2][1] == "X" or board[0][2] == board[1][2] == board[2][2] == "X" or 
    board[0][0] == board[1][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X"): 
        winwindow("Player 1 won")
        return True
    elif (
    board[0][0] == board[0][1] == board[0][2] == "O" or board[1][0] == board[1][1] == board[1][2] == "O" or board[2][0] == board[2][1] == board[2][2] == "O" or
    board[0][0] == board[1][0] == board[2][0] == "O" or board[0][1] == board[1][1] == board[2][1] == "O" or board[0][2] == board[1][2] == board[2][2] == "O" or 
    board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O"):
        winwindow("The AI won")
        return True
    elif turns >= 9:
        winwindow("ITS A TIE")
        return True

def winwindow(winner):
    """
    A nyertest kiíró ablak

    param winner: A nyertes játékos
    """

    global wwindow

    wwindow = tk.Toplevel(windowrandom)
    wwindow.title("This is the winner window")
    wlabel = tk.Label(wwindow,text="THE WINNER IS:")
    wlabel.grid(row=0, column=1)
    wlabel2 = tk.Label(wwindow,text=winner)
    wlabel2.grid(row=1,column=1)
    wbutton = tk.Button(wwindow,text='Leave Game',command=windowrandom.destroy)
    wbutton.grid(row=2,column=1)
    wbutton2 = tk.Button(wwindow,text='Return to Menu',comman=windowrandom.destroy)
    wbutton2.grid(row=2,column=2)

## Változók
turns = 0
board = np.array([
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9']])

def main():
    """
    Játék grafikája

    global variables: windowrandom, b1-b9, playerlabelvar, var
    """
    global windowrandom
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global playerlabelvar
    global var


    windowrandom = tk.Tk()
    windowrandom.resizable(True,True)
    windowrandom.title("A fun game of Tic Tac Toe with a randomized AI")

    playerlabelvar = StringVar()
    playerlabelvar.set("Player: 1(X)")
    var = StringVar()
    var.set("The game begins!")


    player_label = tk.Label(windowrandom, textvariable = playerlabelvar, font=('Times', 15))
    player_label.grid(row=0,column=0)

    turn_label = tk.Label(windowrandom, textvariable = var,  font=('Times', 15))
    turn_label.grid(row=4,column=1)

    quit_button = tk.Button(windowrandom, text="Quit Game", font=('Times', 15), command=quit)
    quit_button.grid(row=0,column=2)

    b1 = tk.Button(windowrandom,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'), command=lambda: random_turn_change(b1,0,0) )
    b2 = tk.Button(windowrandom,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'), command=lambda: random_turn_change(b2,0,1) )
    b3 = tk.Button(windowrandom,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'), command=lambda: random_turn_change(b3,0,2) )
    b4 = tk.Button(windowrandom,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'), command=lambda: random_turn_change(b4,1,0) )
    b5 = tk.Button(windowrandom,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'), command=lambda: random_turn_change(b5,1,1) )
    b6 = tk.Button(windowrandom,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'), command=lambda: random_turn_change(b6,1,2) )
    b7 = tk.Button(windowrandom,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'), command=lambda: random_turn_change(b7,2,0) )
    b8 = tk.Button(windowrandom,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'), command=lambda: random_turn_change(b8,2,1) )
    b9 = tk.Button(windowrandom,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'), command=lambda: random_turn_change(b9,2,2) )

    b1.grid(row=1,column=0)
    b2.grid(row=1,column=1)
    b3.grid(row=1,column=2)
    b4.grid(row=2,column=0)
    b5.grid(row=2,column=1)
    b6.grid(row=2,column=2)
    b7.grid(row=3,column=0)
    b8.grid(row=3,column=1)
    b9.grid(row=3,column=2)

    windowrandom.mainloop()

if __name__ == '__main__':
    main()