import shutil
import os
import platform
import socket
import subprocess


def main():
    while True:
        print("\n" + "=" * 50)
        print("📋 ГЛАВНОЕ МЕНЮ")
        print("=" * 50)
        print("1 — Создать файл")
        print("2 — Удалить файл")
        print("3 — Создать папку")
        print("4 — Удалить папку")
        print("5 — Открыть PythonProject1")
        print("6 — Данные устройства")
        print("7 — Проверка активных IP")
        print("8 — Запуск антивируса")
        print("0 — ВЫХОД")
        print("error 404 and 42")
        print("=" * 50)
        
        choice = input("Введите номер команды >>> ")

        if choice == "0":
            print("👋 До свидания!")
            break  # Выход из цикла

        elif choice == "1":
            filename = input("Введите имя файла: ")
            with open(filename, 'w', encoding='utf-8') as file:
                pass
            print(f"✅ Файл '{filename}' успешно создан.")
            input("\nНажмите Enter для продолжения...")

        elif choice == "2":
            filename = input("Выберите файл для удаления: ")
            if os.path.exists(filename):
                confirm = input(f"Удалить '{filename}'? (да/нет): ")
                if confirm.lower() == 'да':
                    try:
                        os.remove(filename)
                        print(f"✅ Файл '{filename}' удалён.")
                    except Exception as e:
                        print(f"Ошибка: {e}")
                else:
                    print("❌ Удаление отменено.")
            else:
                print("⚠️ Файл не найден. Директива 42 ???")
            input("\nНажмите Enter для продолжения...")

        elif choice == "3":
            dirname = input("Введите имя папки: ")
            try:
                os.mkdir(dirname)
                print(f"✅ Папка '{dirname}' успешно создана.")
            except FileExistsError:
                print(f"⚠️ Папка '{dirname}' уже существует.")
            input("\nНажмите Enter для продолжения...")

        elif choice == "4":
            dirname = input("Выберите папку для удаления: ")
            if os.path.exists(dirname):
                confirm = input(f"Удалить папку '{dirname}'? (да/нет): ")
                if confirm.lower() == 'да':
                    try:
                        shutil.rmtree(dirname)
                        print(f"✅ Папка '{dirname}' удалена. [ДАННЫЕ УДАЛЕНЫ]")
                    except Exception as e:
                        print(f"Ошибка: {e}")
                else:
                    print("❌ Удаление отменено. База данных активна. И жива (=.")
            else:
                print("⚠️ Папка не найдена. ls или cd [путь]")
            input("\nНажмите Enter для продолжения...")

        elif choice == "5":
            print("📂 Открытие PythonProject1...")
            path = "C:/Users/Rick and Morty/PycharmProjects/PythonProject1"
            if os.path.exists(path):
                os.startfile(path)
                print("✅ Папка открыта.")
            else:
                print("⚠️ Путь не найден.")
            input("\nНажмите Enter для продолжения...")

        elif choice == "6":
            print("\n--- 📊 ДАННЫЕ УСТРОЙСТВА ---")
            if hasattr(os, "uname"):
                print(os.uname())
            print(platform.uname())
            try:
                username = os.getlogin()
            except OSError:
                username = os.environ.get('USERNAME')
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            print(f"Имя пользователя: {username}")
            print(f"Имя хоста: {hostname}")
            print(f"IP-адрес: {ip_address}")

            print("\n📋 Запуск Диспетчера задач...")
            subprocess.Popen("taskmgr.exe")

            print("\n📁 Содержимое текущей папки:")
            for entry in os.scandir('.'):
                print(f"  {'📁' if entry.is_dir() else '📄'} {entry.name}")

            print("\n🌐 Активные подключения:")
            subprocess.run("netstat -ano", shell=True)

            print("\n🔧 IP-конфигурация:")
            subprocess.run("ipconfig", shell=True)

            input("\nНажмите Enter для продолжения...")

        elif choice == "7":
            print("\n📡 ПРОВЕРКА АКТИВНЫХ IP")
            target = input("Введите IP-адрес или домен: ")
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

        elif choice == "8":
            print("\n🛡️ АНТИВИРУС (Windows Defender)")
            print("1 — Быстрая проверка")
            print("2 — Полная проверка")
            print("3 — Проверить папку")
            print("4 — Обновить базы")
            print("5 — Статус антивируса")
            print("0 — Назад")

            av_choice = input("Выберите действие >>> ")

            if av_choice == "1":
                print("\n🔍 Быстрая проверка...")
                subprocess.run(r'"C:\ProgramData\Microsoft\Windows Defender\Platform\*\MpCmdRun.exe" -Scan -ScanType 1',
                               shell=True)
                print("✅ Завершено.")
            elif av_choice == "2":
                print("\n🔍 Полная проверка...")
                subprocess.run(r'"C:\ProgramData\Microsoft\Windows Defender\Platform\*\MpCmdRun.exe" -Scan -ScanType 2',
                               shell=True)
                print("✅ Завершено.")
            elif av_choice == "3":
                folder = input("Путь к папке: ")
                if os.path.exists(folder):
                    subprocess.run(
                        f'"C:\\ProgramData\\Microsoft\\Windows Defender\\Platform\\*\\MpCmdRun.exe" -Scan -ScanType 3 -File "{folder}"',
                        shell=True)
                    print("✅ Завершено.")
                else:
                    print("⚠️ Папка не существует.")
            elif av_choice == "4":
                print("\n🔄 Обновление...")
                subprocess.run(r'"C:\ProgramData\Microsoft\Windows Defender\Platform\*\MpCmdRun.exe" -SignatureUpdate',
                               shell=True)
                print("✅ Завершено.")
            elif av_choice == "5":
                print("\n📊 Статус:")
                subprocess.run(
                    'powershell.exe -Command "Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled"',
                    shell=True)
            elif av_choice == "0":
                pass
            else:
                print("⚠️ Неверный выбор. Директива 42.")

            input("\nНажмите Enter для продолжения...")

        elif choice == "42":
            print("🐬 42 — ответ на главный вопрос жизни, вселенной и всего такого.")
            print("Но знаешь ли ты сам вопрос?..")
            input("\nНажмите Enter для продолжения...")

        elif choice == "404":
            print("❌⚠️ 404 — выбор не найден. Пустота ERROR 404 NOT FOUND ⚠️ ♾️")
            input("\nНажмите Enter для продолжения...")

        else:
            print("⚠️ Неверный выбор. Попробуйте снова.")
            input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()



