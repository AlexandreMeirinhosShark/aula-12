from time import sleep
from turtle import *
from random import randint


def translate(a):
    if a == 1:
        return "Pedra"
    if a == 2:
        return "Papel"
    if a == 3:
        return "Tesoura"
def draw_rock():
    seth(180)
    fd(30)
    seth(350)
    fillcolor("#737373")
    begin_fill()
    for i in range(10):
        fd(15)
        lt(3)
    lt(42)
    fd(15)
    lt(45)
    for i in range(10):
        fd(6)
        lt(2)
    lt(30)
    for i in range(5):
        fd(5)
        lt(2)
    lt(25)
    fd(20)
    rt(30)
    fd(20)
    lt(15)
    fd(15)
    lt(17)
    fd(30)
    rt(17)
    fd(10)
    seth(180)
    lt(30)
    for i in range(5):
        fd(5)
        lt(2)
    lt(30)
    for i in range(10):
        fd(6)
        lt(2)
    lt(72)
    fd(20)
    end_fill()
    pu()
    seth(0)
    lt(45)
    fd(50)
    rt(50)
    pencolor("#525252")
    pensize(3)
    pd()
    fd(40)
    lt(120)
    pu()
    fd(20)
    rt(100)
    pd()
    fd(30)
    pensize(1)
def draw_paper():
    fillcolor("#FFFFFF")
    speed(10)
    begin_fill()
    seth(10)
    fd(100)
    lt(90)
    fd(140)
    lt(90)
    fd(100)
    lt(90)
    fd(140)
    end_fill()
    lt(100)
    pu()
    fd(9)
    for i in range(9):
        pu()
        fd(81)
        lt(170)
        pd()
        fd(80)
        rt(170)
def draw_scissors():
    seth(0)
    speed(8)
    for i in range(2):
        pencolor("#2b1809")
        fillcolor("#2b1809")
        pensize(13)
        circle(22)
        pensize(1)
        pencolor("#000000")
        pu()
        lt(60)
        fd(55)
        lt(120)
        fd(15)
        rt(90)
        pensize(1)
        pd()
        fillcolor("#999999")
        begin_fill()
        fd(65)
        lt(90)
        fd(25)
        lt(90)
        fd(65)
        end_fill()
        bk(65)
        begin_fill()
        lt(170)
        fd(70)
        rt(160)
        fd(70)
        end_fill()
        seth(0)
        rt(150)
        pu()
        fd(110)
        lt(90)
        fd(20)
        pd()
        fillcolor("#000002")
def finale(b, tie=False):
    pd()
    if b == 1:
        draw_rock()
    elif b == 2:
        draw_paper()
    elif b == 3:
        draw_scissors()
    pencolor("#000000")
    pu()
    setpos(0, -100)
    if not tie:
        write("WINS!", False, "center", ("Arial", 60, "bold"))
    elif tie:
        write("TIED", False, "center", ("Arial", 60, "bold"))
    pd()
def comp_print(text, skips=1):
    for a in str(text):
        print(a, end="")
        sleep(0.05)
    if skips > 0:
        for b in range(int(skips)):
            print()


comp_print("Bem-vindo ao jogo de Pedra Papel Tesoura.", 1)
draw_scissors()
sleep(1)
home()
clear()
draw_paper()
sleep(1)
home()
clear()
draw_rock()
sleep(1)
clear()
check = ["Who wins:"]
pguess = 1
while True:
    comp_print("Escolhe a tua jogada:", 1)
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")
    print()
    comp_print("A tua escolha:", 0)
    cguess = randint(1, 3)
    try:
        pguess = int(input())
    except ValueError:
        print("Tem que ser um múmero entre 1 e 3. Tente novamente.")
        pguess = 0
    comp_print(f"A escolha do computador:{cguess}", 1)
    check.append(pguess)
    check.append(cguess)
    if 1 <= pguess <= 3:
        pu()
        setpos(-200, -50)
        pd()
        if pguess == 1:
            draw_rock()
        elif pguess == 2:
            draw_paper()
        elif pguess == 3:
            draw_scissors()
        pu()
        home()
        pencolor("#000000")
        write("VS", False, "center", ("Arial", 20, "bold"))
        setpos(170, -50)
        pd()
        if cguess == 1:
            draw_rock()
        elif cguess == 2:
            draw_paper()
        elif cguess == 3:
            draw_scissors()
        pu()
        sleep(0.5)
        clear()
        home()

        comp_print("Resultado: ", 0)

        if check == ["Who wins:", 1, 3]:
            finale(pguess)
            comp_print("Ganhaste! Pedra gannha de Tesoura.", 1)
        elif check == ["Who wins:", 3, 1]:
            finale(cguess)
            comp_print("Perdeste. Pedra ganha de Tesoura.", 1)
        if check == ["Who wins:", 3, 2]:
            finale(pguess)
            comp_print("Ganhaste! Tesoura ganha de Papel.", 1)
        elif check == ["Who wins:", 2, 3]:
            finale(cguess)
            comp_print("Perdeste. Tesoura ganha de Papel.", 1)
        if check == ["Who wins:", 2, 1]:
            finale(pguess)
            comp_print("Ganhaste! Papel ganha de Pedra.", 1)
        elif check == ["Who wins:", 1, 2]:
            finale(cguess)
            comp_print("Perdeste. Papel ganha de Pedra.", 1)
        if pguess == cguess:
            finale(pguess, True)
            comp_print(f"Empate. {translate(pguess)} não tem efeito contra si mesmo.", 1)
    else:
        comp_print("Tem que ser um número entre 1 e 3. Tente novamente.", 1)
    check.remove(pguess)
    check.remove(cguess)
    clear()