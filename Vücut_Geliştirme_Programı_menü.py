from  Body_Building_Program_Modülleri import *

print("""\033[93m
❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ 

                Vücut Geliştirme Rehberi
                     M.N.C Yazılım 

❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ ❈ 
""")
Vücut_Geliştirme_atama = Vücut_Geliştirme_Programı()
İşlem_Kayıtları_Programı_atama = İşlem_Kayıtları_Programı()


while True:
    try:
        print("\nVücut Geliştirme Menü İşlemleri\n_______________________________\n1 Kayıtlı Kullanıcılar\n2 Kullanıcı Ekle\n3 Kullanıcı Sil\n7 Program Hakkında\n8 Tek Kullanıcı Çok İşlem\n_______________________________")
        menü = int(input("\nİşlem numarası giriniz : "))
        if(menü == 1):
            Vücut_Geliştirme_atama.vücut_geliştirme_bilgileri()
            time.sleep(2)
        elif(menü == 2):# kayıt menüsü başlangıç ----------------------------------------------
            try:

                print("\nÖrnek İsim & Soyisim : Nurullah İkbal")
                isim = input("Kayıt olucak kişinin İsmini & Soyismini Giriniz : ")

                print("\n1 Erkek\n2 Kadın\nÖrnek Cinsiyet : 1")
                cinsiyet = int(input("Kayıt olucak kişinin Cinsiyetini Giriniz : "))
                if(cinsiyet == 1):
                    cinsiyet = "Erkek"
                elif(cinsiyet == 2):
                    cinsiyet = "Kadın"
                else:
                    print("Hatalı Seçim")
                    cinsiyet = "Belirtilmedi"
                print("\nÖrnek Yaş : 18")
                yaş = int(input("Kayıt olucak kişinin Yaşını Giriniz : "))
                print("\nÖrnek Boy : 185")
                boy = int(input("Kayıt olucak kişinin Boyunu Giriniz cm: "))
                print("\nÖrnek Kilo : 105")
                kilo = int(input("Kayıt olucak kişinin Kilosunu Giriniz kg: "))
                print("\n______________\n1 Güç Kazanma\n2 Kas Arttırma\n______________\n\nÖrnek Hedef : 1")
                hedef = int(input("Kayıt olucak kişinin Hedefini Giriniz : "))
                vücut_indeksi = "Belirtilmedi"
                vücut_su_ihtiyacı = "Belirtilmedi"
                kayıt_tarihi = "Belirtilmedi"
                if(hedef == 1):
                    hedef = "Güç Kazanma"
                elif(hedef == 2):
                    hedef = "Kas Arttırma"
                else:
                    hedef = "Belirtilmedi"
                    print("Hatalı seçim ")

                hepsi = Vücut_Geliştirme(isim,cinsiyet,yaş,boy,kilo,hedef,vücut_indeksi,vücut_su_ihtiyacı,kayıt_tarihi)
                Vücut_Geliştirme_atama.vücut_geliştirme_bilgileri_ekleme(hepsi,isim)
                Vücut_Geliştirme_atama.vücut_geliştirme_bilgileri_vücut_indeksi_hesaplama(isim)# burada ve aşağı satırdaki istediğim 2 fonksiyonu çalıştırdım :D iyi anlamaya çalışın çok önemli
                Vücut_Geliştirme_atama.vücut_su_ihtiyacı_hesaplama(isim)
                Vücut_Geliştirme_atama.kayıt_tarihi(isim)
                # burası işlemkayıtları için
                kayıt_oluşturma = ""
                kayıt_silme = "Belitilmedi"
                işlem_kayıtları_hepsi = İşlem_Kayıtları(isim,kayıt_oluşturma,kayıt_silme)
                İşlem_Kayıtları_Programı_atama.işlem_kayıtları_ekleme(işlem_kayıtları_hepsi)
                time.sleep(1)
            except ValueError:
                print("Lütfen Sayı giriniz : ")
                #  kayıt menüsü bitiş ------------------------------------------------------------
        elif(menü == 3):
            silme_input = input("Silmek istediğiniz Kullanıcı İsmini & Soyismini Giriniz : ")
            Vücut_Geliştirme_atama.vücut_geliştirme_bilgileri_silme(silme_input)
            İşlem_Kayıtları_Programı_atama.işlem_kayıtları_silme_güncelleme(silme_input)
            time.sleep(2)
        elif(menü == 7):
            Vücut_Geliştirme_atama.program_bilgileri()
            time.sleep(2)
        elif(menü == 8):
            isim_input = input("\nİşlem yapmak istediğiniz Kullanıcı İsmi & Soyismini giriniz : ")
            Vücut_Geliştirme_atama.bütün_işlemler(isim_input)# Toplu işlem için fonksiyon oluşturdum ve burda o fonskiyonu kullandım..!
            time.sleep(0.5)
        elif(menü == "KayıtlarıGöster"):
            İşlem_Kayıtları_Programı_atama.işlem_kayıtları_bilgiler()
        else:
            print("Geçersiz işlem numarası ..!")
            time.sleep(1)
    except ValueError:
        print("Geçersiz işlem ..!")
        time.sleep(2)