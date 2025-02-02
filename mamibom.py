from concurrent.futures import ThreadPoolExecutor, wait
import os
import time
from sms import SendSms  # Make sure to import the SendSms class

# Example phone number and email
phone_number = "5551234567"
email = "example@gmail.com"

# Create an instance of SendSms
send_sms = SendSms(phone_number, email)

try:
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(send_sms.Trendyol),
            executor.submit(send_sms.Getir),
            executor.submit(send_sms.Dsmart),
            executor.submit(send_sms.Uber),
            executor.submit(send_sms.Kimgbister),
            executor.submit(send_sms.asiselektronik),
            executor.submit(send_sms.Evidea),
            executor.submit(send_sms.Dominos),
            executor.submit(send_sms.Englishhome),
            executor.submit(send_sms.Evidea),
            executor.submit(send_sms.File)
        ]
        wait(futures)
except KeyboardInterrupt:
    os.system("cls||clear")
    print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
    time.sleep(2)
