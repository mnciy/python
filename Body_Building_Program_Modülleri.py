import sqlite3
import time
import os
from datetime import datetime # zaman hesaplayıcı için
import locale # zaman heasplayıcı için
locale.setlocale(locale.LC_ALL,"") # zaman hesaplayıcı türkçe çevirmek için
# Os modülü
def klasör():
    kullanıcı_adı = str(os.getlogin())
    başlangıç_dizini = "C:\\Users\\"+kullanıcı_adı+"\\Desktop"
    klasör_eklenmiş_dizin = "C:\\Users\\"+kullanıcı_adı+"\\Desktop\\VücutGeliştirmeDatabase"
    try:
        os.chdir(başlangıç_dizini)
        os.mkdir(klasör_eklenmiş_dizin)
    except FileExistsError:
        pass
    os.chdir(klasör_eklenmiş_dizin)

klasör()

class Vücut_Geliştirme():

    def __init__(self,isim_soyisim,cinsiyet,yaş,boy,kilo,hedef,vücut_indeksi,vücut_su_ihtiyacı,kayıt_tarihi):
        self.isim_soyisim = isim_soyisim
        self.cinsiyet = cinsiyet
        self.yaş = yaş
        self.boy = boy
        self.kilo = kilo
        self.hedef = hedef
        self.vücut_indeksi = vücut_indeksi
        self.vücut_su_ihtiyacı = vücut_su_ihtiyacı
        self.kayıt_tarihi = kayıt_tarihi


    def __str__(self):

        return "\nİsim & Soyisim : {}\nCinsiyet : {}\nYaş : {}\nBoy : {}\nKilo : {}\nHedefi : {}\nVücut İndeksi : {}\nVücut Su İhtiyacı : {}\nKayıt Tarihi : {}\n\n".format(self.isim_soyisim,self.cinsiyet,self.yaş,self.boy,self.kilo,self.hedef,self.vücut_indeksi,self.vücut_su_ihtiyacı,self.kayıt_tarihi)


class Vücut_Geliştirme_Programı():
    def __init__(self):

        self.bağlantıoluştur()

    def bağlantıoluştur(self):
        self.bağlantı = sqlite3.connect("VücutGeliştirmeProgramı.db")
        self.cursor = self.bağlantı.cursor()
        vücut_geliştirme_tablosu = "Create table If not exists VücutGeliştirmeProgramı (isim_soyisim TEXT,cinsiyet TEXT,yaş İNT,boy İNT,kilo İNT,hedef TEXT,vücut_indeksi TEXT,vücut_su_ihtiyacı TEXT,kayıt_tarihi TEXT)"
        self.cursor.execute(vücut_geliştirme_tablosu)
        self.bağlantı.commit()

    def bağlantıbitir(self):
        self.bağlantı.close()
    def kayıt_tarihi(self,isim_soyisim):
        sorgu = "Update VücutGeliştirmeProgramı set kayıt_tarihi = ? where isim_soyisim = ?"
        şimdiki_zaman = datetime.now()
        düzenli_tarih = datetime.strftime(şimdiki_zaman, "%d %B %Y %A %X")
        self.cursor.execute(sorgu,(düzenli_tarih,isim_soyisim))
        self.bağlantı.commit()

    def işlem_kaydı(self,):

        şimdiki_zaman = datetime.now()
        düzenli_tarih = datetime.strftime(şimdiki_zaman, "%d %B %Y %A %X")
        ayırıştırma = datetime.strptime(düzenli_tarih, "%d %B %Y %A %X")
        #_________________________
        saniye = fark.seconds % 60
        dakika = fark.seconds // 60
        saat = fark.seconds // 3600


        #__________________________

        if (dakika > 0):
            print(str(dakika) + " Dakika", str(saniye) + " Sn Önce Yapıldı.")

    def vücut_su_ihtiyacı_hesaplama(self,ara_input):
        sorgu = "Select cinsiyet,kilo From VücutGeliştirmeProgramı where isim_soyisim = ?"
        self.cursor.execute(sorgu,(ara_input,))
        cinsiyet_kilo_liste = self.cursor.fetchall()
        if(len(cinsiyet_kilo_liste) == 0):
            print("Kayıtlı kullanıcı bulunamadı ..!")
        else:
            for c_k in cinsiyet_kilo_liste:
                cinsiyet = c_k[0]
                kilo = c_k[1]
                su_ihtiyacı_yeni = " "
                if(cinsiyet == "Erkek"):
                    su_ihtiyacı_yeni = "Ortalama "+str(round(kilo * 0.032,3))+" Litre"
                elif(cinsiyet == "Kadın"):
                    su_ihtiyacı_yeni = "Günlük Ortalama " + str(round(kilo * 0.030,3)) + " Litre"
                sorgu2 = "Update VücutGeliştirmeProgramı set vücut_su_ihtiyacı = ? where isim_soyisim = ?"
                self.cursor.execute(sorgu2,(su_ihtiyacı_yeni,ara_input))
                self.bağlantı.commit()


    def vücut_geliştirme_bilgileri(self):
        vücut_geliştirme_bilgileri = "Select * From VücutGeliştirmeProgramı"
        self.cursor.execute(vücut_geliştirme_bilgileri)
        vücut_geliştirme_bilgileri_listesi = self.cursor.fetchall()
        if(len(vücut_geliştirme_bilgileri_listesi) == 0):
            print("Kullanıcı kaydı oluşturulmamış ..!")
        else:
            for v in vücut_geliştirme_bilgileri_listesi:
                vücut_geliştirme_listesi_for = Vücut_Geliştirme(v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8])
                print(vücut_geliştirme_listesi_for)

    def vücut_geliştirme_bilgileri_ara(self,ara_input):
        vücut_geliştirme_bilgileri_ara_sorgu = "Select * From VücutGeliştirmeProgramı where isim_soyisim = ?"
        self.cursor.execute(vücut_geliştirme_bilgileri_ara_sorgu,(ara_input,))
        v_liste = self.cursor.fetchall()
        if(len(v_liste) == 0):
            print(ara_input+" Kayıtlı değil ..!")
        else:
            arama_listesi = Vücut_Geliştirme(v_liste[0][0],v_liste[0][1],v_liste[0][2],v_liste[0][3],v_liste[0][4],v_liste[0][5],v_liste[0][6],v_liste[0][7],v_liste[0][8])
            print(arama_listesi)

    def vücut_geliştirme_bilgileri_ekleme(self,V,isim_input):
        try:
            # aynı kullanıcıdan varsa bunu sorgulamak için
            sorgu = "Select * From VücutGeliştirmeProgramı where isim_soyisim = ?"
            self.cursor.execute(sorgu, (isim_input,))
            isim = self.cursor.fetchall()
            self.bağlantı.commit()
            if (len(isim) == 1):
                print(isim_input+" Sisteme kayıtlı ..!\nYeni kullanıcı eklenmedi ..!")
            else:
                # burda direk kullanıcı ekliyorum üstteki aynı kullanıcı varsa eklenmesin diye yazmış oldugum sorgu
                vücut_ekleme = "Insert into VücutGeliştirmeProgramı Values (?,?,?,?,?,?,?,?,?)"
                self.cursor.execute(vücut_ekleme,(V.isim_soyisim,V.cinsiyet,V.yaş,V.boy,V.kilo,V.hedef,V.vücut_indeksi,V.vücut_su_ihtiyacı,V.kayıt_tarihi))
                self.bağlantı.commit()
                print("\nKullanıcı kaydı oluşturuldu .")
                İşlem_Kayıtları_Programı_atama = İşlem_Kayıtları_Programı() # bu class ı kullanmak için değişken atadım

        except sqlite3.OperationalError:
            print("Vücut Geliştirme Rehberi Programından 1 den fazla algılandı lütfen diğerlerini kapatın ..!")







    def vücut_geliştirme_bilgileri_silme(self,silme_input):
        try:
            vücut_geliştirme_bilgileri_kontrol_2 = "Select * From VücutGeliştirmeProgramı where isim_soyisim = ?"
            self.cursor.execute(vücut_geliştirme_bilgileri_kontrol_2,(silme_input,))
            vücut_geliştirme_bilgileri_silme_kontrol_listesi = self.cursor.fetchall()
            if (len(vücut_geliştirme_bilgileri_silme_kontrol_listesi) == 0):
                print("Kullanıcı kaydı oluşturulmamış ..!")
            else:
                print("Kullanıcı Silindi ... \n")
                vücut_geliştirme_bilgileri_silme_sorgu = "Delete From VücutGeliştirmeProgramı where isim_soyisim = ?"
                self.cursor.execute(vücut_geliştirme_bilgileri_silme_sorgu, (silme_input,))
                self.bağlantı.commit()
            self.bağlantı.commit()
        except sqlite3.OperationalError:
            print("Vücut Geliştirme Rehberi Programından 1 den fazla algılandı lütfen diğerlerini kapatın ..!")


    def vücut_geliştirme_bilgileri_kilo_değiştirme(self,isim_input):
        try:
            print("\nÖrnek kilo : 90")
            yeni_kilo_int = int(input("Yeni kilo girin kg : "))
            sorgu = "Update VücutGeliştirmeProgramı set kilo = ? where isim_soyisim = ?"
            self.cursor.execute(sorgu,(yeni_kilo_int,isim_input))
            self.bağlantı.commit()
            self.vücut_geliştirme_bilgileri_vücut_indeksi_hesaplama(isim_input)
            print("Kilo Güncellendi .\n")
        except ValueError:
            print("\nHatalı kilo girişi ..!\nKilo güncellenemedi ..!")
    def vücut_geliştirme_bilgileri_boy_değiştirme(self,isim_input):
        try:
            print("\nÖrnek boy : 188")
            yeni_boy_int = int(input("Yeni boy giriniz cm : "))
            sorgu = "Update VücutGeliştirmeProgramı set boy = ? where isim_soyisim = ?"
            self.cursor.execute(sorgu,(yeni_boy_int,isim_input))
            self.bağlantı.commit()
            self.vücut_geliştirme_bilgileri_vücut_indeksi_hesaplama(isim_input)
            print("Boy Güncellendi .\n")
        except ValueError:
            print("\nHatalı boy girişi ..!\nBoy güncellenemedi ..!")


    def vücut_geliştirme_bilgileri_vücut_indeksi_hesaplama(self,hesapla):
        vücut_geliştirme_bilgileri_sorgu = "Select kilo,boy From VücutGeliştirmeProgramı where isim_soyisim = ?"
        self.cursor.execute(vücut_geliştirme_bilgileri_sorgu,(hesapla,))
        vücut_geliştirme_bilgileri_liste = self.cursor.fetchall()
        if(len(vücut_geliştirme_bilgileri_liste) == 0):
            print("Kullanıcı Bulunamadı ..!")
        else:
            for kb in vücut_geliştirme_bilgileri_liste:
                kilo = kb[0]
                boy = kb[1]
                çarpım = (kilo / (boy / 50))
                vücut = "Belirtilmemiş"
                if çarpım < 18.5:
                    vücut = "Zayıf"
                elif çarpım < 25:
                    vücut = "Normal"
                elif çarpım < 30:
                    vücut = "Fazla Kilolu"
                elif çarpım < 35:
                    vücut = "1.Derece Obez"
                elif çarpım < 40:
                    vücut = "2.Derece Obez"
                elif çarpım > 40:
                    vücut = "3.Derecede Obez"
                sorgu = "Update VücutGeliştirmeProgramı set vücut_indeksi = ? where isim_soyisim = ?"
                self.cursor.execute(sorgu,(vücut,hesapla))
        self.bağlantı.commit()


    def bütün_işlemler(self,isim_input):# burda diğer fonksiyonları argüman olrak döndüm süpper değilmi :D
        vücut_geliştirme_bilgileri_ara_sorgu = "Select * From VücutGeliştirmeProgramı where isim_soyisim = ?"
        self.cursor.execute(vücut_geliştirme_bilgileri_ara_sorgu,(isim_input,))
        v_liste = self.cursor.fetchall()
        if(len(v_liste) == 0):
            print(isim_input+" Kayıtlı değil ..!")
        else:
            arama_listesi = Vücut_Geliştirme(v_liste[0][0],v_liste[0][1],v_liste[0][2],v_liste[0][3],v_liste[0][4],v_liste[0][5],v_liste[0][6],v_liste[0][7],v_liste[0][8])
            print(arama_listesi)
            while True:
                try:
                    print("_______________________________\n1 Kullanıcı Kaydını Sil\n2 Kullanıcı Kilo Değiştir\n3 Kullanıcı Boy Değiştir\n9 Ana Menüye Dön\n_______________")
                    işlem_seç = int(input("\nİşlem seçiniz : "))
                    if(işlem_seç == 1):
                        İşlem_Kayıtları_Programı_atama = İşlem_Kayıtları_Programı()# Başka Class dan fonksiyon almak için yazdım
                        self.vücut_geliştirme_bilgileri_silme(isim_input)
                        İşlem_Kayıtları_Programı_atama.işlem_kayıtları_silme_güncelleme(isim_input)# Başka class
                        time.sleep(2)
                        break
                    elif(işlem_seç == 2):
                        self.vücut_geliştirme_bilgileri_kilo_değiştirme(isim_input)
                        time.sleep(2)
                        time.sleep(2)
                    elif(işlem_seç == 3):
                        self.vücut_geliştirme_bilgileri_boy_değiştirme(isim_input)
                        time.sleep(2)
                    elif(işlem_seç == 9):
                        time.sleep(1)
                        break
                except ValueError:
                    print("İşlem numarası hatalı ..!")

    def program_bilgileri(self):
        print("\nProgramın Kayıtlı Olduğu yer : ", os.getcwd())
        print("Programı Hazırlayan : Nurullah İkbal")


class İşlem_Kayıtları():
    def __init__(self,isim_soyisim,kayıt_oluşturma,kayıt_silme):
        self.isim_soyisim = isim_soyisim
        self.kayıt_oluşturma = kayıt_oluşturma
        self.kayıt_silme = kayıt_silme

    def __str__(self):

        return "\nİsim Soyisim : {}\nKayıt Oluşturma : {}\nSilinen Kayıt {}".format(self.isim_soyisim,self.kayıt_oluşturma,self.kayıt_silme)

class İşlem_Kayıtları_Programı():
    def __init__(self):
        self.bağlantıoluştur()

    def bağlantıoluştur(self):
        self.bağlantı = sqlite3.connect("İşlemKayıtları.db")
        self.cursor = self.bağlantı.cursor()
        işlem_kayıtları_tablosu = "Create Table If not exists İşlemKayıtları (isim_soyisim TEXT,kayıt_oluşturma TEXT,kayıt_silme TEXT)"
        self.cursor.execute(işlem_kayıtları_tablosu)
        self.bağlantı.commit()
    def bağlantıbitir(self):
        self.bağlantı.close()
    def işlem_kayıtları_ekleme(self,K):
        şimdiki_zaman = datetime.now()
        düzenli_zaman = datetime.strftime(şimdiki_zaman, "%d %B %Y %A %X")
        sorgu = "Insert into İşlemKayıtları Values (?,?,?)"
        self.cursor.execute(sorgu,(K.isim_soyisim,K.kayıt_oluşturma+düzenli_zaman,K.kayıt_silme))
        self.bağlantı.commit()



    def işlem_kayıtları_silme_güncelleme(self,isim_soyisim):
        sorgu = "Update İşlemKayıtları set kayıt_silme = ? where isim_soyisim = ?"
        şimdiki_zaman = datetime.now()
        düzenli_tarih = datetime.strftime(şimdiki_zaman, "%d %B %Y %A %X")
        kayıt_silme = düzenli_tarih+" Kayıt silindi."
        self.cursor.execute(sorgu,(kayıt_silme,isim_soyisim))
        self.bağlantı.commit()

    def işlem_kayıtları_bilgiler(self):
        sorgu = "Select * From İşlemKayıtları"
        self.cursor.execute(sorgu,)
        bilgiler = self.cursor.fetchall()
        if(len(bilgiler) == 0):
            print("\nİşlem Kaydı Bulunamadı ..!")
        else:
            for b in bilgiler:
                bilgiler_listesi = İşlem_Kayıtları(b[0],b[1],b[2])
                print(bilgiler_listesi)

