#Lav et tekstbaseret “sten-saks-papir”-spil.

valg1 = input("Sten, saks eller papir? ").lower()
valg2 = input("Sten, saks eller papir? ").lower()

if valg1 == valg2:
    print("Uafgjort!")
elif valg1 == ("sten") and valg2 == ("saks") or valg2 == ("sten") and valg1 == ("saks"):
    print("Sten vinder!")
elif valg1 == ("sten") and valg2 == ("papir") or valg2 == ("sten") and valg1 == ("papir"):
    print("Papir vinder!")
elif valg1 == ("saks") and valg2 == ("papir") or valg2 == ("saks") and valg1 == ("papir"):
    print("Saks vinder!")

