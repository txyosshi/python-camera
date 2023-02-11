from PIL import Image
import cv2
import time
import sys
import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
	print("No OCR tool found")
	sys.exit(1)
tool = tools[0]

#VideoCaptureクラス
#
#メソッド
#
#read() 1コマ分の画像データ読み込み
#release() デバイスリリース（動画ファイルの場合ファイルクローズも行う）

cap = cv2.VideoCapture(1)

#whileがあるので、cap.read()がtrue（画像データが読み取れている）間はframeにデータを格納
#aaaはtrue/falseを格納する変数（通常はretと書くみたい）
last_txt = ""

while(True):
	aaa, frame = cap.read()
	#cv2.imshow()はOpenCVで用意されているコマンド
	#cv2.imshow('フレーム名',画像を格納している変数（=frame）

	#Pythonは最初からn番目までの要素を取得するときは[:n]と書く
	#shapeの戻り値は横サンプル、縦サンプル、チャンネル数（カラーの場合）
	orgHeight, orgWidth = frame.shape[:2]

	#画像サイズを小さくする
	size = (int(orgWidth/2), int(orgHeight/2))

	#解析しやすいようグレースケールにする
	glay = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#画像をリサイズ
	image = cv2.resize(glay,size)

	#読み取り結果をtesseractを使ってテキスト表示
	txt = tool.image_to_string(Image.fromarray(image),lang="jpn",builder=pyocr.builders.TextBuilder())
	if len(txt) != 0 and txt != last_txt:
	        last_txt = txt
        	print( txt )

	cv2.imshow('frame',image)	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#whileを抜けたらリリース
cap.release()
#フレームを閉じる
cv2.destroyAllWindows()