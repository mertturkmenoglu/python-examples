# Example 045: RegEx example

import re

def regExp(pattern, string):
    result = re.match(pattern, string)

    if result:
        print("{} matches {}".format(string, pattern))
    else:
        print("{} does not match {}".format(string, pattern))


regExp('^p....n$', 'python')
regExp('[an]', "anna")
regExp('[an]', "han")
regExp('[an]', "emily")
regExp('[^an]', "anna")
regExp('[^an]', "emily")
regExp('...', "you")
regExp('...', "du")
regExp('...', "andy")
regExp('^yi', "yildiz")
regExp('..a$', "ama")
regExp('..a$', "mama")
regExp('..a$', "da")
regExp('10*1', "11")
regExp('10*1', "101")
regExp('10*1', "1001")
regExp('10+1', "11")
regExp('10+1', "101")
regExp('10+1', "1001")
regExp('ab?a', "aa")
regExp('ab?a', "aba")
regExp('ab?a', "abba")
regExp('ab{3,5}a', "aba")
regExp('ab{3,5}a', "abbba")
regExp('ab{3,5}a', "abbbba")
regExp('ab{3,5}a', "abbbbba")
regExp('ab{3,5}a', "abbbbbba")
regExp('a|b', "a")
regExp('a|b', "b")
regExp('a|b', "ab")
regExp('(a|b)aa', "aaa")
regExp('(a|b)aa', "baa")
regExp('(a|b)aa', "caa")
