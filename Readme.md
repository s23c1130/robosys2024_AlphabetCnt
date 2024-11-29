<!---
  SPDX-FileCopyrightText: 2024 Toki Makabe <s23c1130sm@s.chibakoudai.jp>
  SPDX-License-Identifier:BSD-3-Clause
--->

[![test](https://github.com/s23c1130/robosys2024_AlphabetCnt/actions/workflows/test.yml/badge.svg)](https://github.com/s23c1130/robosys2024_AlphabetCnt/actions/workflows/test.yml)

# はじめに
このプログラムは、アルファベット+数字の文字数をカウントするプログラムです。

# 動作環境＆開発環境
### 動作環境
- Python3 (3.7～3.10までGithub Actionsにてテスト済み)

### 開発（テスト）環境
- Python 3.10.12
- WSL2 (Ubuntu 22.04 LTS)

# ダウンロード＆インストール方法
```bash
$ git clone https://github.com/s23c1130/robosys2024_AlphabetCnt.git
$ cd robosys2024_AlphabetCnt
```

# 使い方
このプログラムは別ファイルを入力し、結果を出力します。<BR>
ファイルを読み込ませるには ```-i``` オプションを使用します。<BR>
日本語等、英語と数字以外の文字はカウントされません。<BR>

最後に```-e```を使用し、コマンド操作を終了することで、プログラムが動作します。
### 例
```bash
$ ./counter
> -i
> input.txt
> -e
**********(ここより下に結果が出力される)
a,5
b,2
…
```
このプログラムには複数のオプションが存在します。
| オプション | 用途                       | オプションのあとに付ける文字列        | 
| ---------- | -------------------------- | ------------------------------------- | 
| -i         | インプットファイル指定     | インプットするファイル (例:input.txt) | 
| -o         | アウトプットファイル指定   | アウトプットするファイル名            | 
| -s         | ソート　昇順             |                                    | 
| -r         | ソート　降順               |                                       | 
| -a         | 大文字・小文字を区別しない |                                       | 
| -k         | 区切り文字変更             | 使いたい区切り文字                    | 
| -e         | コマンド入力終了           |                                       | 

### 例
```bash
# input.txtを読み込ませて、output.txtに出力 ソートを降順にし、区切り文字を':'に変更
$ ./counter
> -i
> input.txt
> -o
> output.txt
> -r
> -k
> :
> -e
```
### output.txtの結果
```
i:167
e:151
o:125
r:118
t:118
n:113
m:62
f:60
p:58
c:56
u:56
a:47
…
```
# 謝辞
これらは、このプログラムを書く上で、参考にさせていただきましたサイトです。ありがとうございました。
- [組み込み例外 - Python3.13.0ドキュメント](https://docs.python.org/ja/3/library/exceptions.html)
- [5. データ構造 — Python 3.11.10 ドキュメント](https://docs.python.org/ja/3.11/tutorial/datastructures.html)
- [Pythonプログラミング入門 2-2. リスト (list)](https://utokyo-ipp.github.io/2/2-2.html)
- [3. 形式ばらない Python の紹介 3.1.3. リスト型 (list)](https://docs.python.org/ja/3/tutorial/introduction.html#lists)
# ライセンス
 - このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布および使用が許可されます。
 - このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/my_slides robosys_2024](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2024)
 - ©️ 2024 - Toki Makabe
