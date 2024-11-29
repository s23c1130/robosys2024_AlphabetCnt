#!/usr/bin/python3

# SPDX-FileCopyrightText: 2024 Toki Makabe <s23c1130sm@s.chibakoudai.jp>
# SPDX-License-Identifier:BSD-3-Clause

import sys
import re

BEFORE_SORT = 1
BEFORE_DESC = 2
BEFORE_INPUT = 3
BEFORE_OUTPUT = 4
BEFORE_NOAPPER_LOWER = 5
BEFORE_KUGIRI = 6

sort_comm = 0 #ソートをする
desc_comm = 0 #ソートする＆降順で並べる
input_file = "" #インプットするテキストデータのパス
output_file = "" #アウトプットする場合のパス
NoApperLower_comm = 0 #大文字・小文字を区別しない
kugiri_comm = "," #区切り文字の変更
before_tmp = 0

moji_count = [[0 for _ in range(2)] for _ in range(200)]


for line in sys.stdin:
    # オプションだったら(先頭にハイフンがつく)
    if line[0] == '-':
        if line[1] == 'i':
            before_tmp = BEFORE_INPUT
            continue
        elif line[1] == 'o':
            before_tmp = BEFORE_OUTPUT
            continue
        elif line[1] == 's':
            sort_comm = 1
            continue
        elif line[1] == 'r':
            desc_comm = 1
            continue
        elif line[1] == 'a':
            NoApperLower_comm = 1
            continue
        elif line[1] == 'k':
            before_tmp = BEFORE_KUGIRI
            continue
        elif line[1] == 'e':
            break
        elif line[1] == 'h':
            print("文字をカウントして出力します\n-i:インプットファイル指定 \n-o:アウトプット指定(オプション)")
            print("-s:ソート(オプション・昇順) \n-r:ソート(オプション・降順)\n-a:大文字・小文字を区別しない(オプション) \n-k:区切り文字変更（オプション)\n-e コマンド入力終了")
            print("例： $char_count (enter) -i (enter) input.txt (enter) -r (enter) -k (enter) : (enter) -e (enter)")
            sys.exit(0)
        else:
            print("不明なコマンド -h(help)を参照\n")
            sys.exit(1)

    if before_tmp == BEFORE_INPUT:
        input_file = line
        continue
    elif before_tmp == BEFORE_OUTPUT:
        output_file = line
        continue
    elif before_tmp == BEFORE_KUGIRI:
        kugiri_comm = line
        kugiri_comm = kugiri_comm.replace("\n","")
        continue
        

if input_file == "":
    print("入力ファイルが指定されていません。終了します。（-iオプションでファイルを入力してください)")
    exit(2)

#改行文字を取り除く
input_file = input_file.replace("\n","")
f_open = open(input_file, "r",-1 ,"utf-8")
data = f_open.read()
if f_open == OSError:
    print("エラーが発生しました。ファイルを開けませんでした。")
    exit(3)

#英語と数字のみにする
data = re.sub(r'[^a-zA-Z0-9]',"",data)

#大文字＆小文字を区別しないので、すべて大文字にする
if NoApperLower_comm == 1:
    data = data.upper()

#小文字の処理
for i in range(ord('a'), ord('z')):
    moji_count[i][0] = data.count(chr(i))
    moji_count[i][1] = chr(i)

#大文字の処理
for i in range(ord('A'), ord('Z')):
    moji_count[i][0] = data.count(chr(i))
    moji_count[i][1] = chr(i)

#数字の処理
for i in range(ord('0'), ord('9')):
    moji_count[i][0] = data.count(chr(i))
    moji_count[i][1] = chr(i)

if desc_comm == 1:
    sort_moji = sorted(moji_count, key = lambda x:-x[0])
elif sort_comm == 1:
    sort_moji = sorted(moji_count, key = lambda x:x[0])
else:
    sort_moji = moji_count

#別ファイルに出力する場合は
if output_file != "":
    #改行文字を取り除く
    output_file = output_file.replace("\n","")
    f_save = open(output_file, "w",-1,"utf-8")
    if f_open == OSError:
        print("エラーが発生しました。ファイルを開けませんでした。")
        exit(3)

    for i in range(0,200):
        if sort_moji[i][0] != 0:
            f_save.write(sort_moji[i][1])
            f_save.write(kugiri_comm)
            f_save.write(str(sort_moji[i][0]))
            f_save.write("\n")
else:
    for i in range(0,200):
        if sort_moji[i][0] != 0:
            print(sort_moji[i][1],end='')
            print(kugiri_comm,end='')
            print(sort_moji[i][0])


        
