from tkinter import *
from sqlite3 import *

master = Tk()
master.title("Inventura") 
master.geometry('450x500+0+0')
background_image = PhotoImage(file = "1.gif")
background_label = Label(master, image = background_image)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

L1 = Label(master, text = "Vrsta proizvoda", font = ("ms serif", 16)).place(x = 10,y = 10)
L2 = Label(master, text = "Količina", font = ("ms serif", 16)).place(x = 10,y = 60)
L3 = Label(master, text = "Cijena", font = ("ms serif", 16)).place(x = 10,y = 110)
L4 = Label(master, text = "Vrijednost", font = ("ms serif", 16)).place(x = 10,y = 160)

vrsta_proizvoda = Entry(master, bd = "3")
vrsta_proizvoda.place(x = 250, y = 10)

kolicina = Entry(master, bd = "3")
kolicina.place(x = 250, y = 60)

cijena = Entry(master, bd = "3")
cijena.place(x = 250, y = 110)

vrijednost = Entry(master, bd="3")
vrijednost.place(x = 250, y = 160)

frame = Frame(master)
frame.place(x= 40, y = 260)
           
Lb = Listbox(frame, height = 9, width = 40, font = ("times new roman", 12)) 
Lb.pack(side = LEFT, fill = Y)
            
scroll = Scrollbar(frame, orient = VERTICAL)
scroll.config(command = Lb.yview)
scroll.pack(side = RIGHT, fill = Y)
Lb.config(yscrollcommand = scroll.set) 

con = connect('inventura.db') 
c = con.cursor()

c.execute('CREATE TABLE IF NOT EXISTS inventura1 (vrsta_proizvoda TEXT, kolicina INTEGER, cijena FLOAT, vrijednost TEXT)')

def dodaj_proizvod():
        c.execute('INSERT INTO inventura1 (vrsta_proizvoda, kolicina, cijena, vrijednost) VALUES (?, ?, ?, ?)',
                  (vrsta_proizvoda.get(), kolicina.get(), cijena.get(), vrijednost.get()))
        con.commit()

        vrsta_proizvoda.delete(0, END)
        kolicina.delete(0, END)
        cijena.delete(0, END)
        vrijednost.delete(0, END)

def izbrisi_proizvod():
        c.execute("DELETE FROM inventura1 WHERE vrsta_proizvoda = '" + vrsta_proizvoda.get() + "'")
        
        con.commit()

        vrsta_proizvoda.delete(0, END)
        kolicina.delete(0, END)
        cijena.delete(0, END)
        vrijednost.delete(0, END)

def pretrazi_proizvod():
        c.execute('SELECT vrsta_proizvoda FROM inventura1 WHERE vrsta_proizvoda = ?', (vrsta_proizvoda.get(),))
        if c.fetchone():
            L5 = Label(master, text="Artikl pronađen", font=("times new roman",10, "bold"), fg="blue", width= 16).place(x = 75, y = 203)
        else:
            L5 = Label(master, text="Artikl nije pronađen", font=("times new roman",10, "bold"), fg="red").place(x = 75, y = 203)

        a = c.execute('SELECT * FROM inventura1 WHERE vrsta_proizvoda LIKE (?)', (vrsta_proizvoda.get(),))
        podaci = c.fetchall()
        for a in podaci:
                Lb.insert(1,a)

        con.commit()

vrsta_proizvoda.delete(0, END)
kolicina.delete(0, END)
cijena.delete(0, END)
vrijednost.delete(0, END)
        
def ispis():
        c.execute('SELECT * FROM inventura1')
        podaci = c.fetchall()
            
        for row in podaci:
                Lb.insert(1,row)         

        con.commit()

gumb1 = Button(master, text = "Dodaj",command = dodaj_proizvod, font = ("times new roman", 10))
gumb1.place(x = 200, y = 200)

gumb2 = Button(master, text = "Pretraži",command = pretrazi_proizvod, font = ("times new roman", 10))
gumb2.place(x = 250, y = 200)

gumb3 = Button(master, text = "Izbriši",command = izbrisi_proizvod, font = ("times new roman", 10))
gumb3.place(x = 306, y = 200)

gumb4 = Button(master, text = "Ispis artikala iz baze podataka", command = ispis, font = ("times new roman", 10))
gumb4.place(x = 130, y = 455)


master.mainloop()
c.close()
con.close()