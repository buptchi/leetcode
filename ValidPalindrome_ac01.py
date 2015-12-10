__author__ = 'chi'



# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
"""
    s_alnumber = ""
    for ss in s:
        if ss.isalnum():
            s_alnumber += ss.lower()
"""


def isPalindrome(s):
    j = len(s) - 1
    if j == -1:
        return True
    i = 0

    alnumflagi = True
    alnumflagj = True

    while not i == j:
        alnumflagi = True
        alnumflagj = True
        while not s[i].isalnum():
            if i < j:
                i += 1
            else:
                alnumflagi = False
                break
        while not s[j].isalnum():
            if i < j:
                j -= 1
            else:
                alnumflagi = False
                break

        if i <= j and alnumflagi and alnumflagj:
            print(s[i], s[j], i, j)
            if not s[i].lower() == s[j].lower():
                return False
            else:
                if i == j or (j - i) == 1:
                    return True
                else:
                    i += 1
                    j -= 1
        else:
            return True
    return True
#str1="A man, a plan, a canal: Panama"
str1="  .,,ffddff,.  "
print isPalindrome(str1)