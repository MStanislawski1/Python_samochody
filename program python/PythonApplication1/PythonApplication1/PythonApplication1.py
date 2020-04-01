import sys #do zamykania opcją "0"
import os #do clearowania konsoli

class Samochod: #klasa przechowująca dane jednego samochodu
    def __init__(self, data_string):#funkcja init, która wczytuje dane samochodu
        tmp_l=data_string.split("|")
        self.numer=tmp_l[0]
        self.marka=tmp_l[1]
        self.model=tmp_l[2]
        self.rok=tmp_l[3]
        self.pojemnosc=tmp_l[4]
        self.przebieg=tmp_l[5]
        self.typ=tmp_l[6]

    def wyswietl(self):#funkcja która wyświetla parametry samochodu
        print("Numer samochodu: "+self.numer)
        print("Marka: "+self.marka)
        print("Model: "+self.model)
        print("Rocznik: "+self.rok)                                 #parametry samochodu
        print("Pojemność: "+self.pojemnosc)
        print("Przebieg: "+self.przebieg)
        print("Rodzaj skrzyni biegów: "+self.typ)

    def przygotowanie_zapisu(self):#zwraca format w którym nastąli zapis
        return (self.numer+"|"+self.marka+"|"+self.model+"|"+self.rok+"|"+self.pojemnosc+"|"+self.przebieg+"|"+self.typ)


def wczytaj_katalog(nazwa_pliku):#funkcja wczytująca bazę samochodów
    f=open(nazwa_pliku,"r")
    lines=f.readlines()
    samochod_lista=[] #tablica do której zalisywane są wartości z pliku
    for line in lines:
        if line!="\n":
            samochod_lista.append(Samochod(line[0:-1]))
    f.close()
    return samochod_lista

def zapis(nazwa_pliku, samochod_lista): #funkcja, która zapisuje dane z powyższej tablicy w bazie
    f=open(nazwa_pliku, "w")
    for samochod in samochod_lista:
        f.write(samochod.przygotowanie_zapisu())
        f.write("\n") #przejście do kolejnej linii, aby dane nie były w jednym ciągu
    f.close()

def wyswietl_warunek(wybor,samochod_lista, wartosc): #funkcja wyświetlająca warunkowo parametry samochodów, które są wartością liczbową, np. przebieg
   
    print("\n")
    print("Jaki samochód checesz wyświtlić ?")
    print("1. o wartości mniejszej od podanej")
    print("2. o wartości większej od podanej")
    print("3. o wartości równej wartości podanej")
    wybor_limit=input()
    if wybor_limit=='1':       #kiedy chcemy wyświetlić auta o parametrach mniejszych od "wartosc"
        if wybor == '3':       #wyświetlanie roczników
            for samochod in samochod_lista:
                if int(samochod.rok)<int(wartosc):
                    print(samochod.numer)
        elif wybor == '4':     #wyświetlanie pojemności
            for samochod in samochod_lista:
                if float(samochod.pojemnosc) < float(wartosc):
                    print(samochod.numer)
        elif wybor == '5':     #wyświetlanie przebiegu 
            for samochod in samochod_lista:
                if int(samochod.przebieg) < int(wartosc):
                    print(samochod.numer)
    elif wybor_limit=='2':     #kiedy chcemy wyświetlić auta o parametrach większych od "wartosc"
        if wybor == '3':       #wyświetlanie roczników
            for samochod in samochod_lista:
                if int(samochod.rok)>int(wartosc):
                    print(samochod.numer)
        elif wybor == '4':     #wyświetlanie pojemności
            for samochod in samochod_lista:
                if float(samochod.pojemnosc) > float(wartosc):
                    print(samochod.numer)
        elif wybor == '5':     #wyświetlanie przebiegów
            for samochod in samochod_lista:
                if int(samochod.przebieg) > int(wartosc):
                    print(samochod.numer)
    elif wybor_limit=='3':     #kiedy chcemy wyświetlić auta o parametrach równych "wartosc"
        if wybor == '3':       #wyświetlanie roczników
            for samochod in samochod_lista:
                if int(samochod.rok)==int(wartosc):
                    print(samochod.numer)
        elif wybor == '4':     #wyświetlanie pojemności
            for samochod in samochod_lista:
                if float(samochod.pojemnosc) == float(wartosc):
                    print(samochod.numer)
        elif wybor == '5':     #wyświetlanie przebiegów
            for samochod in samochod_lista:
                if int(samochod.przebieg) == int(wartosc):
                    print(samochod.numer)


def sortuj(sortuj_atrybut, sortuj_sposob): #wyświtla posortowaną listę według parametru sortuj_atrybut, sortuj_sposob ustala porządek: 0-rosnąco, 1-malejąco
    if sortuj_sposob=="1" or sortuj_sposob=="0":
        sposob=int(sortuj_sposob)
        if sortuj_atrybut=="1":
            samochod_sortuj_lista=sorted(samochod_lista, key= lambda samochod: samochod.marka, reverse=sposob)
        elif sortuj_atrybut=="2":
            samochod_sortuj_lista=sorted(samochod_lista, key= lambda samochod: samochod.model, reverse=sposob)
        elif sortuj_atrybut=="3":
            samochod_sortuj_lista=sorted(samochod_lista, key= lambda samochod: samochod.rocznik, reverse=sposob)
        elif sortuj_atrybut=="4":
            samochod_sortuj_lista=sorted(samochod_lista, key= lambda samochod: samochod.pojemnosc, reverse=sposob)
        elif sortuj_atrybut=="5":
            samochod_sortuj_lista=sorted(samochod_lista, key= lambda samochod: samochod.przebieg, reverse=sposob)
        elif sortuj_atrybut=="6":
            samochod_sortuj_lista=sorted(samochod_lista, key= lambda samochod: samochod.typ, reverse=sposob)
    for samochod in samochod_sortuj_lista:
        print(samochod.numer)


samochod_lista=[]#lista obiektów Samochod, przechowuje wszystkie dane katalogu

print ('Porada: Aby wyświetlić katalog, musisz najpierw załadowac bazę, wybierając opcję 1. z MENU GŁÓWNEGO')
print("\n") 
arg=True
while arg: #nieskończona pętla wyświetlająca menu
    print("             MENU GŁÓWNE")
    print("------------------------------------------")
    print("1. Wczytaj bazę samochodów")
    print("2. Dodaj samochód")
    print("3. Wyświetl wszystkie samochody")
    print("4. Usuń samochód")
    print("5. Wyświetl dane wybranego samochodu")
    print("6. Wyświetl listę samochodów pod warunkiem")
    print("7. Posortuj samochody po parametrze")
    print("8. Zapisz katalog")
    print("0. Wyjdź")
    wybor=str(input())     #wybór opcji z menu

    if wybor=="1":
        #clearowanie i "przytrzymane" funkcji jest analogiczne w każdej z nich
        os.system('CLS')#wyclearowanie menu
        nazwa_pliku="baza.txt"
        samochod_lista=wczytaj_katalog(nazwa_pliku)
        print ("Baza została załadowana!\n")
        print ("Aby kontynuować naciśnij enter...")
        x=input() #"przytrzymane" wyśietlanego tekstu
        os.system('CLS') #wyclearowanie zawartości funkcji
    elif wybor=="2":           
        os.system('CLS')
        print ('Podaj dane samochodu, który checesz dodać')
        print ('Schemat: numer|marka|model|rocznik|pojemność|przebieg|rodzaj_skrzyni_biegów')
        dodaj_wartosc=input()
        samochod_lista.append(Samochod(dodaj_wartosc)) #dodanie samochodu do tablicy
        print("Podany samochód został dodany.")
                
        print ("Aby kontynuować naciśnij enter...")
        x=input()
        os.system('CLS')

    elif wybor=="3":   
        os.system('CLS')
        for samochod in samochod_lista:
            samochod.wyswietl()
            print("\n") 
        print ("Aby kontynuować naciśnij enter...")
        x=input()
        os.system('CLS')
    elif wybor=="4":           
        print ("Wybrałeś opcję usunięcia sammochochodu!")
        print('')
        print("Podaj ID samochodu, który chcesz usunąć: ")
        a=input()
        print('')
        print('')
        counter =1 
        with open('baza.txt', 'r') as f:
            lines = f.readlines()

        with open ('baza.txt', 'w') as f:
            for line in lines:
                if counter != int(a):
                    f.write(line)
                counter += 1
        print ("Aby kontynuować naciśnij enter...")
        x=input()
        os.system('CLS')
    
    elif wybor=="5":                           
        print("Podaj numer samochodu, którego dane chcesz wyświetlić: ")
        wybor_numer=input()
        for samochod in samochod_lista:
            if(samochod.numer==wybor_numer):
                samochod.wyswietl()
        
        print ("Aby kontynuować naciśnij enter...")
        x=input()
        os.system('CLS')
    
    

    elif wybor=="6":
        os.system('CLS')
        print("\n")
        print("Wyświetl według:")
        print("1. Marka")
        print("2. Model")
        print("3. Rocznik")
        print("4. Pojemność")
        print("5. Przebieg")
        print("6. Rodzaj skrzyni biegów")
        wybor_parametru_warunek=input()      #wybór według czego nastąpi wyświetlenie
        print("Podaj wartość graniczną: ")
        wartosc=input()                       #podanie wartości od której mają być wyśiwetlanie dane, np. o pojemności większej niż 1200 cm^3
        os.system('CLS')
        if wybor_parametru_warunek=='3' or wybor_parametru_warunek=='4' or wybor_parametru_warunek=='5': #odwołanie do funkcji "wyswietl_warunek", jeśli wyśiwetlane dane są wartością liczbową
            wyswietl_warunek(wybor_parametru_warunek, samochod_lista, wartosc)
        elif wybor_parametru_warunek=='1':   #wyświetlenie samochodów o takiej samej marce jak wpisana
            for samochod in samochod_lista:
                if(samochod.marka==wartosc):
                    samochod.wyswietl()
                    print("\n")
        elif wybor_parametru_warunek=='2':   #wyświetlenie samochodów o takim samym modelu jak wpisany
            for samochod in samochod_lista:
                if(samochod.model==wartosc):
                    samochod.wyswietl()
                    print("\n")
        elif wybor_parametru_warunek=='6':   #wyświetlenie samochodów z takim samym typem skrzyni biegów jak wpisana
            for samochod in samochod_lista:
                if(samochod.typ==wartosc):
                    samochod.wyswietl()
                    print("\n")
        print ("Aby kontynuować naciśnij enter...")
        x=input()
        os.system('CLS')
    elif wybor=="7":
        os.system('CLS')
        print("Sortuj według: ")
        print("1. Marka")
        print("2. Model")
        print("3. Rocznik")
        print("4. Pojemność")
        print("5. Przebieg")
        print("6. Rodzaj skrzyni biegów")
        sortuj_atrybut=input()  #parametr według, którego sortujemy
        print ("(0-rosnąco,1-malejąco)")
        print("Wybierz sposób sortowania:")
        sortuj_sposob=input() #podanie jak mają być sortowane samochody
        print("\n")
        sortuj(sortuj_atrybut, sortuj_sposob)      #sortowanie i wyświetlenie posortowanej listy
        
        print ("Aby kontynuować naciśnij enter...")
        x=input()
        os.system('CLS')
    elif wybor=="8":
        os.system('CLS')
        nazwa_pliku = "baza.txt"
        zapis(nazwa_pliku,samochod_lista)
        print ("Baza została zapisana!\n")
        print ("Aby kontynuować naciśnij enter...")
        x=input()
        os.system('CLS')
    elif wybor=="0":
        os.system('CLS')
        print ("Wyjście")
        sys.exit(0)
        SystemExit: 0
    else:       
        os.system('CLS') 
        print ("W menu nie ma takiej opcjii, musiałeś coś źle nacisnąć!")
        x=input()
        print ("Aby kontynuować naciśnij enter...")
        os.system('CLS') 


