'''
Created on 20.09.2012.

@author: Aleksandar
'''
def login(username,password):
    for user in korisnici:
        if user["username"] == username and user["password"] == password:
            imePrezime.append(user["ime"])
            imePrezime.append(user["prezime"])
            return True
    return False

def loadUsers():
    check=""
    for line in open("korisnici.txt","r").readlines():
        x=1
        check1=check
        if len(line)>1:
            user = str2user(line)
            check = user["username"]
            if check == check1:
                x=x+1
            else:
                korisnici.append(user)
    checkPrint(x)

def checkPrint(x):
    print()
    print("Postoje jos",x,"korisnika sa istim korisnickim imenom!!!")
    print("Oni nisu ucitani!")
    print("Ispravite to u korisnici.txt pre ponovnog pokretanja programa.")

def str2user(line):
    if line[-1] == "\n":
        line=line[:-1]
    ime,prezime,username,password = line.split("|")
    user = {
        "ime":ime,
        "prezime":prezime,
        "username":username,
        "password":password
        }
    return user

def user2str(user):
    return "|".join([user["ime"],user["prezime"],user["username"],user["password"]])

   
def radnik():
    imeRadnika=imePrezime[0]+" "+imePrezime[1]
    return imeRadnika

imePrezime=[]
korisnici=[]
loadUsers()
