# Vytvoří seznam pěti různých čtverců pomocí cyklu.

class Ctverec():
    pocet_stran = 4

    def __init__(self, delka_strany):
        self.delka_strany = delka_strany

    def vypocitej_obvod(self):
        return self.delka_strany * self.pocet_stran

    def vypocitej_obsah(self):
        return self.delka_strany ** 2

    def __repr__(self):
        return f"<Čtverec s délkou strany {self.delka_strany} cm>"

seznam_ctvercu = []
for strana in range(1, 6):
    seznam_ctvercu.append(Ctverec(strana))
print(seznam_ctvercu)



# ---------------------------------------------------------------------
# Vytvoří třídu Ctverec s jedním atributem strana a metodami obvod(),
# obsah() a rozdil_obsahu(jiny_ctverec Ctverec), která vrátí rozdíl
# obsahů dvou čtverců - zadaného a toho, jehož metodu voláme.

class Ctverec():
    pocet_stran = 4

    def __init__(self, strana):
        self.strana = strana

    def obvod(self):
        return self.strana * self.pocet_stran

    def obsah(self):
        return self.strana ** 2

    def rozdil_obsahu(self, jiny_ctverec):
        return jiny_ctverec.obsah() - self.obsah()

strana1 = 10
strana2 = 15
prvni_ctverec = Ctverec(strana1)
druhy_ctverec = Ctverec(strana2)

print(f"Rozdíl obsahů čtverců se stranami {strana2} cm a {strana1} \
cm je {prvni_ctverec.rozdil_obsahu(druhy_ctverec)} cm2.")



# ---------------------------------------------------------------------
# Vytvoří vlastní třídu pro celá čísla tak, aby tato nová třída
# měla všechny vlastnosti a schopnosti běžných celých čísel v Pythonu
# (objekty bude možné sčítat, odečítat, porovnávat atp.) a navíc měla
# metodu pro rozpoznání, zda je číslo v objektu sudé nebo liché jménem
# je_sude(), která bude vracet True nebo False.

class Moje_cela_cisla(int):
    def je_sude(self):
        if self % 2 == 0:
            return True
        else:
            return False

cislo1 = Moje_cela_cisla(4)
print(f"Je číslo {cislo1} sudé? {cislo1.je_sude()}")
cislo2 = Moje_cela_cisla(5)
print(f"Je číslo {cislo2} sudé? {cislo2.je_sude()}")