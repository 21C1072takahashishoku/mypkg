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
* /talker が数字をカウントし /countup を通じて送信、/listner がメッセージを受け取り表示
```
ros2 run mypkg talker
```
もう一つ端末を立ち上げてそこで
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
