def isPalindrome_num(Num):
    if Num < 0:
        return False
    else:
        cur = 0
        num = Num
        while(num != 0):
            cur =cur*10 + num%10
            num = num // 10
        return cur == Num

def isPalindrome_str(str):
    return str == str[::-1]
# 这里前两个：代表切片的范围，最后一个代表切片的距离，-1就是翻转

def _is_palindromes(string):
        """判断是否回文"""
        i = 0
        length = len(string)
        while i < length / 2:
            if string[i] != string[length - 1 - i]:
                return False
            i += 1
        return True


if __name__ == '__main__':
    print(isPalindrome_num(12321))
