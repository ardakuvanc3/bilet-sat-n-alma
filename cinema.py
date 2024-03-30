from prettytable import PrettyTable
from colorama import Fore, Style
import datetime
import time
import os
import random

now = datetime.datetime.now()
day = now.day
month = now.month
year = now.year

movie_table = PrettyTable(["İsim", "Fiyat", "Saat"])

movie_table.add_row(["Oppenheimer", "150₺", "15:00"])
movie_table.add_row(["Oppenheimer", "150₺", "21:00"])
movie_table.add_row(["Barbie", "150₺", "15:00"])
movie_table.add_row(["Barbie", "150₺", "15:00"])
movie_table.add_row(["Tenet", "150₺", "15:00"])
movie_table.add_row(["Tenet", "150₺", "15:00"])
movie_table.add_row(["İntersteller", "150₺", "15:00"])
movie_table.add_row(["İntersteller", "150₺", "15:00"])
movie_table.add_row(["İntersteller", "150₺", "15:00"])
movie_table.add_row(["Spiderman", "150₺", "15:00"])

def loginPage():
    if 1 <= month <= 9:
        print(Fore.GREEN + """
            
    Arda Sinemalarına Hoş Geldiniz!
        
    Tarih: {}.0{}.{}
            
        Filmlerimiz: 
            """.format(day, month, year))
        time.sleep(2)
        print(movie_table)
        print(Style.RESET_ALL)
    
    else:
        print(Fore.GREEN + """
            
        Arda Sinemalarına Hoş Geldiniz!
        
        Tarih: {}.{}.{}
            
        Filmlerimiz: 
        
        
            """.format(day, month, year))
        time.sleep(2)
        print(movie_table)
        print(Style.RESET_ALL)

def MovieChoice():
    isOk = True
    while isOk:
        isimler = [satir[0] for satir in movie_table._rows]
        fiyatlar = [satir[1] for satir in movie_table._rows]
        saatler = [satir[2] for satir in movie_table._rows]
        global movie_choice
        global time_choice
        movie_choice = input("İstediğiniz Film İsmini Seçiniz: ")
        # İsimleri ekrana yazdır
        if movie_choice in isimler:
            isOk = False
            time_choice = input("Saat: ")
            while time_choice not in saatler:
                print("Geçersiz saat, lütfen tekrar deneyin.")
                time_choice = input("Saat: ")
        else:
            print("Geçersiz film, lütfen tekrar deneyin.")
        
            # Film ve seans bulunduğunda fiyatı al
        index = (isimler.index(movie_choice), saatler.index(time_choice))
        global price
        price = movie_table._rows[index[0]][1]  # Fiyatı al


def Odeme():
    print("Ödeme Sayfasına Hoş Geldiniz!")
    print("Seçilen Film: " + movie_choice)
    print("Seçilen Film Seansı: " + time_choice)
    print("Ödenecek Tutar: " + price)
    
    while True:
        global odeme_soru
        odeme_soru = input("Ödemeyi Nasıl Yapacaksınız?: ").lower()
        
        if odeme_soru == "nakit":
            print("{} nakit ödemeniz alınmıştır.".format(price))
            time.sleep(3)
            break
        elif odeme_soru == "kart":
            print("Kartınızdan {} çekilmiştir".format(price))
            time.sleep(3)
            break
        else:
            print("Hatalı Giriş! Bloklandın!")

def BiletYazdir():
    
    harfler = ["a", "b", "c", "d", "e", "f"]
    koltuk = random.randint(1,10)
    koltuk_str = random.choice(harfler)
    
    print("      Biletiniz       ")
    print("Filminiz: "+ movie_choice)
    print("Seansınız: "+ time_choice)
    print("Koltuk Numaranız: {}.sıra {} numara".format(koltuk, koltuk_str) )
    print("Ödenen Ücret : " + price)
    print("İşlem: "+ odeme_soru)
    


loginPage()
MovieChoice()
os.system('cls')
Odeme()
os.system('cls')
BiletYazdir()


