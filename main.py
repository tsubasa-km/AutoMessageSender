import pyautogui as pag
import keyboard
from time import time

# 定数(適当な秒数)
WAIT_SEC = 5
DURATION = 30/5

t = 0
# キー入力(esc)があるか、時間が終わるまで待つ
def wait(sec,print_=False):
    if keyboard.is_pressed("esc"):return
    start = time()
    while time()-start < sec:
        if keyboard.is_pressed("esc"):return
        if print_:print(f"残り{round(sec-(time()-start),2)}秒")


def main(write_function,message,duration=0,charbychar=False,max_=100):
    global t
    while t < max_:
        if keyboard.is_pressed("esc"):return
        # 一文字ずつ送信するかそのまま送信するか
        if charbychar or type(message)==list or type(message)==tuple:
            for c in message:
                if keyboard.is_pressed("esc"):return
                write_function(c,duration)
                t+=1
        else:
            write_function(message,duration)
            t+=1

# 文字列をそのまま送信
def nomal(message,duration):
    pag.typewrite(message)
    pag.hotkey("enter")
    wait(duration)

# 文字列を日本語に変換して送信
def nomal_ja(message,duration):
    pag.hotkey('hanja')
    pag.typewrite(message)
    pag.hotkey("enter")
    pag.hotkey("enter")
    pag.hotkey('hanja')
    wait(duration,True)


# カウントダウン
for i in range(WAIT_SEC + 1)[::-1]:
    wait(1)
    print(f"送信開始まで : {i}秒")

main(nomal_ja,["a","i","si","te","ru"],DURATION)

print(f"\n\n送信回数 : {t}\n\n")