import cv2
import time

#VideoCaptureクラス
#
#メソッド
#
#read() 1コマ分の画像データ読み込み
#release() デバイスリリース（動画ファイルの場合ファイルクローズも行う）


#インスタンス化
#引数はWindowsのカメラデバイス番号
#1台接続の場合0を指定
#cap = cv2.VideoCapture(1)

#動画の場合はファイル名を指定する
cap = cv2.VideoCapture('./sample.mp4')


#動画の場合元ファイルのFPSでウェイトを入れる必要がある
#これをやらないと再生スピードが変わるので
#CAP_PROP_FPSでFPSを取得して格納しておく

fps = cap.get(cv2.CAP_PROP_FPS)

#whileがあるので、cap.read()がtrue（画像データが読み取れている）間はframeにデータを格納
#aaaはtrue/falseを格納する変数（通常はretと書くみたい）

while(True):
	aaa, frame = cap.read()
	#cv2.imshow()はOpenCVで用意されているコマンド
	#cv2.imshow('フレーム名',画像を格納している変数（=frame）

	#表示サイズを変更
	resize = cv2.resize(frame,(960,540))

	#ウェイトを入れる
	time.sleep(1/fps)
	#リサイズして表示する
	cv2.imshow('frame',resize)
	
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#whileを抜けたらリリース
capture.release()
#フレームを閉じる
cv2.destroyAllWindows()