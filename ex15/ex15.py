# http://learnpythonthehardway.org/book/ex15.html
from sys import argv

script, filename = argv

txt = open(filename)

print "here's your file %r:" % filename
print txt.read()
raw_input(sample.txt)