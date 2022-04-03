from datetime import datetime

if __name__ == "__main__":
    d = datetime.today().strftime("%Y%m%d")
    intd = int(d)

    with open(r"C:\Users\doock\Documents\jihwan\cd_key\cdkey.txt", mode="r") as file:
        lines = file.read()
        print(lines)

    cdkey = lines
    keyCheck = False

    if cdkey == '19as-asw2-wq2d-d2da':
        keyCheck= True
    elif intd >= 20200716 and intd < 20200720:
        if cdkey != '19as-asw2-wq2d-d2da':
            keyCheck = False
    elif intd >= 20200720 and intd < 20200820:
        if cdkey != '2323-asw2-wq2d-d2da':
            keyCheck = False
    elif intd >= 20200820 and intd < 20200920:
        if cdkey != '4242-asw2-2132-2222':
            keyCheck = False
    elif intd >= 20200920 and intd < 20201020:
        if cdkey != '5646-asw2-wq2d-3333':
            keyCheck = False
    elif intd >= 20201020 and intd < 20201120:
        if cdkey != '6655-asw2-wq2d-4444':
            keyCheck = False

    if keyCheck == False:
        exit()

    print('올바른 CD Key 입니다. 프로그램을 시작합니다.')
    c = input()