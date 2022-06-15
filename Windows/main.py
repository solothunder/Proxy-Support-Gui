import PySimpleGUI as sg
import subprocess
import shutil
import wget
from subprocess import PIPE
import os
# coding: utf-8
# Your code here!

def layout_apt():
 apt_layout = [[sg.Text('aptは入れましたか？', font=('Noto Serif CJK JP',27))],
         [sg.Text('入っていない場合は yum install apt などで入れてください。')],
         [sg.Button('はい', key='apt-setup-button'), sg.Button('いいえ', key='no-apt-setup-button')]
         ]
 return sg.Window('Proxy Support Gui', apt_layout, finalize=True, size=(750, 250))

def layout_install_now():
 install_now_layout = [[sg.Text('インストール中です。', font=('Noto Serif CJK JP',27))],
         ]
 return sg.Window('Proxy Support Gui', install_now_layout, finalize=True, size=(750, 250))

def layout_install_cre():
 install_cre_layout = [[sg.Text('インストール完了しました。', font=('Noto Serif CJK JP',27))],
                       [sg.Text('もし設定を変更したい場合は C:/nginx/conf/nginx.conf（Nginx本体ファイル）', font=('Noto Serif CJK JP',13))],
                       [sg.Text('C:/nginxse/out.conf（プロキシ出力ポートファイル）', font=('Noto Serif CJK JP',13))],
                       [sg.Text('C:/nginxse/in.conf（マイクラサーバー入力側IP・ポートファイル）から変更できます。', font=('Noto Serif CJK JP',13))],
                       [sg.Button('戻る', key='install-cre-button')]
         ]
 return sg.Window('Proxy Support Gui', install_cre_layout, finalize=True, size=(750, 250))

def layout_main():
 layout = [[sg.Text('Proxy Support Gui By Windows', font=('Noto Serif CJK JP',27))],
         [sg.Text('このプログラムはWindows専用です。 管理者権限で実行してください')],
         [sg.Text('セットアップをする前にいかの注意事項をお読みください')],
         [sg.Text('ここではWindows Server VPSなどでマインクラフトのDOS、DDOS対策などのプロキシ設定を支援するものです。')],
         [sg.Text('※このプログラムで問題が発生しても責任は負いません。')],
         [sg.Button('今すぐセットアップ', key='setup-button')] ]
# ウィンドウを作成する
 return sg.Window('Proxy Support Gui', layout, finalize=True, size=(750, 250))

def layout_sub():
 install_info_layout = [[sg.Text('情報を入力してください', font=('Noto Serif CJK JP',27))],
         [sg.Text('出力ポート（例：25565 80 443）'), sg.Input(key='outportnum')],
         [sg.Text('サーバーのグローバルサーバーIPもしくはプライベートIP（同じネットワーク上のみ）を入力してください。')],
         [sg.Text('（グローバルIPの場合の例：182.22.25.124(Yahho))')],
         [sg.Input(key='inip')],
         [sg.Text('サーバーのポートを入力してください。（例：25565 80 443）'), sg.Input(key='inportf')],
         [sg.Button('今すぐセットアップ', key='info-setup-button')]]
 return sg.Window('Proxy Support Gui', install_info_layout, finalize=True, size=(750, 250))
 

window = layout_main()
# ウィンドウを表示し、対話する
while True:
   # イベントの読み込み
    event, values = window.read()
   # ウィンドウの×ボタンが押されれば終了
    if event == sg.WIN_CLOSED or event == "Exit":
       break
   # ボタン操作時のアクション
    elif event == "setup-button":
     window.close()
     window = layout_sub()
    elif event == "no-apt-setup-button":
     window.close()
     window = layout_main()
    elif event == "info-setup-button":
        window.close()
        window = layout_install_now()
        outportnum = values['outportnum']
        inportf = values['inportf']
        inip = values['inip']


# apt インストール同意するか？

# apt入れた？

        
# ディレクトリ削除・ファイル削除
        if os.path.isdir("C:\\nginx"):
         shutil.rmtree("C:\\nginx")
         pass
        else:
         if os.path.isdir("C:\\nginxse"):
          shutil.rmtree("C:\\nginxse")
          pass
         else:
#        res = subprocess.call("rd C:\nginxse", shell=True)
#        res = subprocess.call("rd C:\nginx", shell=True)
#        res = subprocess.call("rm -r nginx-1.18.0/", shell=True)
# コマンド実行
          print('Nginxを入れます。')
#        res = subprocess.call("sudo apt update && sudo apt upgrade -y", shell=True)
#        res = subprocess.call("sudo apt install gcc", shell=True)
#        res = subprocess.call("sudo apt install build-essential -y", shell=True)
#        res = subprocess.call("wget https://nginx.org/download/nginx-1.18.0.tar.gz", shell=True)
#        res = subprocess.call("tar -zxvf nginx-1.18.0.tar.gz", shell=True)
#        res = subprocess.call("cd nginx-1.18.0", shell=True)
#        res = subprocess.call("cd nginx-1.18.0/ && ./configure --with-stream --without-http_rewrite_module --without-http_gzip_module", shell=True)
#        res = subprocess.call("cd nginx-1.18.0/ && make", shell=True)
#        res = subprocess.call("cd nginx-1.18.0/ && sudo make install", shell=True)
# Nginx Zip ダウンロード
        site_url = 'http://nginx.org/download/nginx-1.18.0.zip'
        file_name = wget.download(site_url)
        print(file_name)
# zip 解凍
        shutil.unpack_archive('nginx-1.18.0.zip', 'nginx-1.18.0')
# nginxファイルコピー
        shutil.copytree('nginx-1.18.0','c:\\nginx')
# UFWコマンド＋ポート 変数格納
        ufwoutportfile = 'netsh advfirewall firewall add rule name="Proxy Support outport" dir=in action=allow protocol=tcp localport='+str(outportnum)+' profile=private,public localip=any'
        ufwoutportfiletwo = 'netsh advfirewall firewall add rule name="Proxy Support outport2" dir=out action=allow protocol=tcp localport='+str(outportnum)+' profile=private,public localip=any'
        
# コマンド実行
        res = subprocess.call(str(ufwoutportfile), shell=True)
        res = subprocess.call(str(ufwoutportfiletwo), shell=True)
#        res = subprocess.call("sudo ufw enable", shell=True)
#        res = subprocess.call("sudo ufw reload", shell=True)
        os.makedirs('C:\\nginxse', exist_ok=True)
        inipportpath = 'C:\\nginxse\in.conf'
        outipportpath = 'C:\\nginxse\out.conf'
        indire = open(inipportpath, 'w')
        indire.write('')  # 
        indire.close()

        outdi = open(outipportpath, 'w')
        outdi.write('')  # 
        outdi.close()
# IP聞く・上書き
#        inipport = open('data/file/inipport.txt','a')
#        inipport.write((inip))
#        inipport.write(":")
#        inipport.close()
#        inipporttwo = open('data/file/inipport.txt','a')
#        inipporttwo.write((inport))
#        inipporttwo.write(";")
#        inipporttwo.close()
#        inipporthe = open('data/file/inipport.txt','r')
# 入力ポート・出力ポート保存ファイル上書き
        infi = open('C:\\nginxse\in.conf','a')
        infi.write("server "+str(inip)+":"+str(inportf)+";")
        infi.close()

#        infitwo = open('/home/nginx/in.conf','a')
#        infitwo.write(":", (inport), ";")
#        infitwo.close()        


        outfi = open('C:\\nginxse\out.conf','w')
        outfi.write("listen     "+str(outportnum)+"; \n proxy_pass mcserver;")
        outfi.close()
# nginx.conf上書き
        nginxsamplefile = open('data/nginxfile/nginx.conf', 'r') 
        contents = nginxsamplefile.read()
        nginxfile = open('C:/nginx/conf/nginx.conf','w')
        nginxfile.write(str(contents))
        nginxfile.close()
        nginxsamplefile.close()
# nginx.service作成＆上書
        nginxservicesamplefile = open('data/file/nginx.bat', 'r', encoding="utf-8") 
        servicecontents = nginxservicesamplefile.read()
        nginxservicefile = open('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/nginx.bat','w')
        nginxservicefile.write(str(servicecontents))
        nginxservicefile.close()
        nginxservicesamplefile.close()
# Nginx再起動
        res = subprocess.call("C:\nginx\nginx.exe -s reload", shell=True)
#        res = subprocess.call("sudo systemctl restart nginx", shell=True)
#        res = subprocess.call("sudo systemctl status nginx", shell=True)

        window.close()
        window = layout_install_cre()

    elif event == "install-cre-button":
         window.close()
         window = layout_main()



window.close()    