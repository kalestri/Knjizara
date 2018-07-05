'''
Created on 21.09.2012.

@author: Aleksandar
'''
from os.path import exists
import korisnici

def str2bill(line):
    if line[-1] == "\n":
        line = line[:-1]
    identifikator,naslov,cena, broj, suma, radnik = line.split("|")
    bill = {
        "naslov": naslov,
        "cena": cena,
        "broj": broj,
        "suma": suma,
        "radnik": radnik
    }
    return bill

def bill2str(bill):
    return "|".join([bill["naslov"],bill["cena"],bill["broj"],bill["suma"],bill["radnik"]])

def formatHeader():
    return \
        "----------------------------------\n"\
        "Trenutno stanje vase korpe: \n" \
        "\n" \
        "----------------------------------\n"\
        "Naslov              |Cena   |Broj \n " \
        "-------------------+-------+-----"\

def formatFinalHeader():
    return \
        "------------------------------------------\n"\
        "Vas racun            "+korisnici.radnik()+"\n" \
        "\n" \
        "------------------------------------------\n"\
        "Naslov              |Cena   |Broj |Suma  \n " \
        "-------------------+-------+-----+-------"\

def formatFinalHeaderBot():
    return \
        "------------------------------------------"\
        
def formatBill(bill):
    return "{0:20}|{1:7}|{2:4}".format(
      bill["naslov"],
      bill["cena"],
      bill["broj"])
    
def formatBillFinal(bill):
    return "{0:20}|{1:7}|{2:5}|{3:5}".format(
      bill["naslov"],
      bill["cena"],
      bill["broj"],
      bill["suma"])

def formatBills(billList):
    result = ""
    for bill in billList:
        result += formatBill(bill) + "\n"
    return result

def formatBillsFinal(billList):
    result = ""
    for bill in billList:
        result += formatBillFinal(bill) + "\n"
    return result

        
def formatAllBills():
    return formatBills(bills)

def formatAllBillsFinal():
    return formatBillsFinal(bills)

def loadBills():
    checkFile()
    for line in open("racuni.txt", "r").readlines():
        if len(line) > 1:
            bill = str2bill(line)
            bills.append(bill)
            
def checkFile():
    if not exists("racuni.txt"):
        open("racuni.txt", "w").close()

def saveBills():
    file = open("racuni.txt", "w")
    for bill in bills:
        file.write(bill2str(bill))
        file.write("\n")
    file.close()
    
def priceSum():
    file = open("racuni.txt", "r")
    temp=0
    for bill in bills:
        temp=temp+(int(bill["suma"]))
    file.close()
    return str(temp)

def addBill(bill):
    bills.append(bill)

bills = []