from tkinter import *

def eredmeny(lotto, sajatszamok1, sajatszamok2, sajatszamok3, sajatszamok4, sajatszamok5, genelso, genmasodik, genharmadik, gennegyedik, genotodik):
    frame6 = Frame(lotto)
    frame6.pack(side=TOP)
    label5 = Label(frame6, text="")
    label5.pack(side=LEFT)

    # tömbbé alakítás
    sajatok = [sajatszamok1.get(), sajatszamok2.get(), sajatszamok3.get(), sajatszamok4.get(), sajatszamok5.get()]
    generaltak = [genelso.get(), genmasodik.get(), genharmadik.get(), gennegyedik.get(), genotodik.get()]

    # teszt kiirás
    print(f"Végleges saját számok: {sajatok}")
    print(f"Végleges lottószámok: {generaltak}")

    db = int(0)
    for x in sajatok:
        for y in generaltak:
            if x == y:
                db = db + 1;

    frame7 = Frame(lotto)
    frame7.pack(side=TOP)
    label6 = Label(frame7, font=("Arial", 20), width=24, text="Eltalált lottószámok: " + str(db))
    label6.pack(side=LEFT)