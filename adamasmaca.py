#Created by Hüseyin.
#Hüseyin tarafından oluşturuldu.
import random
import sys
print("")
ad = input("Adınız: ")
print("Adam asmaca oyununa hoşgeldin " + ad)



print("_KATEGORİLER_")
print("  [1] Programlama Dilleri")
print("  [2] Hayvanlar ")
print("  [3] Bitkiler")
print("  [4] Şehirler")
print("  [5] Ünlüler")
print("  [6] Su markaları")
print("  [0] Çıkış ")

cikti = input("Seçiniz > ")

if cikti == "0":
	print("Çıkılıyor")
	sys.exit()

programlamadili = ["php","javascript","python","C","java","kotlin","perl","ruby","pascal","swift","R","go"]
hayvanlar = ["kedi","köpek","keçi","kuzu","koyun","zürafa","penguen","lama","Eşek","devekuşu","maymun","köpekbalığı","timsah","aslan","panda","domuz","papağan","kanarya","kurt"]
bitkiler = ["salatalık","adaçayı","ahududu","ananas","ayva","anason","blokoli","defne","dereotu","devedikeni","dut","domates","elma","armut","fesleğen","fındık"]
sehirler = ["adana","adıyaman","afyon","ağrı","amasya",",istanbul","ankara","selanik","newyork","kosova","bingöl","bitlis","hakkari","kocaeli","Karabük","izmir","osmaniye","ardahan","kırıkkale","van","tokat"]
unluler = ["selena gomez","beren saat","rihanna","taylor swift","justen bieber","zayn malik","tom cruise","Mustafa Kemal Atatürk","Seyit Onbaşı"]
su = ["sırma","damla","sultan","erikli","pınar","saka","abant","özkaynak","aquafina","hamidiye"]

def whiled():
	string_tahmin = ""
	can = 10
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
		print("------------------")
		string_tahmin += tahmin
		if tahmin not in kelime:
			can -= 1
			print(f"{can} Canın Kaldı ")
			print(" ")
			if can == 0:
				print("")
				print("Kelime " + kelime + "'ydi ")
				print("Öldün")
				print(" ")
				

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
	kelime = random.choice(sehirler)
	whiled()

if cikti == "5":
	kelime = random.choice(unluler)
	whiled()

if cikti == "6":
	kelime = random.choice(su)
	whiled()
