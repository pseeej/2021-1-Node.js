# python 기초 코딩
# print 구문의 이해

# 기본 출력. 아래 네 개 다 가능
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Separator 옵션 사용
print('T', 'E', 'S', 'T')   #T E S T
print('T', 'E', 'S', 'T', sep='')   #TEST
print('2021', '02', '01', sep='-')  #2021-02-01
print('niceman', 'google.com', sep='@') #niceman@google.com

# end 옵션 사용
print('Welcome to', end=' ')
print('the black parade', end=' ')   #Welcome to the black parade
print('piano notes') #~~ piano notes

print()

# format 사용 [], {}, ()
print('{} and {}'.format('You', 'Me'))  #You and me. format에 넣고자 하는 거 써둠
print('{0} and {1} and {0}'.format('You', 'Me'))    #You and me and you. 0번에 you, 1번에 me라고 생각하고 대입됨
print("{a} are {b}".format(a='You', b='Me')) #You are me

print()

# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" %('Sejin', 2)) #Sejin's favorite number is 2

print("Test1 : %5d, Price : %4.2f" %(776, 6534.123))    #%5d는 총 5자리로 표현하라~ %4.2f는 앞자리는 네자리로, 소수점 이하 자리는 두 개까지만
print("Test1 : {0: 5d}, Price : {1:4.2f}".format(776, 6534.123)) #위랑 동일
print("Test1 : {a: 5d}, Price : {b:4.2f}".format(a=776, b=6534.123))    #이것도 위랑 동일

print()

# escape문
print("'you'")  #'you'
print('\'you\'') #위랑 동일
print('"you"')  #"you"
print("""'you'""")  #'you'
print('\\you\\')    #\you\
print('\ntest') #\n은 줄바꿈
print('\t\ttest')   #\t는 tab
