from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import tkinter
from selenium import webdriver
from tkinter import messagebox


class ogrenci():
    ogrNo = " "
    ogrSifre = " "


def can_login():
    if driver.current_url[: 50] == giris_url:
        return 1
    else:
        messagebox.showinfo("Başarılı", "Öğrenbi bilgi sistemine giriş yapılmıştır.")
        return 0


def giris():
    driver.get("https://ogr.kocaeli.edu.tr/KOUBS/Ogrenci/index.cfm")


def repeat_login():
    while can_login():
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'Ara')))
            print("Sayfa giriş yapmaya hazır! ")
            driver.find_element_by_name("OgrNo").send_keys(ogrenci.ogrNo)
            driver.find_element_by_name("Sifre").send_keys(ogrenci.ogrSifre)
            driver.find_element_by_xpath("//*[@id='Ara']").click()

        except TimeoutException:
            print
            "Sayfa Yüklemesi Uzun Sürüyor"
            repeat_login()


def deger_ata(ogrNo, ogrSifre):
    ogrenci.ogrNo = ogrNo
    ogrenci.ogrSifre = ogrSifre
    repeat_login()


def gui():
    window = tkinter.Tk()
    window.geometry("400x300")
    window.title('Obs Giris Programı')
    mycolor = '#%02x%02x%02x' % (132, 244, 255)
    window.configure(background=mycolor)

    numara = tkinter.Label(window, text="Ogrenci Numaraniz")
    numara.place(x=15, y=30)
    numara_gir = tkinter.Entry(window)
    numara_gir.place(x=175, y=30)

    sifre = tkinter.Label(window, text="Ogrenci Sifreniz")
    sifre.place(x=15, y=80)
    sifre_gir=tkinter.Entry(window)
    sifre_gir.place(x=175, y=80)

    buton=tkinter.Button(window, text="Giris", command=lambda: deger_ata(numara_gir.get(), sifre_gir.get()))
    buton.place(x=175, y=130)

    bilgilendirme=tkinter.Label(window,text="Obs sistemine giris programi bilgilerinizi asla kaydetmez. \n Yalnizca giris aninda ihtiyac duyar.")
    bilgilendirme.place(x=40, y=200)

    window.mainloop()


giris_url="https://ogr.kocaeli.edu.tr/KOUBS/Ogrenci/index.cfm"
driver = webdriver.Chrome()
giris()
gui()







