<!---
  SPDX-FileCopyrightText: 2024 Toki Makabe <s23c1130sm@s.chibakoudai.jp>
  SPDX-License-Identifier:BSD-3-Clause
--->

[![test](https://github.com/s23c1130/robosys2024_AlphabetCnt/actions/workflows/test.yml/badge.svg)](https://github.com/s23c1130/robosys2024_AlphabetCnt/actions/workflows/test.yml)

# はじめに
アルファベット+数字の文字数をカウントするプログラムです。

# 動作環境＆開発環境
### 動作環境
- Python3

### テスト環境
- Python 3.10.12
- WSL2 (Ubuntu 22.04 LTS)
- Github Actions
    - ubuntu-latest
    - Python Version 3.7~3.10

# 導入方法
```bash
$ git clone https://github.com/s23c1130/robosys2024_AlphabetCnt.git
$ cd robosys2024_AlphabetCnt
$ chmod +x counter
```

# 使い方
標準入力から、データを入力し、文字のカウントをしたあとに、結果を出力します。

### 例
```bash
$ cat input.txt | ./counter
**********(ここより下に結果が出力される)
a,5
b,1
…
```
このプログラムには複数のオプションが存在します。
| オプション | 用途                       | オプションのあとに付ける文字列        | 
| ---------- | -------------------------- | ------------------------------------- | 
| -o         | アウトプットファイル指定(別ファイルに出力)   | アウトプットするファイル名            | 
| -s         | ソート　昇順             |                                    | 
| -r         | ソート　降順               |                                       | 
| -a         | 大文字・小文字を区別しない |                                       | 
| -k         | 区切り文字変更             | 使いたい区切り文字                    | 

### 例
```bash
# input.txtを読み込ませて、output.txtに出力 ソートを降順にし、区切り文字を':'に変更
$ cat input.txt | ./counter -r -k : -o output.txt
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
これらは、このプログラムを書く上で、参考にさせていただきましたサイトです。ここにて感謝申し上げます。
- [組み込み例外 - Python3.13.0ドキュメント](https://docs.python.org/ja/3/library/exceptions.html)
- [5. データ構造 — Python 3.11.10 ドキュメント](https://docs.python.org/ja/3.11/tutorial/datastructures.html)
- [Pythonプログラミング入門 2-2. リスト (list)](https://utokyo-ipp.github.io/2/2-2.html)
- [3. 形式ばらない Python の紹介 3.1.3. リスト型 (list)](https://docs.python.org/ja/3/tutorial/introduction.html#lists)
# ライセンス
 - このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布および使用が許可されます。
 - このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [第3回: Linux環境でのPythonプログラミングII](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson3.html)
      - 13ページ目 ファイルからの入力 (counter)
    - [第5回: 著作権とライセンス](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson5.html)
      - 10ページ目 作業: コードに著作権表示 (すべてのコードファイル)
    - [第6回: ソフトウェアのテスト](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson6.html)
      - 19ページ目 コマンドに対するリグレッションテストの記述 (test.bash)
      - 20ページ目 コマンドに対するリグレッションテストの記述(続き)
    - [第7回: GitHubでのテスト](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson7.html)
      - 8ページ目 テストの手続きの記述 (test.yml)
 - ©️ 2024 - Toki Makabe
