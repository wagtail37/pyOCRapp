import PySimpleGUI as sg
from PIL import Image
import pyocr

# OCRエンジンを取得
engines = pyocr.get_available_tools()
engine = engines[0]
builder = pyocr.builders.TextBuilder(tesseract_layout=6)

# GUIのレイアウトを設定
layout = [[sg.Input(key='-FILE-', visible=False, enable_events=True), sg.FileBrowse('ファイルを選択')],
          [sg.Multiline(size=(60, 20), key="-OUTPUT-")],
          [sg.Button('終了')]]

# ウィンドウを作成
window = sg.Window('簡易OCRアプリ', layout)

# イベントループ
while True:
    event, values = window.read()
    
    # ウィンドウが閉じられた場合、または「終了」ボタンが押された場合
    if event == sg.WINDOW_CLOSED or event == '終了':
        break

    # ファイルが選択された場合
    if event == '-FILE-':
        # 選択した画像の文字を読み込む
        txt = engine.image_to_string(Image.open(values['-FILE-']), lang="jpn", builder=builder)
        window["-OUTPUT-"].update(txt)

# ウィンドウを閉じる
window.close()



