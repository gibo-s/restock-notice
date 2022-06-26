!pip install requests
import requests

#必要な変数を設定
#取得したトークン
TOKEN = ''
#APIのURL
api_url = 'https://notify-api.line.me/api/notify'
#通知内容１
send_content_01 = 'まだ入荷待ちだよ。'
send_content_02 = '再入荷したよ。'

#情報を辞書型にする
TOKEN_dic = {'Authorization':'Bearer' + ' ' + TOKEN}
send_dic_01 = {'message': send_content_01}
send_dic_02 = {'message': send_content_02}

#webdriverのインストール
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

#webdriverのインストール
from selenium import webdriver

#sleepメソッドのインポート
from time import sleep

#webdriver managerのインストール・インポート
sleep(3)
from webdriver_manager.chrome import ChromeDriverManager
 

# ブラウザーを起動(ヘッドレスにする記述)
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

# 商品ページにアクセス
driver.get('https://~')

sleep(1)

if len(driver.find_elements_by_class_name("is-disabled")) > 0:
    requests.post(api_url,headers=TOKEN_dic,data=send_dic_01)
else:
    requests.post(api_url,headers=TOKEN_dic,data=send_dic_02)

# ブラウザーを終了
driver.quit()

