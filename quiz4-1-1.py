def palindrome(text):
    if str.strip(text[::-1].lower()) == str.strip(text).lower():
        return True
    else:
        return False
while True:
    a = input('회문판별할 문자열 입력 :')
    print(palindrome(a))