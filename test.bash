#!/bin/bash -xv

# SPDX-FileCopyrightText: 2024 Toki Makabe <s23c1130sm@s.chibakoudai.jp>
# SPDX-License-Identifier:BSD-3-Clause

ng () {
	echo ${1}行目が違う
	res=1
}

res=0

echo "TEST_test_aaabbcccczzzz123432" > /tmp/test_data.txt

### 通常のテスト(正常に終わるか) ###
echo -e "-i\n/tmp/test_data.txt\n-k\n:\n-e" | ./counter > /tmp/test_output.txt
grep b:2 /tmp/test_output.txt
out=$?

[ "$out" == 0 ] || ng "$LINENO"

### ヘルプ表示テスト ###
echo -e "-h" | ./counter > /tmp/test_help.txt
grep 文字をカウントして出力します /tmp/test_help.txt
out=$?

[ "$out" == 0 ] || ng "$LINENO"

### 入力エラーテスト（存在しない適当なファイルを入力する) ###

echo -e "-i\n/tmp/nweokgjeiogneiopfj.txt\n-k\n:\n-e" | ./counter > /tmp/test_output.txt
out=$?

[ "$out" == 0 ] && ng "$LINENO"

### 区切り変更テスト（区切り文字を変更してみる)
echo -e "-i\n/tmp/test_data.txt\n-k\n,\n-e" | ./counter > /tmp/test_output.txt
grep b,2 /tmp/test_output.txt
out=$?

[ "$out" == 0 ] || ng "$LINENO"

exit $res