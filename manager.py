from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep
import time
import webbrowser  
import os
init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]
scam = '@notoscam'
try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo
    b = [
    
' ___      _   _     _   _______   _       _______   _ ',
'|   \    | | | |   | | |   ____| | |     |   ____| | |',
'| |\ \   | | | |   | | |  |      | |     |  |_     | |',
'| | \ \  | | | |   | | |  |      | |     |   _|    | |',
'| |  \ \ | | | |   | | |  |      | |     |  |      | |',
'| |   \ \| | | |___| | |  |____  | |___  |  |____  | |',
'|_|    \___| |_______| |_______| |_____| |_______| |_|',
    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    #print('=============SON OF GENISYS==============')
    print(f'   Version: 0.9 | Author: @Helloo_Hii{n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] Add new accounts'+n)
    print(lg+'[2] Filter all banned accounts'+n)
    print(lg+'[3] Delete specific accounts'+n)
    print(lg+'[4] Update your Astra'+n)
    print(lg+'[5] Display All Accounts'+n)
    print(lg+'[6] Report Scam'+n)
    print(lg+'[7] Quit'+n)
    a = int(input('\nEnter your choice: '))
    if a == 1:
        input("termux-open-url https://youtu.be/k4Az47agzvw")
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg} [~] Enter number of accounts to add: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg} [~] Enter Phone Number: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [i] Saved all accounts in vars.txt')
            clr()
            print(f'\n{lg} [*] Logging in from new accounts\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                c.start(number)
                print(f'{lg}[+] Login successful')
                c.disconnect()
            input(f'\n Press enter to goto main menu...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] There are no accounts! Please add some and retry')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{lg}[+] {phone} is not banned{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' is banned!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Congrats! No banned accounts')
                input('\nPress enter to goto main menu...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] All banned accounts removed'+n)
                input('\nPress enter to goto main menu...')

    elif a == 3:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[i] Choose an account to delete\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Enter a choice: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Account Deleted{n}')
        input(f'\nPress enter to goto main menu...')
        f.close()
    elif a == 4:
        # thanks to github.com/th3unkn0n for the snippet below
        print(f'\n{lg}[i] Checking for updates...')
        try:
            # https://raw.githubusercontent.com/Cryptonian007/Astra/main/version.txt
            version = requests.get('https://raw.githubusercontent.com/Cryptonian007/Astra/main/version.txt')
        except:
            print(f'{r} You are not connected to the internet')
            print(f'{r} Please connect to the internet and retry')
            exit()
        if float(version.text) > 1.1:
            prompt = str(input(f'{lg}[~] Update available[Version {version.text}]. Download?[y/n]: {r}'))
            if prompt == 'y' or prompt == 'yes' or prompt == 'Y':
                print(f'{lg}[i] Downloading updates...')
                if os.name == 'nt':
                    os.system('del add.py')
                    os.system('del manager.py')
                else:
                    os.system('rm add.py')
                    os.system('rm manager.py')
                #os.system('del scraper.py')
                os.system('curl -l -O https://raw.githubusercontent.com/Cryptonian007/Astra/main/add.py')
                os.system('curl -l -O https://raw.githubusercontent.com/Cryptonian007/Astra/main/manager.py')
                print(f'{lg}[*] Updated to version: {version.text}')
                input('Press enter to exit...')
                exit()
            else:
                print(f'{lg}[!] Update aborted.')
                input('Press enter to goto main menu...')
        else:
            print(f'{lg}[i] Your Astra is already up to date')
            input('Press enter to goto main menu...')
    elif a == 5:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        print(f'\n{cy}')
        print(f'\tList Of Phone Numbers Are')
        print(f'==========================================================')
        i = 0
        for z in accs:
            print(f'\t{z[0]}')
            i += 1
        print(f'==========================================================')
        input('\nPress enter to goto main menu')
    elif a == 6:
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        
        #print('\n' + info + lg + ' Checking for banned accounts...' + rs)
        print('\n' ' Checking for banned accounts...' )
        for a in accounts:
            phn = a[0]
            print(f'Checking {lg}{phn}')
            clnt = TelegramClient(f'sessions/{phn}', 8027196 , '9b70b20efd67e9b99edc395d78407cfa')
            clnt.connect()
            banned = []
            if not clnt.is_user_authorized():
                try:
                    clnt.send_code_request(phn)
                    print('kk')
                except PhoneNumberBannedError:
                    print(f'{error} {w}{phn} {r}is banned!{rs}')
                    banned.append(a)
            for z in banned:
                accounts.remove(z)
                print('{lg}Banned account removed[Remove permanently using manager.py]{rs}')
            time.sleep(0.5)
            clnt.disconnect()
        print(' Sessions created!')
        clr()
        banner()
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break
        print(f'{lg} Total accounts: {w}{len(accounts)}')
        number_of_accs = int(input(f'{cy} Enter number of accounts to Report: {r}'))
        choice = str(input(f'{cy} Send Message For Report {r}'))
        to_use = [x for x in accounts[:number_of_accs]]
        for l in to_use: accounts.remove(l)
        with open('vars.txt', 'wb') as f:
            for a in accounts:
                pickle.dump(a, f)
            for ab in to_use:
                pickle.dump(ab, f)
            f.close()
        sleep_time = 1
        print(f'{lg} -- Sending Reports from {w}{len(to_use)}{lg} account(s) --')   
        send_status = 0
        
        approx_members_count = 0
        index = 0
        for acc in to_use:
            stop = index + 60
            c = TelegramClient(f'sessions/{acc[0]}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
            print(f'User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
            c.start(acc[0])
            acc_name = c.get_me().first_name
            try:
                c.send_message(scam,choice)
                print(f'Report Done From: {cy}{acc_name}{lg}  To Notoscam-- ')
                send_status += 1
            except Exception as e:
                print(f'{e}')
                continue
        if send_status != 0:
            print(f"\n{lg}session ended")
            input(f'\n{cy} Press enter to exit...')
        else:
            print(f"\n{lg}All reports done sucesfully")
            input(f'\n{cy} Press enter to exit...')
        
    elif a == 7:
        clr()
        banner()
        exit()