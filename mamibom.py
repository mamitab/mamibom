from concurrent.futures import ThreadPoolExecutor, wait
import os
import time

try:
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(send_sms.elexushotel),
            executor.submit(send_sms.Akbati),
            executor.submit(send_sms.Ayyildiz),
            executor.submit(send_sms.Baydoner),
            executor.submit(send_sms.Beefull),
            executor.submit(send_sms.Bim),
            executor.submit(send_sms.Bisu),
            executor.submit(send_sms.Bodrum),
            executor.submit(send_sms.Clickme),
            executor.submit(send_sms.Dominos),
            executor.submit(send_sms.Englishhome),
            executor.submit(send_sms.Evidea),
            executor.submit(send_sms.File),
            executor.submit(send_sms.Frink),
            executor.submit(send_sms.Happy),
            executor.submit(send_sms.Hayatsu),
            executor.submit(send_sms.Hey),
            executor.submit(send_sms.Hizliecza),
            executor.submit(send_sms.Icq),
            executor.submit(send_sms.Ipragaz),
            executor.submit(send_sms.Istegelsin),
            executor.submit(send_sms.Joker),
            executor.submit(send_sms.KahveDunyasi),
            executor.submit(send_sms.KimGb),
            executor.submit(send_sms.Komagene),
            executor.submit(send_sms.Koton),
            executor.submit(send_sms.KuryemGelsin),
            executor.submit(send_sms.Macro),
            executor.submit(send_sms.Metro),
            executor.submit(send_sms.Migros),
            executor.submit(send_sms.Naosstars),
            executor.submit(send_sms.Paybol),
            executor.submit(send_sms.Pidem),
            executor.submit(send_sms.Porty),
            executor.submit(send_sms.Qumpara),
            executor.submit(send_sms.Starbucks),
            executor.submit(send_sms.Suiste),
            executor.submit(send_sms.Taksim),
            executor.submit(send_sms.subaro),
            executor.submit(send_sms.Tasdelen),
            executor.submit(send_sms.Tasimacim),
            executor.submit(send_sms.Tazi),
            executor.submit(send_sms.TiklaGelsin),
            executor.submit(send_sms.ToptanTeslim),
            executor.submit(send_sms.Ucdortbes),
            executor.submit(send_sms.Uysal),
            executor.submit(send_sms.Wmf),
            executor.submit(send_sms.Yapp),
            executor.submit(send_sms.YilmazTicaret),
            executor.submit(send_sms.Yuffi),
            executor.submit(send_sms.Akasya)
        ]
        wait(futures)
except KeyboardInterrupt:
    os.system("cls||clear")
    print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
    time.sleep(2)
    
