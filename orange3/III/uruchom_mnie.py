import dom as d1
import dom2 as d2
import dom3 as d3
import ptak as p
import ptak2 as p2

# dom_1 = dom.Dom()
# print(dom_1.__czy_ma_basen)
# dom_1.buduj_basen()
# print(dom_1.__czy_ma_basen)
# dom_1.maluj_dom()
# dom_1.wstaw_okna()
# print(dom_1.__kolor)

# dom_2 = d1.Dom()
# dom_2.maluj_dom()
# dom_2.wstaw_okna()
# dom_2.kolor = [5, 3, 56, 34, 3, 4, 5]
# dom_2.ilosc_okien = -23
# print(dom_2.kolor)
# print(dom_2.ilosc_okien)
#
# dom_3 = d2.Dom("zielony", 4)
# print(dom_3.kolor)
# print(dom_3.czy_ma_basen)
# dom_3.maluj_dom()
# dom_3.wstaw_okna()
# dom_3.ilosc_okien = "nie ma okien"
# print(dom_3.ilosc_okien)
#
# dom_4 = d3.Dom("czerwony", 5, True)
# dom_4.maluj_dom()
# dom_4.wstaw_okna()

henia = p.Kura("kura", 1)
henia.wydajOdglos()
henia.lataj()
henia.idz_na_rosol()

orzel = p.Ptak('orzeł', 20)
orzel.wydajOdglos()
orzel.lataj()

kura2 = p2.Kura('kura2')
kura2.lataj()

pingwin = p2.Pingwin("pingwin")
pingwin.lataj()
pingwin.wydajOdglos()

print(pingwin.formatowanie())
print(p2.Pingwin("pingwin2").formatowanie())