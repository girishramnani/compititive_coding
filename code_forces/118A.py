word = input()
word = filter(lambda x: not x in "aeiouy" ,list(word.lower()))
print("."+".".join(word))

