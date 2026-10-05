<div align="center">
  <лого>
   
  
  <h1>Kali Shell 🐉</h1>
  <p><b>Мощная интерактивная оболочка для автоматизации пентеста и сетевых операций.</b></p>


  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Kali_Linux-purple.svg" alt="Platform">
  <img src="https://img.shields.io/badge/Docker-Supported-blue.svg" alt="Docker">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="Status">
  <img src="https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white" alt="Windows 11">
</div>

---

## 📖 О проекте
**Kali Shell** — это удобный CLI-интерфейс, который объединяет в себе популярные инструменты для пентеста и сетевых манипуляций. Вместо того чтобы запоминать сотни флагов и команд, вы запускаете один скрипт и выбираете нужное действие в интерактивном меню. Проект поддерживает работу с Docker, Heroku и имеет встроенные механизмы блокировки/маршрутизации трафика.

## ✨ Возможности
- 🚀 **Nmap:** Быстрый запуск сканирования через встроенный модуль `Nmap.py`.
- 🛡️ **VPN Killer / Управление IP:** Проверяйте активность ip подключения и узнайте свой ip и другие даные через ping:,nmap:,wireshark:,ip_func: .
- 🌐 **Proxy Support:** Конфигурации для `shadowsocks-libev` и `nginx`.
- ✳️ **skript:OS** контроль ОС
- 🎨 **Интерактивное меню:** Удобная навигация по командам (`nmap`, `vpn` и др.).
- VPN ПОКА НЕ РАБОТАЕТ (ЗАГОТОВКА)
- 🔎**modem:consol** в консоли будут доавлятся запуск других проектов (лежат в папке .github)
- ❇️**PENTEST** Ваш помошник в работе с сетью и пентэстом 

## 👁️‍🗨️ Работа nmap:
<img width="1379" height="761" alt="Снимок экрана 2026-10-05 184011" src="https://github.com/user-attachments/assets/f178c40c-11b5-49cb-9b85-07ec0b607796" />


## ❇️ Работа skript:OS







## 🚀 Быстрый старт

### Windows установка
1) скачайте python: https://www.python.org/downloads/release/python-31012/
2) скачайте сам проект с github: https://github.com/HACKER-ANONIM/Kali_shell
3) установите wireshark (если хотите чтоб работала функция wireshark:)
4) запустите kali.ру

### Внимание програма заточена имено под windows как перенос утилит для network с kalli на windows 

### Большенство функций особено для взоимодействия с ОС не работуют на Linux 

### Linux установка
```bash

# Клонируем репозиторий
git clone https://github.com/HACKER-ANONIM/Kali_shell.git
cd Kali_shell
скачайте python: https://www.python.org/downloads/release/python-31012/

# Устанавливаем зависимости (если есть requirements.txt)
pip install -r requirements.txt (зависимостей пока нет)

# Запускаем главный скрипт
python kali.py
