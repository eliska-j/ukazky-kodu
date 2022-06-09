# Simulace skautské hry „Kdo? S kým? Co dělali?“.
# Hra se hráče zeptá postupně na různé otázky, například „Kdo?“, „S kým?“,
# „Co dělali?“, „Kde?“, „Kdy?“, a nakonec „Proč?“, s tím, že mu umožní na
# jednu otázku odpovědět vícekrát a všechny odpovědi si uloží. Na závěr
# pak hra z každé sady odpovědí vybere náhodně jednu odpověď a z takto
# vybraných odpovědí složí větu, kterou vypíše uživateli.


from random import choice

def pta_se_uzivatele():
    otazky = ("Kdo", "S kým", "Co dělali", "Kde", "Kdy", "Proč")
    pocet_variant = 3
    slovnik_odpovedi = {}
    for otazka in otazky:
        slovnik_odpovedi[otazka] = []
        for i in range(pocet_variant):
            odpoved = input(otazka + "? ")
            odpoved = odpoved.strip()
            slovnik_odpovedi[otazka].append(odpoved)
    return slovnik_odpovedi

def slozi_a_vypise_vetu():
    odpovedi = pta_se_uzivatele()
    veta = ""
    for klic in odpovedi:
        vybrany_text = choice(odpovedi[klic]) + " "
        veta = veta + vybrany_text
    veta = veta[0].upper() + veta[1:].rstrip() + "."
    print(veta)

slozi_a_vypise_vetu()