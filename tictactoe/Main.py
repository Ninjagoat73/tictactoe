import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os

## Két változó amire majd hivatkozunk
turns = 0
board = [
        ['','',''],
        ['','',''],
        ['','','']]

def tictactoe_mp():

    """
    A más ember ellenes játék grafikája
    
    global váltaozók: window, turns, player_label
    return: játék grafika
    """

    global window
    global turns
    global player_label

    ## Megnyitjuk az ablakot
    window = tk.Toplevel(root)
    window.resizable(True,True)
    window.title("A fun game of Tic Tac Toe")

    ## Szöveget hozunk létre ami elmondja kinek a köre van
    player_label = tk.Label(window, textvariable = playerlabelvar, font=('Times', 15))
    player_label.grid(row=0,column=0)

    ## Szöveg ami megmondja hanyadik kör van
    turn_label = tk.Label(window, textvariable = var,  font=('Times', 15))
    turn_label.grid(row=4,column=1)

    ## Kilépő gomb
    quit_button = tk.Button(window, text="Quit Game", font=('Times', 15), command=quit)
    quit_button.grid(row=0,column=2)

    ## Játék mező
    b1 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: turn_change(b1,0,0))
    b2 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: turn_change(b2,0,1))
    b3 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: turn_change(b3,0,2))
    b4 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: turn_change(b4,1,0))
    b5 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: turn_change(b5,1,1))
    b6 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: turn_change(b6,1,2))
    b7 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: turn_change(b7,2,0))
    b8 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: turn_change(b8,2,1))
    b9 = tk.Button(window,text='',height=8, width=16,bg='black',activebackground='white',fg= 'white',font=('times 15'),command=lambda: turn_change(b9,2,2))

    ## Elhejezzük a gombokat
    b1.grid(row=1,column=0)
    b2.grid(row=1,column=1)
    b3.grid(row=1,column=2)
    b4.grid(row=2,column=0)
    b5.grid(row=2,column=1)
    b6.grid(row=2,column=2)
    b7.grid(row=3,column=0)
    b8.grid(row=3,column=1)
    b9.grid(row=3,column=2)

    ## Eltüntetjük a menüt
    root.withdraw()

def turn_change(b,r,c):
    """
    Kört átadja a másik játékosnak és kitölti a játék mezőt
    
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
            playerlabelvar.set("Player: 1(O)")
            board[r][c]="X"
        else:
            b['text']='O'
            playerlabelvar.set("Player: 2(X)")
            board[r][c]="O"
        ## Hozzáad egyet a körszámlálóhoz
        turns = turns + 1
        if turns >= 5:
            win_check()
    else: messagebox.showerror("Error","This box is already filled")
    ## Körszámláló kiírást megváltoztatja    
    var.set("It is turn:" + str(turns))

def win_check():
    """
    Ellenőrzi, hogy nyert e az egyik játékos

    return: winwindow() ha egy játékos nyert
    """

    if (
    board[0][0] == board[0][1] == board[0][2] == "X" or board[1][0] == board[1][1] == board[1][2] == "X" or board[2][0] == board[2][1] == board[2][2] == "X" or
    board[0][0] == board[1][0] == board[2][0] == "X" or board[0][1] == board[1][1] == board[2][1] == "X" or board[0][2] == board[1][2] == board[2][2] == "X" or 
    board[0][0] == board[1][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X"): 
        winwindow("Player 1 won")
    elif (
    board[0][0] == board[0][1] == board[0][2] == "O" or board[1][0] == board[1][1] == board[1][2] == "O" or board[2][0] == board[2][1] == board[2][2] == "O" or
    board[0][0] == board[1][0] == board[2][0] == "O" or board[0][1] == board[1][1] == board[2][1] == "O" or board[0][2] == board[1][2] == board[2][2] == "O" or 
    board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O"):
        winwindow("Player 2 won")
    elif turns >= 9:
        winwindow("ITS A TIE")

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
    wbutton = tk.Button(wwindow,text='Leave Game',command=destruct)
    wbutton.grid(row=2,column=1)
    wbutton2 = tk.Button(wwindow,text='Return to Menu',command=menureturn)
    wbutton2.grid(row=2,column=2)

def destruct():
    """
    Bezárja az applikációt
    """
    root.destroy()

def menureturn():
    """
    Újraindítja a játékot

    global variables: turns, board
    """

    global turns
    global board

    window.destroy()
    wwindow.destroy()
    root.deiconify()

    ## Reseteljük a számokat
    turns = 0
    board = [
        ['','',''],
        ['','',''],
        ['','','']]

def ai_window():
    """
    Nehézségi szint választás
    """
    global aiWindow

    aiWindow = Toplevel(root)
    randB = tk.Button(aiWindow,text='Random AI',command=runRandom)
    aiB = tk.Button(aiWindow,text='Real AI',command=runAI)

    randB.pack()
    aiB.pack()

def runRandom():
    """
    Randomizált gép elleni játék indítása
    """
    os.system('python Random.py')
    aiWindow.destroy()
def runAI():
    """
    Normál gép elleni játék indítása
    """
    os.system('python Computer.py')
    aiWindow.destroy()

def main():
    
    """
    A menü grafikája

    global variables: root, var, playerlabelvar
    """

    global root
    global var
    global playerlabelvar

    root = tk.Tk()

    ## Változók amiket majd használunk
    playerlabelvar = StringVar()
    playerlabelvar.set("Player: 1(X)")
    var = StringVar()
    var.set("The game begins!")

    ## Grafika
    intro = tk.Label(root, text= "WELCOME TO TIC TAC TOE", font=('Times', 25))
    sp_button = tk.Button(root, text="Singleplayer",font= ('Times', 25), command=ai_window)
    mp_button = tk.Button(root, text="Multiplayer",font= ('Times', 25), command=tictactoe_mp)
    menu_quit = tk.Button(root, text="Quit Game", font=('Times', 25), command=quit)

    intro.grid(row=0,column=0)
    sp_button.grid(row=1,column=0)
    mp_button.grid(row=2,column=0)
    menu_quit.grid(row=3,column=0)

    root.mainloop()

if __name__ == '__main__':
    main()