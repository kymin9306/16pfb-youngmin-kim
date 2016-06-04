# -*- coding:utf-8 -*-

print "i eat %d apples" %3

# 숫자열에 대입하는 특수 문자는 %d 이다.

print "i eat %s apples" % 'seven'

# 문자열에 대입하는 특수문자는 %s 이다. (문자를 대입 할 떄에는 뒤에 괄호를 붙힌다.)

number = 5
print "i eat %d apples" % number
# 위의 number 처럼 따로 지정된 변수가 있을경우 뒤에 괄호는생략한다.

mine = 10
day = "ten"
print " i ate %d apples. so i was sick for %s days " % (mine , day)
# 문자열이든 숫자열이든 괄호안에서는 순서대로 적어준다

print "i want to eat %s BBQ " % 2

print "i eat %s BBQ" % 3

print "Error is %d%%" % 98
# 확률을 나타내는 %기호를 작성할떄는 %d, %s 기호뒤에 %를 두개를 써 준다.

print "%10s" % "hi"
#  %()s 괄호 안에 숫자를 기입한 숫자만큼 실행시 문자열 10개를 기준으로 오른쪽에서 정렬을 한다.


print "%-10s jane." % "tom"
# -숫자는 숫자만큼의 문자열에서 왼쪽으로 정렬시킨다.

print "%0.5f"  % 3.1415927989
# %f는 소숫점 자리 표시 기호로서 0.(숫자)를 기입하면 숫자만큼의 소숫점 자리를 표기한다.

print "%15.10f" % 3.11415926535
# 소숫점 자리 표기와 간격표시의 혼합.


