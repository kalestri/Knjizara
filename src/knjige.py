'''
Created on 20.09.2012.

@author: Aleksandar
'''
from os.path import exists

def str2book(line):
    if line[-1] == "\n":
        line = line[:-1]
    identifikator, naslov, autor, izdavac, cena, kolicina, godinaIzdanja = line.split("|")
    book = {
        "identifikator": identifikator,
        "naslov": naslov,
        "autor": autor,
        "izdavac": izdavac,
        "cena": cena,
        "kolicina": kolicina,
        "godinaIzdanja": godinaIzdanja
    }
    return book

def book2str(book):
    return "|".join([book["identifikator"],book["naslov"],book["autor"],book["izdavac"],
                     book["cena"],book["kolicina"],book["godinaIzdanja"]])
    
def formatHeader():
    return \
        "Id.  |Naslov               |Autor           |Izdavac     |Cena    |Kol.  |God. Izdanja\n " \
        "----+---------------------+----------------+------------+--------+------+---------------"
        
def formatBook(book):
    return "{0:5}|{1:21}|{2:16}|{3:12}|{4:8}|{5:6}|{6:9}".format(
      book["identifikator"],
      book["naslov"],
      book["autor"],
      book["izdavac"],
      book["cena"],
      book["kolicina"],
      book["godinaIzdanja"])
    
def formatBooks(bookList):
    result = ""
    for book in bookList:
        result += formatBook(book) + "\n"
    return result
    
def formatAllBooks():
    return formatBooks(books)

def loadBooks():
    checkFile()
    for line in open("knjige.txt", "r").readlines():
        if len(line) > 1:
            book = str2book(line)
            books.append(book)

def saveBooks():
    file = open("knjige.txt", "w")
    for book in books:
        file.write(book2str(book))
        file.write("\n")
    file.close()

def checkFile():
    if not exists("knjige.txt"):
        open("knjige.txt", "w").close()

def findBook(identifikator):
    for book in books:
        if book["identifikator"] == identifikator:
            return book
    return None

def searchBooks(field, value):
    result = []
    for book in books:
        if book[field].upper() == value.upper():
            result.append(book)
    return result

def addBook(book):
    books.append(book)

def updateBook(identifikator, book):
    books[identifikator] = book


def findMin(bookList, key, start):
    n = len(bookList)
    if n == 0:
        return -1
    if n <= start:
        return -1
    if n-start == 1:
        return start
    min = bookList[start]
    minPos = start
    for i in range(start+1, n):
        if bookList[i][key] < min[key]:
            min = bookList[i]
            minPos = i
    return minPos

def sort(bookList, key, start):
    minPos = findMin(bookList, key, start)
    if minPos == -1:
        return
    bookList[start], bookList[minPos] = bookList[minPos], bookList[start]
    if start < len(bookList)-1:
        sort(bookList, key, start+1)
    
def sortBooks(key):
    sort(books, key, 0)

books = []
loadBooks()
