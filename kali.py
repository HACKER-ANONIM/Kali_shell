import os
import time
import socket
import requests
import webbrowser 
import platform
import subprocess
import shutil
import sys 
import requests
from datetime import datetime
            

                  
                

def main():
    while True:
        print( "CONSOL@HACKER-kali@linux" )
        print(""" 
                            ██
                    
    ██╗  ██╗ █████╗ ██╗     ██╗
    ██║ ██╔╝██╔══██╗██║     ██║
    █████╔╝ ███████║██║     ██║
    ██╔═██╗ ██╔══██║██║     ██║
    ██║  ██╗██║  ██║███████╗██‖
    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝══╝
            
            ██
             
    ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗
    ██║     ██║████╗  ██║╚██╗ ██╔╝╚██╗██╔╝
    ██║     ██║██╔██╗ ██║ ╚████╔╝  ╚███╔╝
    ██║     ██║██║╚██╗██║  ╚██╔╝   ██╔██╗
    ███████╗██║██║ ╚████║   ██║   ██╔╝ ██╗
    ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝



    """)

       
        print("comand list: 1-open:search Enter а потом >>> сылка на сайт ")
        print("comand list: 2-ping: Enter затем  сылку на сайт")
        print("comand list: 3-ip_func: ваш IP")
        print("comand list: 4-wireshark: ")
        print("comand list: 5-nmap: ")
        print("comand list: 6-top: процесы" )
        print("comand list: 7-htop: диспечер задачь")
        print("comand list: 9-skript:OS  скрипт для быстрого управления OS [В МЕСТО  КОМАНДЫ А ЧИСЛА ДЛЯ ПРОСТОТЫ ]")
        print("comand list: O exit: выход ")
        print("comand list: MR.ROBOT")



        command = input("kali@linux~# >>> ")

        if command == "exit:":
            break


        if command == "open:search": #1 команда для открытия сылок
            url = input("⟪consol⟫  >>> адрес сайта:" )
            webbrowser.open(url)
            input("\nНажмите Enter для продолжения...")    
             
        elif command == "ping:": #2 для пинга сылки пороверки активности сайта 
            target = input("⟪consol⟫  >>> адрес сайта:")
            print(f"\nПроверяю {target}...")

            param_count = "-n" if platform.system().lower() == "windows" else "-c"
            command = ["ping", param_count, "4", target]

            try:
                result = subprocess.run(command, capture_output=True, text=True, encoding="cp866", timeout=10)
                print(result.stdout)
                if result.returncode == 0:
                    print(f"✅ {target} АКТИВЕН")
                else:
                    print(f"❌ {target} НЕ АКТИВЕН")
            except subprocess.TimeoutExpired:
                print(f"⏱️ Превышено время ожидания.")
            except UnicodeDecodeError:
                subprocess.run(command)
            except Exception as e:
                print(f"⚠️ Ошибка: {e}")
            input("\nНажмите Enter для продолжения...")
        elif command == "ip_func:": # 3 команда простая для того чтобы узнать IP
            ip = os.system("ipconfig")
            print(ip)
            input("\nНажмите Enter для продолжения...")
                      
                         
          
        
        
        elif command == "top:":
            try:
                result = subprocess.run(["powershell", "-Command", "Get-Process"],capture_output=True,text=True,timeout=10)
                print(result.stdout)
            except Exception as e:
                print(f"Ошибка: {e}")
            input("\nНажмите Enter для продолжения...")    
        elif command == "htop:":
            print(" ========= открытие диспечер задачь =========")
            time.sleep(3)
            if platform.system() == "Windows":
                subprocess.run(["taskmgr.exe"])
            else:
                print("htop работает только в Windows.")    
            print("диспечер задачь открыт >....")
            print()
            input("\nНажмите Enter для продолжения...")
             
        elif command == "MR.ROBOT":
            print("\033[92m" + r"""
             __  __            __ ____   ______   _______      _______   ____________
            |  \/  |          |   >___| /      \  /       \   /       \  |____    ____|
            | \  / |  _ __    |   |     |      |  |        /   |       |       |  |
            | |\/| | | '__|   |   |     |      |  |========    |       |       |  |
            | |  | | | |      |   |     |      | |        \   |       |       |  |
            |_|  |_| |_|    * |___|     \______/  |________/   \_______/       |__|        

            """ + "\033[0m")
            webbrowser.open("https://www.bing.com/images/search?view=detailV2&ccid=qx0GhH0i&id=A2D8D7F42FE6509CF17418AD7CB164FC321FC34C&thid=OIP.qx0GhH0ib8UtmCRN3R4P4wHaFj&mediaurl=https%3a%2f%2fm.media-amazon.com%2fimages%2fS%2fpv-target-images%2fd0542d296dd3dbb63bcb56b9b2c1973b21575c011c64750430576ef76d0fb367.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.ab1d06847d226fc52d98244ddd1e0fe3%3frik%3dTMMfMvxksXytGA%26pid%3dImgRaw%26r%3d0&exph=1920&expw=2560&q=mr.robot&FORM=IRPRST&ck=0DCA20174D6B925EED451F0DFD52ECA6&selectedIndex=11&itb=0")
            webbrowser.open("https://www.bing.com/ck/a?!&&p=9e7072aced5840b75c67eea9b6bf0fbbe8a3455d56e50115c24bf9270238c79aJmltdHM9MTc4MzIwOTYwMA&ptn=3&ver=2&hsh=4&fclid=048dcdd4-8bbb-6f7a-2d43-db6e8af16e0e&psq=mr.robot&u=a1aHR0cHM6Ly9ydXR1YmUucnUvcGxzdC85MTQ4MTcv")
            input("\nНажмите Enter для продолжения... 5 сезон ? error404 NOT FUND")
                                                                
        elif command == "skript:OS": 
            # Внутри обработки команды "skript:OS"
         base_dir = os.path.dirname(os.path.abspath(__file__))
         target_script = os.path.join(base_dir, "SKRIPT", "skriptOS.py")

         if not os.path.exists(target_script):
            print(f"Файл не найден: {target_script}")
            print("Проверь, что skriptOS.py лежит в папке SKRIPT")
         else:
            subprocess.Popen([sys.executable, target_script], creationflags=subprocess.CREATE_NEW_CONSOLE)   # ✅ ПРАВИЛЬНО *надеюсь
            print("Скрипт запущен в новом окне!")
        elif command == "wireshark:":
            print("⟪consol⟫  >>> |open wireshark|")
            time.sleep(2)
            print("❇️SCANING❇️")
            wireshark_path = r"C:\Program Files\Wireshark\Wireshark.exe"

            if os.path.exists(wireshark_path):
                subprocess.run([wireshark_path])   
                print("✅wireshark найден✅")
                print("♾️СКАНИРОВАНИЕ ТРАФИКА♾️")
                time.sleep(3)
            else:
                print("❌wireshark не найден❌.")  
                print("⚠️УСТАНОВИТЕ WIRESHARK⚠️.") 
            input("\nНажмите Enter для продолжения... ╰(*°▽°*)╯")
        elif command == "nmap:":
            print("⟪consol⟫  >>> |open nmap|")
            print("🔎NMAP🔍")
            base_dir = os.path.dirname(os.path.abspath(__file__))
            maper = os.path.join(base_dir, "skript", "Nmap.py")
            subprocess.run(["python",maper])
        
        elif command == "vpn:":
            print("vpn kiler DIP")
            subprocess.run([])
   

    
         
            

           





    
   

           
            
                       
     




       




           
if __name__ == "__main__":
    main()

        

    




         



    






    

















   




    




