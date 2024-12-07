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
cat /tmp/test_data.txt | ./counter > /tmp/test_output.txt
grep b,2 /tmp/test_output.txt
out=$?

[ "$out" = 0 ] || ng "$LINENO"

### ヘルプ表示テスト ###
echo | ./counter -h > /tmp/test_help.txt
grep 文字をカウントして出力します /tmp/test_help.txt
out=$?

[ "$out" = 0 ] || ng "$LINENO"

### 区切り変更テスト（区切り文字を変更してみる)
cat /tmp/test_data.txt | ./counter -k :> /tmp/test_output.txt
grep b:2 /tmp/test_output.txt
out=$?

[ "$out" = 0 ] || ng "$LINENO"

### 大文字・小文字を区別しないテスト
cat /tmp/test_data.txt | ./counter -a > /tmp/test_output.txt
grep T,4 /tmp/test_output.txt
out=$?

[ "$out" = 0 ] || ng "$LINENO"

### 存在しない引数を選択した場合
cat /tmp/test_data.txt | ./counter -d 2> /tmp/test_output.log
grep "不明なコマンド -h(help)を参照" /tmp/test_output.log
out=$?

[ "$out" = 0 ] || ng "$LINENO"

[ "$res" = 0 ] && echo TEST_OK

exit $res