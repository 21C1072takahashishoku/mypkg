![test](https://github.com/s21c1072/mypkg/actions/workflows/test.yml/badge.svg)
# mypkg
ロボットシステム学のROS2パッケージ  

## 説明
* messageの通信方法 topic通信
* publisher: /talker
* subscriber: /listner
* topic: /countup
* messageの型: int16

## 実行
* /talkerが数字をカウントし、/countupを通じて送信。/listnerがメッセージを受け取り表示する。
一つ目の端末で
```
ros2 run mypkg talker
```
別の端末を立ち上げ、そこで
```
ros2 run mypkg listener
```

## 必要なソフトウェア
* Python
  * テスト済み: 3.7〜3.10   
* ROS2
  * テスト済みバージョン: Humble

## テスト環境
* Ubuntu

## ライセンス
 * このソフトウェアパッケージは、3条項BSDライセンスのもと、再頒布および使用が許可されます。
  * © 2022 Shoku Takahashi
