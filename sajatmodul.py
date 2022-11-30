from tkinter import *

def eredmeny(lotto, sajatelsoseged, sajatmasodikseged, sajatharmadikseged, sajatnegyedikseged, sajatotodikseged, genelso, genmasodik, genharmadik, gennegyedik, genotodik):
    frame6 = Frame(lotto)
    frame6.pack(side=TOP)
    label5 = Label(frame6, text="")
    label5.pack(side=LEFT)

    db = int(0)
    # teszt kiirás
    print(
        sajatelsoseged.get() + sajatmasodikseged.get() + sajatharmadikseged.get() + sajatnegyedikseged.get() + sajatotodikseged.get())

    sajatok = [sajatelsoseged.get(), sajatmasodikseged.get(), sajatharmadikseged.get(), sajatnegyedikseged.get(),
               sajatotodikseged.get()]
    generaltak = [genelso.get(), genmasodik.get(), genharmadik.get(), gennegyedik.get(), genotodik.get()]
    # teszt kiirás
    print(sajatok)
    print(generaltak)

    for x in sajatok:
        for y in generaltak:
            if x == y:
                db = db + 1;

    frame7 = Frame(lotto)
    frame7.pack(side=TOP)
    label6 = Label(frame7, font=("Arial", 20), width=24, text="Eltalált lottószámok: " + str(db))
    label6.pack(side=LEFT)