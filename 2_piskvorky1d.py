# Hra Piškvorky1d s počítačem.


from random import randrange

def tah_hrace(pole):
    while True:
        pozice = int(input("Na kterou pozici (0-19) chceš hrát? "))
        if pozice < 0 or pozice > 19:
            print("Nelze hrát mimo hrací pole.")
        elif pole[pozice] != "-":
            print("Nelze hrát na již obsazené políčko.")
        else:
            pole_s_tahem_hrace = pole[:pozice] + "x" + pole[pozice + 1:]
            return pole_s_tahem_hrace

def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače."
    while True:
        if "-oo" in pole:
            pole_s_tahem_pocitace = pole.replace("-oo", "ooo")
            return pole_s_tahem_pocitace
        elif "o-o" in pole:
            pole_s_tahem_pocitace = pole.replace("o-o", "ooo")
            return pole_s_tahem_pocitace
        elif "oo-" in pole:
            pole_s_tahem_pocitace = pole.replace("oo-", "ooo")
            return pole_s_tahem_pocitace
        elif "-xx" in pole:
            pole_s_tahem_pocitace = pole.replace("-xx", "oxx")
            return pole_s_tahem_pocitace
        elif "x-x" in pole:
            pole_s_tahem_pocitace = pole.replace("x-x", "xox")
            return pole_s_tahem_pocitace
        elif "xx-" in pole:
            pole_s_tahem_pocitace = pole.replace("xx-", "xxo")
            return pole_s_tahem_pocitace
        elif "-x-" in pole:
            pole_s_tahem_pocitace = pole.replace("-x-", "ox-")
            return pole_s_tahem_pocitace
        pozice = randrange(20)
        if pole[pozice] == "-":
            if pozice != 0 and pozice != 19:
                if pole[pozice + 1] != "-" or pole[pozice - 1] != "-":
                    pole_s_tahem_pocitace = pole[:pozice] + "o" + pole[pozice + 1:]
                    return pole_s_tahem_pocitace
            elif pozice == 0:
                if pole[pozice + 1] != "-":
                    pole_s_tahem_pocitace = pole[:pozice] + "o" + pole[pozice + 1:]
                    return pole_s_tahem_pocitace
            else:
                if pole[pozice - 1] != "-":
                    pole_s_tahem_pocitace = pole[:pozice] + "o" + pole[pozice + 1:]
                    return pole_s_tahem_pocitace

def vyhodnot(herni_pole):
    if "xxx" in herni_pole:
        return "x"
    elif "ooo" in herni_pole:
        return "o"
    elif "-" not in herni_pole:
        return "!"
    else:
        return "-"

def piskvorky1d():
    herni_pole = "-" * 20
    while True:
        herni_pole = tah_hrace(herni_pole)
        print("Herní pole s tvým tahem: ", herni_pole)
        if vyhodnot(herni_pole) == "x":
            print("Vyhrál/a jsi, gratuluji!")
            break
        elif vyhodnot(herni_pole) == "!":
            print("Remíza.")
            break
        herni_pole = tah_pocitace(herni_pole)
        print("Herní pole s tahem počítače: ", herni_pole)
        if vyhodnot(herni_pole) == "o":
            print("Počítač vyhrál.")
            break
        elif vyhodnot(herni_pole) == "!":
            print("Remíza.")
            break

piskvorky1d()
