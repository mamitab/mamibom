from concurrent.futures import ThreadPoolExecutor, wait
import os
import time

try:
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(send_sms.Dominos),
            executor.submit(send_sms.Englishhome),
            executor.submit(send_sms.Evidea),
            executor.submit(send_sms.File),
        wait(futures)
except KeyboardInterrupt:
    os.system("cls||clear")
    print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
    time.sleep(2)
