while True:
    year = int(input('type year : '))
    leafyear = None
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leafyear = True
            else:
                leafyear = False
        else:
            leafyear = True
    else:
        leafyear = False
    if leafyear == True:
        print(year,'년은 윤년입니다.')
    else:
        print(year,'년은 평년입니다.')