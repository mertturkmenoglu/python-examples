# Example 045: RegEx example

import re


def reg_exp(pattern, string):
    result = re.match(pattern, string)

    if result:
        print("{} matches {}".format(string, pattern))
    else:
        print("{} does not match {}".format(string, pattern))


reg_exp('^p....n$', 'python')
reg_exp('[an]', "anna")
reg_exp('[an]', "han")
reg_exp('[an]', "emily")
reg_exp('[^an]', "anna")
reg_exp('[^an]', "emily")
reg_exp('...', "you")
reg_exp('...', "du")
reg_exp('...', "andy")
# noinspection SpellCheckingInspection
reg_exp('^yi', "yildiz")
reg_exp('..a$', "ama")
reg_exp('..a$', "mama")
reg_exp('..a$', "da")
reg_exp('10*1', "11")
reg_exp('10*1', "101")
reg_exp('10*1', "1001")
reg_exp('10+1', "11")
reg_exp('10+1', "101")
reg_exp('10+1', "1001")
reg_exp('ab?a', "aa")
reg_exp('ab?a', "aba")
reg_exp('ab?a', "abba")
reg_exp('ab{3,5}a', "aba")
# noinspection SpellCheckingInspection
reg_exp('ab{3,5}a', "abbba")
# noinspection SpellCheckingInspection
reg_exp('ab{3,5}a', "abbbba")
# noinspection SpellCheckingInspection
reg_exp('ab{3,5}a', "abbbbba")
# noinspection SpellCheckingInspection
reg_exp('ab{3,5}a', "abbbbbba")
reg_exp('a|b', "a")
reg_exp('a|b', "b")
reg_exp('a|b', "ab")
reg_exp('(a|b)aa', "aaa")
reg_exp('(a|b)aa', "baa")
reg_exp('(a|b)aa', "caa")
