# 모법답안

from random import *
coupon = range(1,21) # 1부터 20까지 숫자를 생성
print(type(coupon))
coupon = list(coupon)
print(type(coupon))

print(coupon)
shuffle(coupon)
print(coupon)

selection = sample(coupon, 4) # 4명 중에서 1명은 치킨, 3명은 커피

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(selection[0]))
print("커피 당첨자 : {0}".format(selection[1:]))
print(" -- 축하합니다 --")

