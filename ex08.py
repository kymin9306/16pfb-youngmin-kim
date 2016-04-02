Formatter = "%r %r %r %r"


print Formatter % (1,2,3,4)
print Formatter % ("one","two","three","four")
print Formatter % (True,False,False,True)
print Formatter % (Formatter, Formatter, Formatter, Formatter)
print Formatter % (
    "i had this thing.",
    "that you could type up right.",
    "but it didn't sing.",
    "so i said good night"
)