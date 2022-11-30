import random
from tkinter import *
from tkinter import messagebox

def sorsolas():
    button1["state"] = DISABLED
    sajatelsoseged.set(sajatszamok1.get())
    sajatmasodikseged.set(sajatszamok2.get())
    sajatharmadikseged.set(sajatszamok3.get())
    sajatnegyedikseged.set(sajatszamok4.get())
    sajatotodikseged.set(sajatszamok5.get())
    if (sajatelsoseged.get() == sajatmasodikseged.get() or sajatelsoseged.get() == sajatharmadikseged.get() or sajatelsoseged.get() == sajatnegyedikseged.get() or sajatelsoseged.get() == sajatotodikseged.get() or sajatmasodikseged.get() == sajatharmadikseged.get() or sajatmasodikseged.get() == sajatnegyedikseged.get() or sajatmasodikseged.get() == sajatotodikseged.get() or sajatharmadikseged.get() == sajatnegyedikseged.get() or sajatharmadikseged.get() == sajatotodikseged.get() or sajatnegyedikseged.get() == sajatotodikseged.get() or sajatelsoseged.get() == "" or sajatmasodikseged.get() == "" or sajatharmadikseged.get() == "" or sajatnegyedikseged.get() == "" or sajatotodikseged.get().isdigit() == FALSE or sajatnegyedikseged.get().isdigit() == FALSE or sajatharmadikseged.get().isdigit() == FALSE or sajatmasodikseged.get().isdigit() == FALSE or sajatelsoseged.get().isdigit() == FALSE):
        messagebox.showwarning("Hiba!", "Hibás értékek!")
        exit()
    sajatszamok1["state"] = DISABLED
    sajatszamok2["state"] = DISABLED
    sajatszamok3["state"] = DISABLED
    sajatszamok4["state"] = DISABLED
    sajatszamok5["state"] = DISABLED

    a = TRUE
    while a == TRUE:
        seged1 = random.randint(1, 90);
        seged2 = random.randint(1, 90);
        seged3 = random.randint(1, 90);
        seged4 = random.randint(1, 90);
        seged5 = random.randint(1, 90);
        segedosszes = [seged1, seged2, seged3, seged4, seged5]
        print(segedosszes)
        if (seged1 == seged2 or seged1 == seged3 or seged1 == seged4 or seged1 == seged5 or seged2 == seged3 or seged2 == seged4 or seged2 == seged5 or seged3 == seged4 or seged3 == seged5 or seged4 == seged5):
            a = TRUE
        else:
            a = FALSE

    genelso.set(seged1)
    genmasodik.set(seged2)
    genharmadik.set(seged3)
    gennegyedik.set(seged4)
    genotodik.set(seged5)

    frame4 = Frame(lotto)
    frame4.pack(side=TOP)
    label3 = Label(frame4, text="")
    label3.pack(side=LEFT)

    frame5 = Frame(lotto)
    frame5.pack(side=TOP)
    label4 = Label(frame5, font=("Arial", 20), width=26, text="A nyertes Lottószámok:")
    label4.pack(side=LEFT)
    genszamok1 = Entry(frame5, textvariable=genelso, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                       width=3, state=DISABLED)
    genszamok1.pack(side=LEFT)
    genszamok2 = Entry(frame5, textvariable=genmasodik, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                       width=3, state=DISABLED)
    genszamok2.pack(side=LEFT)
    genszamok3 = Entry(frame5, textvariable=genharmadik, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                       width=3, state=DISABLED)
    genszamok3.pack(side=LEFT)
    genszamok4 = Entry(frame5, textvariable=gennegyedik, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                       width=3, state=DISABLED)
    genszamok4.pack(side=LEFT)
    genszamok5 = Entry(frame5, textvariable=genotodik, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                       width=3, state=DISABLED)
    genszamok5.pack(side=LEFT)

    eredmeny()

def eredmeny():
    frame6 = Frame(lotto)
    frame6.pack(side=TOP)
    label5 = Label(frame6, text="")
    label5.pack(side=LEFT)

    db = int(0)
    #teszt kiirás
    print(sajatelsoseged.get() + sajatmasodikseged.get() + sajatharmadikseged.get() + sajatnegyedikseged.get() + sajatotodikseged.get())

    sajatok = [sajatelsoseged.get(), sajatmasodikseged.get(), sajatharmadikseged.get(), sajatnegyedikseged.get(), sajatotodikseged.get()]
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

# ablak létrehozása és paraméterezése
lotto = Tk()
lotto.geometry('1000x400')
frame = Frame(lotto)
frame.pack()
lotto.title("Ötöslottó");

# lottószámok változói
genelso = StringVar()
genmasodik = StringVar()
genharmadik = StringVar()
gennegyedik = StringVar()
genotodik = StringVar()

# sajátszámok változói
sajatelso = StringVar()
sajatmasodik = StringVar()
sajatharmadik = StringVar()
sajatnegyedik = StringVar()
sajatotodik = StringVar()

#segedsajat
sajatelsoseged = StringVar()
sajatmasodikseged = StringVar()
sajatharmadikseged = StringVar()
sajatnegyedikseged = StringVar()
sajatotodikseged = StringVar()

frame1 = Frame(lotto)
frame1.pack(side=TOP)
label1 = Label(frame1, font=("Arial", 20), width=26, text="Kérem adja meg a számait! (1-90):")
label1.pack(side=LEFT)

sajatszamok1 = Entry(frame1, textvariable=sajatelso, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok1.pack(side=LEFT)
sajatszamok2 = Entry(frame1, textvariable=sajatmasodik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok2.pack(side=LEFT)
sajatszamok3 = Entry(frame1, textvariable=sajatharmadik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok3.pack(side=LEFT)
sajatszamok4 = Entry(frame1, textvariable=sajatnegyedik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok4.pack(side=LEFT)
sajatszamok5 = Entry(frame1, textvariable=sajatotodik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok5.pack(side=LEFT)

frame2 = Frame(lotto)
frame2.pack(side=TOP)
label2 = Label(frame2, text="")
label2.pack(side=LEFT)

frame3 = Frame(lotto)
frame3.pack(side=TOP)
button1 = Button(frame3, padx=8, width=10, pady=2, bd=8, font=("Arial", 26), text="SORSOLÁS", command=sorsolas)
button1.pack(side=TOP)

lotto.mainloop()