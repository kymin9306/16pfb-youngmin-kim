# -*- coding:utf-8 -*-

# 문자열과 인덱싱

a = "test is very hard. so, we need jump to python"
print a[3]

#파이썬은 숫자를 0부터 센다(맨앞)

b = "work hard play hard"
print b[1]
print b[13]

# [-숫자] 숫자 앞에 마이너스를 붙이는 경우는 뒤에서부터 숫자를 1234..라는 식으로 센다 (0) 없음.
# [-0] 은 [0]과 같은 결과값을 보여준다
print b[-4]

c = b[0] + b[1] + b[2] + b[3]
print c

print b[:]

print b

G = "2015110009gloomy"
ID = G [0:10]
Weather = G[10:]

print ID
print Weather

s = "pithon"
print s[1]

print  s[:1] + "y" +s[2:]