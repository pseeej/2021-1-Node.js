# section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

from pkg.fibonacci import Fibonacci # class method 형태로 받을 수 있음

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title)  #instance로 초기화 해줘야지 method 호출 가능하므로 Fibonacci()로 함

print()

# 사용 2
from pkg.fibonacci import *  # 전부 ㄷㅏ 가져오는 방법. 권장하진 않음. 

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)

print()

# 사용 3
from pkg.fibonacci import Fibonacci as fb   # 이건 권장하는 방법. 매번 길게 작성 안 해도 됨

fb.fib(1000)

print("ex3 : ", fb.fib2(1600))
print("ex3 : ", fb().title)

print()

# 사용 4 (함수)
import pkg.calculations as c    # pkg.calculations에서는 다 함수 형태로 입력이 되어 있음

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

print()

# 사용 5 (함수)
from pkg.calculations import div as d   # 필요한 함수만 가져옴
print("ex5 : ", int(d(100, 10)))

print()

# 사용 6
import pkg.prints as p
import builtins # 파이썬에서 기본적으로 제공하는 directory. import 굳이 안 해도 됨
p.prt1()
p.prt2()
print(dir(builtins))    # 기본으로 들어있는 함수들.