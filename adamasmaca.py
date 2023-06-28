#Created by Hüseyin.
#Hüseyin tarafından oluşturuldu.
import random
import sys
print("")
ad = input("Adınız: ")
print("Adam asmaca oyununa hoşgeldin" + " " + ad)



print("_KATEGORİLER_")
print("  [1] Programlama Dilleri")
print("  [2] Hayvanlar ")
print("  [3] Bitkiler")
print("  [4] Şehirler")
print("  [5] Ülkeler")
print("  [6] Ünlüler")
print("  [7] Su markaları")
print("  [0] Çıkış ")

cikti = input("Seçiniz > ")

if cikti == "0":
	print("Çıkılıyor")
	sys.exit()

programlamadili = ["php","javascript","python","C","java","kotlin","perl","ruby","pascal","swift","R","go",""]
hayvanlar = ["kedi","köpek","keçi","kuzu","koyun","zürafa","penguen","lama","Eşek","devekuşu","maymun","köpekbalığı","timsah","aslan","panda","domuz","papağan","kanarya","kurt"]
bitkiler = ["salatalık","adaçayı","ahududu","ananas","ayva","anason","blokoli","defne","dereotu","devedikeni","dut","domates","elma","armut","fesleğen","fındık"]
Şehirler = ["adana","adıyaman","afyon","ağrı","amasya",",istanbul","ankara","selanik","newyork","kosova","bingöl","bitlis","hakkari","kocaeli","Karabük","izmir","osmaniye","ardahan","kırıkkale","van","tokat"]
Ünlüler = ["selena gomez","beren saat","rihanna","taylor swift","justen bieber","zayn malik","tom cruise","Mustafa Kemal Atatürk","Seyit Onbaşı"]
su = ["sırma","damla","sultan","erikli","pınar","saka","abant","özkaynak","aquafina","hamidiye"]

def whiled():
	while can > 0:
		kcan = 0
		for karakter in kelime:
			if karakter in string_tahmin:
				print(karakter)
			else:
				print("-")
				kcan += 1
		if kcan == 0:
			print("")
			print("Kazandın :D")	
			break
		tahmin = input("Bir Harf : ")
		string_tahmin += tahmin
		if tahmin not in kelime:
			can -= 1
			print("")
			print("")
			print("")
			print(f"{can} Canın Kaldı Dikkat Et")
			if can == 0:
				print("")
				print("Öldün")


string_tahmin = ""
can = 10

if cikti == "1":
	kelime = random.choice(programlamadili)
	whiled()

if cikti == "2":
	kelime = random.choice(hayvanlar)
	whiled()

if cikti == "3":
	kelime = random.choice(bitkiler)
	whiled()

if cikti == "4":
	kelime = random.choice(Şehirler)
	whiled()

if cikti == "5":
	kelime = random.choice(ülkeler)
	whiled()

if cikti == "6":
	kelime = random.choice(ünlüler)
	whiled()

if cikti == "7":
	kelime = random.choice(su)
	whiled()
