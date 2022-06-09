# Program simuluje tuto hru:
# První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6), dokud nepadne šestka.
# Potom hází další hráč, dokud nepadne šestka i jemu. Potom hází hráč třetí a nakonec čtvrtý.
# Vyhrává ten, kdo na hození šestky potřeboval nejvíc hodů. (V případě shody vyhraje ten, kdo házel dřív.)
# Program vypisuje všechny hody a nakonec vypíše, kdo vyhrál.


from random import randrange

def hazeni(cislo_hrace):
    pocet_hodu = 0
    while True:
        pocet_hodu = pocet_hodu + 1
        hod = randrange(1, 7)
        print("Hráč číslo", cislo_hrace, "v hodu číslo", pocet_hodu, "hodil", hod)
        if hod == 6:
            print("Hráč číslo", cislo_hrace, "k hození šestky potřeboval", pocet_hodu, "hodů.")
            return pocet_hodu

pocet_hracu = int(input("Zadej počet hráčů: "))
while pocet_hracu <= 0:
    pocet_hracu = int(input("Číslo musí být kladné. Zadej počet hráčů: "))

pocet_hodu_viteze = 0

for hrac in range(1, pocet_hracu + 1):
    pocet_hodu_do_sestky = hazeni(hrac)
    if pocet_hodu_viteze < pocet_hodu_do_sestky:
        pocet_hodu_viteze = pocet_hodu_do_sestky
        vitez = hrac

print("Vyhrál hráč číslo", vitez, "s", pocet_hodu_viteze, "hody potřebnými k hození šestky.")