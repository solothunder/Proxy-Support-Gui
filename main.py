import PySimpleGUI as sg
import subprocess
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
                       [sg.Text('もし設定を変更したい場合は/etc/nginx/nginx.conf（Nginx本体ファイル）', font=('Noto Serif CJK JP',13))],
                       [sg.Text('/home/nginx/out.conf（プロキシ出力ポートファイル）', font=('Noto Serif CJK JP',13))],
                       [sg.Text('/home/nginx/in.conf（マイクラサーバー入力側IP・ポートファイル）から変更できます。', font=('Noto Serif CJK JP',13))],
                       [sg.Button('戻る', key='install-cre-button')]
         ]
 return sg.Window('Proxy Support Gui', install_cre_layout, finalize=True, size=(750, 250))

def layout_main():
 layout = [[sg.Text('Proxy Support Gui By Linux', font=('Noto Serif CJK JP',27))],
         [sg.Text('セットアップをする前にいかの注意事項をお読みください')],
         [sg.Text('ここではVPSなどでマインクラフトのDOS、DDOS対策などのプロキシ設定を支援するものです。')],
         [sg.Text('※このプログラムで問題が発生しても責任は負いません。')],
         [sg.Text('ここではaptを使います。CentOSではデフォルトではないので（だと思うので）/n yum install apt などでaptを入れてください。')],
         [sg.Button('今すぐセットアップ', key='setup-button')] ]
# ウィンドウを作成する
 return sg.Window('Proxy Support Gui', layout, finalize=True, size=(750, 250))

def layout_sub():
 install_info_layout = [[sg.Text('情報を入力してください', font=('Noto Serif CJK JP',27))],
         [sg.Text('SSHポート（例：22）'), sg.Input(key='sshportnum')],
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
     window = layout_apt()
    elif event == "apt-setup-button":
     window.close()
     window = layout_sub()
    elif event == "no-apt-setup-button":
     window.close()
     window = layout_main()
    elif event == "info-setup-button":
        window.close()
        window = layout_install_now()
        sshportnum = values['sshportnum']
        outportnum = values['outportnum']
        inportf = values['inportf']
        inip = values['inip']


# apt インストール同意するか？

# apt入れた？

        
# ディレクトリ削除・ファイル削除
        res = subprocess.call("sudo rm -r /home/nginx", shell=True)
        res = subprocess.call("rm -r nginx-1.18.0.tar.gz", shell=True)
        res = subprocess.call("rm -r nginx-1.18.0/", shell=True)
# ファイル上書き
        inipporthea = open("data/file/inipport.txt","w")
        inipporthea.write("server ")
        inipporthea.close()
# コマンド実行
        print('NginxとUfwを入れます。')
        res = subprocess.call("sudo apt update && sudo apt upgrade -y", shell=True)
        res = subprocess.call("sudo apt install gcc", shell=True)
        res = subprocess.call("sudo apt install build-essential -y", shell=True)
        res = subprocess.call("wget https://nginx.org/download/nginx-1.18.0.tar.gz", shell=True)
        res = subprocess.call("tar -zxvf nginx-1.18.0.tar.gz", shell=True)
#        res = subprocess.call("cd nginx-1.18.0", shell=True)
        res = subprocess.call("cd nginx-1.18.0/ && ./configure --with-stream --without-http_rewrite_module --without-http_gzip_module", shell=True)
        res = subprocess.call("cd nginx-1.18.0/ && make", shell=True)
        res = subprocess.call("cd nginx-1.18.0/ && sudo make install", shell=True)
# ポート テキスト保存
# UFWコマンド＋ポート 変数格納
        ufwsshportfile = "sudo ufw allow "+str(sshportnum)
        ufwoutportfile = "sudo ufw allow "+str(outportnum)
# コマンド実行
        res = subprocess.call(str(ufwsshportfile), shell=True)
        res = subprocess.call(str(ufwoutportfile), shell=True)
        res = subprocess.call("sudo ufw enable", shell=True)
        res = subprocess.call("sudo ufw reload", shell=True)
        os.makedirs('/home/nginx')
        inipportpath = '/home/nginx/in.conf'
        outipportpath = '/home/nginx/out.conf'
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
        infi = open('/home/nginx/in.conf','a')
        infi.write("server "+str(inip)+":"+str(inportf)+";")
        infi.close()

#        infitwo = open('/home/nginx/in.conf','a')
#        infitwo.write(":", (inport), ";")
#        infitwo.close()        


        outfi = open('/home/nginx/out.conf','w')
        outfi.write("listen     "+str(outportnum)+"; \n proxy_pass mcserver;")
        outfi.close()
# nginx.conf上書き
        nginxsamplefile = open('data/nginxfile/nginx.conf', 'r') 
        contents = nginxsamplefile.read()
        nginxfile = open('/usr/local/nginx/conf/nginx.conf','w')
        nginxfile.write(str(contents))
        nginxfile.close()
        nginxsamplefile.close()
# nginx.service作成＆上書き
        nginxservicesamplefile = open('data/file/nginx.service', 'r') 
        servicecontents = nginxservicesamplefile.read()
        nginxservicefile = open('/usr/lib/systemd/system/nginx.service','w')
        nginxservicefile.write(str(servicecontents))
        nginxservicefile.close()
        nginxservicesamplefile.close()
# Nginx再起動
        res = subprocess.call("sudo systemctl daemon-reload", shell=True)
        res = subprocess.call("sudo systemctl restart nginx", shell=True)
#        res = subprocess.call("sudo systemctl status nginx", shell=True)

        window.close()
        window = layout_install_cre()

    elif event == "install-cre-button":
         window.close()
         window = layout_main()



window.close()    