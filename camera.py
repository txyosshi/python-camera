import cv2

#VideoCaptureクラス
#
#メソッド
#
#read() 1コマ分の画像データ読み込み
#release() デバイスリリース（動画ファイルの場合ファイルクローズも行う）


#インスタンス化
#引数はWindowsのカメラデバイス番号
#1台接続の場合0を指定

cap = cv2.VideoCapture(1)


#whileがあるので、cap.read()がtrue（画像データが読み取れている）間はframeにデータを格納
#aaaはtrue/falseを格納する変数（通常はretと書くみたい）

while(True):
	aaa, frame = cap.read()
	#cv2.imshow()はOpenCVで用意されているコマンド
	#cv2.imshow('フレーム名',画像を格納している変数（=frame）
	cv2.imshow('frame',frame)
	
	#フレーム名を変えると別のウィンドウで出てくる
	cv2.imshow('frame2',frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#whileを抜けたらリリース
capture.release()
#フレームを閉じる
cv2.destroyAllWindows()