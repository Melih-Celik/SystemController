import os
import time

melih_celik="""
 __    __     ______     __         __     __  __        ______     ______     __         __     __  __    
/\ "-./  \   /\  ___\   /\ \       /\ \   /\ \_\ \      /\  ___\   /\  ___\   /\ \       /\ \   /\ \/ /    
\ \ \-./\ \  \ \  __\   \ \ \____  \ \ \  \ \  __ \     \ \ \____  \ \  __\   \ \ \____  \ \ \  \ \  _"-.  
 \ \_\ \ \_\  \ \_____\  \ \_____\  \ \_\  \ \_\ \_\     \ \_____\  \ \_____\  \ \_____\  \ \_\  \ \_\ \_\ 
  \/_/  \/_/   \/_____/   \/_____/   \/_/   \/_/\/_/      \/_____/   \/_____/   \/_____/   \/_/   \/_/\/_/ 
                                                                                                          
"""
def give_space():
    for count in range(20):
        print("\n")

def ins_comp(app):
    print(app,"Kurulumu Tamamlandi.\nLutfen Bekleyiniz...")
    time.sleep(5)
    give_space()

def file_copy_bat():

    files_to_copy=[]

    while True:
        item=input("Kopyalanacak Klasor Yolu : ")
        if item=="end":
            break
        else:
            files_to_copy.append(item)

    target_dir=input("Gonderilecek Klasor Yolu : ")
    bat_file=open("copy_paste.bat","a")
    print("Dosya olusturuluyor...")
    time.sleep(3)
    for counter in files_to_copy:
        target_edited=target_dir.replace("\"","")+"\\"+counter.split("\\")[-1].replace("\"","")
        komut="xcopy "+counter+" \""+target_edited+"\" /E /H /C /I \n"
        bat_file.writelines(komut)
    bat_file.close()

def domain_join():
    try:
        print("Programları kurmadan bilgisayari yeniden başlatmayın.")
        domain_name=input("Domain Adini giriniz : ")
        os.system("powershell add-computer -DomainName "+domain_name)
        print("Bilgisayar Domaine alinmistir.\nYonlendiriliyorsunuz...")
        time.sleep(5)
        give_space()
    except:
        print("Bir hata ile karsilasildi.\nYonlendiriliyorsunuz...")
        time.sleep(5)
        give_space()

def remove_domain():
    try:
        user=input("Yetkili kullanici adi giriniz (ASIR\\administrator stilinde): ")
        os.system("powershell remove-computer -credential "+user+" -force")
        print("Bilgisayar Domainden kaldirilmistir...\nYonlendiriliyorsunuz...")
        time.sleep(5)
        give_space()
    except:
        print("Bir hata ile karsilasildi.\nYonlendiriliyorsunuz...")
        time.sleep(5)
        give_space()

def local_admin():
    try:
        dm_user=input("Local Domainde Olacak Kullanici (ASIR\\melih.celik stilinde): ")
        os.system("powershell Add-LocalGroupMember -Group Administrators -Member $env:"+dm_user)
        print("Kullaniciya Local Admin yetkisi verilmistir.\nYonlendiriliyorsunuz...")
        time.sleep(5)
        give_space()
    except:
        print("Bir hata ile karsilasildi.\nYonlendiriliyorsunuz...")
        time.sleep(5)
        give_space()

def remove_local():
    try:
        rem_user=input("Local User kullanici adi giriniz : ")
        os.system("powershellRemove-LocalUser -Name "+rem_user)
        print("Local Kullanici Kaldirilmistir.\nYonlendiriliyorsunuz...")
        time.sleep(5)
        give_space()
    except:
        print("Bir hata ile karsilasildi.\nYonlendiriliyorsunuz...")
        time.sleep(5)
        give_space()

def install_apps():
    while True:
        app_secim=input("""
    NOT : Programlar Sessiz Kurulumda bu yuzden kurulum ekrani gelmeyecektir.Arada Enter basarak
    programi yenileyebilirsiniz.
    1.Winrar Yukle.
    2.Chrome Yukle.
    3.Office 2016 Standard Yukle.
    4.Office 365 Yukle.
    5.Acrobat PDF Yukle.
    6.Anydesk Yukle.
    7.Hepsini Kur (Office 2016)
    8.Hepsini Kur (Office 365)
    9.Onceki Ekrana Don.
    Secim : """)
        if app_secim=="1":
            print("Winrar Kuruluyor...")
            os.system("Winrar.exe /s")
            ins_comp("Winrar")

        elif app_secim=="2":
            print("Chrome Kuruluyor...")
            os.system("Chrome.exe /silent /install")
            ins_comp("Chrome")

        elif app_secim=="3":
            print("Office 2016 Kuruluyor...")
            os.system("Office_2016\\Setup.exe")
            ins_comp("Office 2016")

        elif app_secim=="4":
            print("Office 365 Kuruluyor...")
            os.system("o365\setup.exe /configure o365/config.xml")
            ins_comp("Office 365")

        elif app_secim=="5":
            print("Acrobat PDF Kuruluyor...")
            os.system("PDF.exe /sAll")
            ins_comp("Acrobat PDF")

        elif app_secim=="6":
            print("Anydesk Kuruluyor...")
            os.system("Anydesk.msi -quiet")
            ins_comp("Anydesk")

        elif app_secim=="7":
            print("Hepsi Kuruluyor.Office versiyonu 2016.Islem Uzun surecek!")
            print("1/5 Winrar Kuruluyor...")
            os.system("Winrar.exe /s")
            ins_comp("Winrar")
            print("2/5 Chrome Kuruluyor...")
            os.system("Chrome.exe /silent /install")
            ins_comp("Chrome")
            print("3/5 Office 2016 Kuruluyor...")
            os.system("Office_2016\\Setup.exe")
            ins_comp("Office 2016")
            print("4/5 Acrobat PDF Kuruluyor...")
            os.system("PDF.exe /sAll")
            ins_comp("Acrobat PDF")
            print("5/5 Anydesk Kuruluyor...")
            os.system("Anydesk.msi -quiet")
            ins_comp("Anydesk")

        elif app_secim=="8":
            print("Hepsi Kuruluyor.Office versiyonu 365.Islem Uzun surecek!")
            print("1/5 Winrar Kuruluyor...")
            os.system("Winrar.exe /s")
            ins_comp("Winrar")
            print("2/5 Chrome Kuruluyor...")
            os.system("Chrome.exe /silent /install")
            ins_comp("Chrome")
            print("3/5 Office 365 Kuruluyor...")
            os.system("o365\setup.exe /configure o365/config.xml")
            ins_comp("Office 365")
            print("4/5 Acrobat PDF Kuruluyor...")
            os.system("PDF.exe /sAll")
            ins_comp("Acrobat PDF")
            print("5/5 Anydesk Kuruluyor...")
            os.system("Anydesk.msi -quiet")
            ins_comp("Anydesk")

        elif app_secim=="9":
            break
        else:
            give_space()
            continue
        print("Programlarin kurulduguna emin olduktan sonra diger programlari kurabilirsiniz...")
        time.sleep(10)
    
menu="""
       _______  _______    ________________  __ 
      / ___/\ \/ / ___/   / ____/_  __/ __ \/ / 
      \__ \  \  /\__ \   / /     / / / /_/ / /  
     ___/ /  / /___/ /  / /___  / / / _, _/ /___
    /____/  /_//____/   \____/ /_/ /_/ |_/_____/
                                           

    1.Kopyala Yapistir Bat Dosyasi Olustur.
    2.Bilgisayari Domaine Dahil Et.
    3.Bilgisayari Domainden Kaldır.
    4.Local Admin Yetkisi Ver.
    5.Local Kullanici Kaldir.
    6.Program Yukle.
    7.Program Hakkinda Bilgi.
    8.Cikis.
    Secim : """

while True:
    secim=input(menu)
    if secim=="1":
        give_space()
        file_copy_bat()
    elif secim=="2":
        give_space()
        domain_join()
    elif secim=="3":
        give_space()
        remove_domain()
    elif secim=="4":
        give_space()
        local_admin()
    elif secim=="5":
        give_space()
        remove_local()
    elif secim=="6":
        give_space()
        install_apps()
    elif secim=="7":
        give_space()
        print(melih_celik)
        print("\nBu Program Melih Celik tarafından hazirlanmistir.\n")
        time.sleep(5)
    elif secim=="8":
        break
    else:
        print("Yanlis Bir Secim Yaptiniz!!!\nYonlendiriliyorsunuz...")
        time.sleep(5)
    give_space()