# SerialBridgePython

## 状態

　開発中 >_<;

## 概要

 本ライブラリは、PCとArduinoマイコンとのシリアル通信を行うためのライブラリです。
 ROSに依存しない処理部分を本リポジトリに記述します。
 マイコンとPC間で数値データのやり取りを可能にします。

## 環境

- Ubuntu 18.04 LTS

- Python 2.7.0
 
## Tutorial
### 導入方法
1. SerialBridgeを利用するパッケージに移動します。    
2. レポジトリをクローンします。(Gitを利用してない場合)
```shell
git clone https://github.com/TNCT-Mechatech/SerialBridgePython
```
2. gitのsubmodule機能を利用してレポジトリをクローンします。(Gitを利用している場合)
```shell
git submodule https://github.com/TNCT-Mechatech/SerialBridgePython
```
  
### メッセージを用意する
ROS同様にメッセージを用意する必要があります。メッセージはYAMLファイルで作成します。  
[vector3.yml](example/vector3.yml) を見てください。これはfloat型のx軸,y軸,z軸を通信できるメッセージになります。'msg_id'はメッセージを識別するためのidです。任意の値を設定してください。  
対応しているデータ型は以下の通りです。  
```
int8_t
uint8_t
int16_t
uint16_t
int
int32_t
uint32_t
float
```  
次に、uint8を送受信する'counter'というメッセージID0のメッセージを用意してみましょう。  
```yaml
counter:
  c: "uint8_t"
msg_id: 0
```
このような構造になります。

### 送受信を行うプログラムを書いてみる
ファイル構造  
```
Project
  |- scripts
  | |- main.py
  | |- counter.yml
  |
  |- SerialBridgePython
    |- scripts
      |- ...
```
[example/ex01_readwrite.py](example/ex01_readwrite.py)  
1. SerialBridgeをimportします。  
sys.path.append()コマンドでSerialBridgeがあるディレクトリに移動します。次にimportを書きます。  
main.py 
```python
sys.path.append('../SerialBridgePython')

import src.message as msg
import src.serial_bridge as pb
```
2. Messageファイルを読み込みます  
先ほど作成したメッセージファイルを読み込みます。まず、messageファイルがあるディレクトリにos.chdir()コマンドで移動します。  
main.py  
```python
sys.path.append('../SerialBridgePython')

import src.message as msg
import src.serial_bridge as pb

# move directory
os.chdir('./scripts')
# load message files
counter0 = msg.Message('./counter.yml')
counter1 = msg.Message('./counter.yml')
```
3. SerialBridgeをセットアップする  
次にSerialBridgeを起動してみましょう。  
main.py  
```python
sys.path.append('../SerialBridgePython')

import src.message as msg
import src.serial_bridge as pb

# move directory
os.chdir('./scripts')
# load message files
counter0 = msg.Message('./counter.yml')
counter1 = msg.Message('./counter.yml')

if __name__=='__main__':
  dev = pb.SerialBridge("TestCounter", 16, "ttyS")
```
この場合、マイコンが待機しているTestCounterというノードを探します。  
USB-Portは、/dev にあるportを指定できます。usb portがtty{数字}の場合は ttyS というふうに書きます。この場合 S に数字が代入されノードを探します。  
ノード間の通信が確立されたら通信を行う準備ができました。  
4. 送受信のプログラムを書く  
変数counter0を送信用、変数counter1を受信用とします。  
受信を行うにはSerialBridgeにフレームを登録する必要があります。  
```python
dev.add_frame(counter1)
```
次に送信のプログラムを書きます。  
まずメッセージにデータを入れてみましょう。  
```python
counter0.set(c= 123)
```  
ここでは、counterメッセージにある変数cに123を代入しています。
送信してみましょう。  
```python
dev.send(0, counter0)
```  
ここでは、メッセージID０にcounter0を送信しています。  
次に受信側のプログラムを書きます。  
```python
if dev.recv() != 1:
  print(counter1.data.c)
```  
recv()は受信するための関数です。成功すればメッセージidが帰されます。失敗した場合は-1を返すため、if構文で受信に成功しているかを確かめる必要があリます。  
データの参照には <メッセージ>.data.<変数> のように取得します。この場合、counter1の変数cを取得しています。  
5. マイコン側のプログラムを書く  
[Arduino版](https://github.com/TNCT-Mechatech/SerialBridgeIno)  
[Mbed版](https://github.com/TNCT-Mechatech/SerialBridgeMbed)  
6. ROSで起動し送受信を行う  
送受信に失敗する場合はdelayの速度を変更してみたりすると成功します。ArduinoのSerialをベースとして作成しているため、バッファーにデータの末端が届かないと成功しません。なので、delayを長くしてみたりして待ってください。
