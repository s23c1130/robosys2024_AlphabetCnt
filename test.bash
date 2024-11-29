#!/bin/bash -xv

# SPDX-FileCopyrightText: 2024 Toki Makabe <s23c1130sm@s.chibakoudai.jp>
# SPDX-License-Identifier:BSD-3-Clause

ng () {
	echo ${1}行目が違う
}

res=0

echo "TEST_test_aaabbcccczzzz123432" > /tmp/test_data.txt

### 通常のテスト(正常に終わるか) ###
echo -e "-i\n/tmp/test_data.txt\n-k\n:\n-e" | ./counter > /tmp/test_output.txt
grep b:2 /tmp/test_output.txt
res=$?

[ "$res" == 0 ] || ng "$LINENO"

exit $res