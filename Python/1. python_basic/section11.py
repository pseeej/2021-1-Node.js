# section11
# 파이썬 외부 파일 처리
# 파이썬 excel, csv 파일 읽기 및 쓰기

# csv : mime - text / csv

import csv

# 예제 1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)  # 구분자가 , 
    #next(reader)    # 그 다음 줄로 넘어감. 한 줄은 아예 안 나오는겨. 보통 처음에 한 번 써서 header skip

    # 확인
    print(reader)
    print(type(reader)) # csv.reader
    print(dir(reader))  # 이거 확인해봤는데 오~ iter가 있구나~

    print()

    for c in reader:
        print(c)    # 한 line을 list로 가져옴

print()

# 예제 2
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f, delimiter ='|')  # delimiter 안 써주면 default가 ,임. 주어진 기호?로 list를 나누겠다~는 뜻

    for c in reader:
        print(c)    

print()

# 예제 3 (dict 변환)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)  # key : value 형태로 가져옴.

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('--------')


# 예제 4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    for v in w: # 하나하나 검수해서 쓸 땐 writerow 쓰는 게 좋고
        wt.writerow(v)  # 한 열에 하나씩 쓰겠다~ 123 \n 456 뭐 이런 식으로


print()

# 예제 5
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w) # 위에 거랑 똑같은데 한 번에 작성함. 조건 상관 없이 그냥 한 번에 쓰려면 이렇게 writerows하는 게 좋음


# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용 (openpyxl, xlrd)
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

# sheetname = '시트명' 또는 숫자, header=숫자, skiprow=숫자
xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인
print(xlsx.head())
print()

# 데이터 확인
print(xlsx.tail())

# 데이터 확인
print(xlsx.shape) # (행, 열)

# 엑셀 or csv 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)    # xlsx 작성하기
xlsx.to_csv('./resource/result.csv', index=False)   # csv 작성하기