'''
Created on 20.09.2012.

@author: Aleksandar
'''
import korisnici
import knjige
import racun

def main():
    print()
    print("Dobrodosli u knjizaru")
    print("======================")
    print()
    if not login():
        print()
        print("\nNiste uneli postojece ime i lozinku!")
        return
    komanda = "0"
    while komanda != "X":
        komanda = mainMenu()
        if komanda == "1":
            findBook()
        elif komanda == "2":
            searchBooks()
        elif komanda == "3":
            sortBooks()
        elif komanda == "4":
            editBook()
        elif komanda == "5":
            addBook()
        elif komanda == "6":
            sellBook()
    print()
    print("Dovidjenja")
    
def mainMenu():
    printMainMenu()
    command = input(">> ")
    while command.upper() not in ("0","1","2","3","4","5","6","X"):
        print()
        print("\nUneli ste pogresnu komandu.\n")
        printMainMenu()
        command = input(">> ")
    return command.upper()


def searchMenu():
    printSearchMenu()
    command = input(">> ")
    while command.upper() not in ("0","1","2","3","4","X"):
        print()
        print("\nUneli ste pogresnu komandu.\n")
        printSearchMenu()
        command = input(">> ")
    return command.upper()

def sortMenu():
    printSortMenu()
    command = input(">> ")
    while command.upper() not in ("0","1","2","3","X"):
        print()
        print("\nUneli ste pogresnu komandu.\n")
        printSortMenu()
        command = input(">> ")
    return command.upper()

def editMenu():
    printEditMenu()
    command = input(">> ")
    while command.upper() not in ("0","1","2","X"):
        print()
        print("\nUneli ste pogresnu komandu.\n")
        printEditMenu()
        command = input(">> ")
    return command.upper()

def sellMenu():
    printSellMenu()
    command = input(">> ")
    while command.upper() not in ("0","1","2","X"):
        print()
        print("\nUneli ste pogresnu komandu.\n")
        printSellMenu()
        command = input(">> ")
    return command.upper()

def printMainMenu():
    print("\nIzaberite opciju:")
    print()
    print("  1 - Pronalazenje knjiga po identifikatoru")
    print("  2 - Pretrazivanje knjiga")
    print("  3 - Pregled svih knjiga")
    print("  4 - Izmena knjige")
    print("  5 - Dodaj novu knjigu")
    print("  6 - Prodaj knjigu")
    print("  x - Izlaz iz programa")
    print()
    
def login():
    username = input("Korisnicko ime >> ")
    password = input("Lozinka >> ")
    return korisnici.login(username, password)

def printSearchMenu():
    print("\nIzaberite opciju pretrazivanja:")
    print()
    print("  1 - Pretrazivanje knjiga po naslovu")
    print("  2 - Pretrazivanje knjiga po autorima")
    print("  3 - Pretrazivanje knjiga po izdavacu")
    print("  4 - Pretrazivanje knjiga po godini izdanja")
    print("  x - Vrati se nazad")
    print()
    
def printSortMenu():
    
    print("\nIzaberite opciju pregleda knjiga:")
    print()
    print("  1 - Pregled knjiga sortiranih po ceni")
    print("  2 - Pregled knjiga sortiranih po autorima")
    print("  3 - Pregled knjiga sortiranih po godini izdanja")
    print("  x - Vrati se nazad")
    print()
    
def printEditMenu():
    
    print("\nIzaberite opciju izmene knjige :")
    print()
    print("  1 - Izmena cene")
    print("  2 - Izmena kolicine")
    print("  x - Vrati se nazad")
    print()
    
def printSellMenu():
    
    print("\nIzaberite opciju  :")
    print()
    print("  1 - Dodaj knjigu u korpu")
    print("  2 - Formiraj racun")
    print("  x - Vrati se nazad")
    print()   
    
def findBook():
    print()
    print("[1] Pronalazenje knjige preko identifikatora []\n")
    identifikator = input("Unesite identifikator >> ")
    book = knjige.findBook(identifikator)
    if book != None:
        print(knjige.formatHeader())
        print(knjige.formatBook(book))
    else:
        print()
        print("Nije pronadjena knjiga sa identifikatorom", identifikator)

def searchBooks():
    print()
    print("[2] Pretrazivanje knjiga\n")
    komanda = "0"
    while komanda != "X":
        komanda = searchMenu()
        if komanda == "1":
            searchBooksTitle()
        elif komanda == "2":
            searchBooksAuthors()
        elif komanda == "3":
            searchBooksPublisher()
        elif komanda == "4":
            searchBooksYear()
    return

def sortBooks():
    print()
    print("[3] Pregled knjiga\n")
    komanda = "0"
    while komanda != "X":
        komanda = sortMenu()
        if komanda == "1":
            sortBooksPrice()
        elif komanda == "2":
            sortBooksAuthors()
        elif komanda == "3":
            sortBooksYear()
    return

def editBook():
    print()
    print("[4] Izmena knjige\n")
    komanda = "0"
    while komanda != "X":
        komanda = editMenu()
        if komanda == "1":
            editBookPrice()
        elif komanda == "2":
            editBookQuantity()
        elif komanda == "3":
            sortBooksYear()
    return

def sellBook():
    print()
    print("[5] Prodaja knjiga\n")
    komanda = "0"
    while komanda != "X":
        komanda = sellMenu()
        if komanda == "1":
            sellAddOnAcc()
        elif komanda == "2":
            sellFinish()
        elif komanda == "3":
            sortBooksYear()
    return
        
def sellAddOnAcc():
    print()
    print("[1] Dodaj knjigu u korpu\n")
    print()
    print(knjige.formatHeader())
    print(knjige.formatAllBooks())
    print()
    bill = {}
    identifikator = input("Unesite identifikator >> ")
    book = knjige.findBook(identifikator)
    if book == None:
        print()
        print("Knjiga sa unetim identifikatorom ne postoji u sistemu")
        print("Pokusajte opet sa drugim identifikatorom")
    else:
        print(knjige.formatHeader())
        print(knjige.formatBook(book))
        print()
        broj = input("Unesite broj primeraka koje zelite dodati u korpu >> ")
        if (int(book["kolicina"])-int(broj))<0:
            print()
            print("Ne postoji toliko primeraka knjige u knjizari, pokusajte ponovo")
        else:
            book["kolicina"] =str(int(book["kolicina"])-int(broj))
            knjige.saveBooks()
            bill["naslov"] = book["naslov"]
            bill["cena"] = book["cena"]
            bill["broj"] = broj
            bill["suma"]=str(int(bill["cena"])*int(broj))
            bill["radnik"]= korisnici.radnik()
            racun.addBill(bill)
            racun.saveBills()  
            print(racun.formatHeader())
            print(racun.formatAllBills())
        
def sellFinish():
    print(racun.formatFinalHeader())
    print(racun.formatAllBillsFinal())
    print(racun.formatFinalHeaderBot())
    print("Vas ukupan racun iznosi:          |"+ racun.priceSum()+"|")
    print(racun.formatFinalHeaderBot())
        
def searchBooksTitle():
    print()
    print("[1] Pretrazivanje knjiga po naslovu\n")
    naslov = input("Unesite naslov >> ")
    bookList = knjige.searchBooks("naslov", naslov)
    if len(bookList) == 0:
        print()
        print("\nNe postoji trazena knjiga.")
    else:
        print("\n")
        print(knjige.formatHeader())
        print(knjige.formatBooks(bookList))
        
def searchBooksAuthors():
    print()
    print("[2] Pretrazivanje knjiga po autorima\n")
    autor = input("Unesite autora >> ")
    bookList = knjige.searchBooks("autor", autor)
    if len(bookList) == 0:
        print()
        print("\nNe postoji trazena knjiga.")
    else:
        print("\n")
        print(knjige.formatHeader())
        print(knjige.formatBooks(bookList))
        
def searchBooksPublisher():
    print()
    print("[3] Pretrazivanje knjiga po izdavac\n")
    izdavac = input("Unesite izdavaca >> ")
    bookList = knjige.searchBooks("izdavac", izdavac)
    if len(bookList) == 0:
        print()
        print("\nNe postoji trazena knjiga.")
    else:
        print("\n")
        print(knjige.formatHeader())
        print(knjige.formatBooks(bookList))
        
def searchBooksYear():
    print()
    print("[4] Pretrazivanje knjiga po godini izdanja\n")
    year = input("Unesite godinu izdanja >> ")
    bookList = knjige.searchBooks("godinaIzdanja", year)
    if len(bookList) == 0:
        print()
        print("\nNe postoji trazena knjiga.")
    else:
        print("\n")
        print(knjige.formatHeader())
        print(knjige.formatBooks(bookList))
        
def sortBooksPrice():
    print()
    print("[1] Pregled svih knjiga sortiranih po ceni\n")
    knjige.sortBooks("cena")
    print(knjige.formatHeader())
    print(knjige.formatAllBooks())

def sortBooksAuthors():
    print()
    print("[2] Pregled svih knjiga sortiranih po autorima\n")
    knjige.sortBooks("autor")
    print(knjige.formatHeader())
    print(knjige.formatAllBooks())    
    
def sortBooksYear():
    print("[3] Pregled svih knjiga sortiranih po godini izdanja\n")
    knjige.sortBooks("godinaIzdanja")
    print(knjige.formatHeader())
    print(knjige.formatAllBooks())    
    
def editBookPrice():
    print()
    print("[1] Izmena cene knjige\n")
    identifikator = input("Unesite identifikator >> ")
    book = knjige.findBook(identifikator)
    if book == None:
        print()
        print("Ne postoji knjiga sa datim identifikatorom")
    else:
        print(knjige.formatHeader())
        print(knjige.formatBook(book))
        print()
        test = input("Unesite novu cenu knjige >> ")
        while not test.isdigit():
            test = input("Cena mora biti ceo broj, pokusajte ponovo >> ")     
        book["cena"] = test
        knjige.saveBooks()
        print()
        print("Cena knjige sa identifikatorom '"+identifikator+"' je promenjena i sada iznosi: " + test)
        
def editBookQuantity():
    print()
    print("[2] Izmena kolicine knjige\n")
    identifikator = input("Unesite identifikator >> ")
    book = knjige.findBook(identifikator)
    if book == None:
        print()
        print("Ne postoji knjiga sa datim identifikatorom")
    else:
        print(knjige.formatHeader())
        print(knjige.formatBook(book))
        print()
        test = input("Unesite novu kolicinu knjige >> ")
        while not test.isdigit():
            test = input("Kolicina mora biti ceo broj, pokusajte ponovo >> ")     
        book["kolicina"] = test
        knjige.saveBooks()
        print()
        print("Kolicina knjige sa identifikatorom '"+identifikator+"' je promenjena i sada iznosi: " + test)
        
def addBook():
    print()
    print("[5] Dodaj novu knjigu\n")
    identifikator = input("Unesite identifikator >> ")
    book = knjige.findBook(identifikator)
    if book != None:
        print("------------------------------------------------------")
        print("Knjiga sa unetim identifikatorom vec postoji u sistemu")
        print("Pokusajte opet sa drugim identifikatorom")
        print("------------------------------------------------------")
    else: 
        book = {}
        book["identifikator"] = identifikator
        book["naslov"] = input("Unesite naslov >> ")
        book["autor"] = input("Unesite autora >> ")
        book["izdavac"] = input("Unesite izdavaca >> ")
        test = input("Unesite cenu >> ")
        while not test.isdigit():
            test = input("Cena mora biti ceo broj, pokusajte ponovo >> ")     
        book["cena"] = test
        test = input("Unesite kolicinu >> ")
        while not test.isdigit():
            test = input("Kolicina mora ceo biti broj, pokusajte ponovo >> ")     
        book["kolicina"] = test
        test = input("Unesite godinu izdanja >> ")
        while not test.isdigit():
            test = input("Godina izdanja mora biti ceo broj, pokusajte ponovo >> ")     
        book["godinaIzdanja"] = test
        knjige.addBook(book)
        knjige.saveBooks()

if __name__ == "__main__":
    main()
    