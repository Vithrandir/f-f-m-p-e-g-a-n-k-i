import os
import sys
import codecs
# reload(sys)
# sys.setdefaultencoding('gbk')

file = open("01.ass","r")
# convertfile = open("convertass.ass","w")

for line in file.readlines():
	# line2 = line.unicode(line,"gb2312")

	newline = line.decode("utf-16").encode("utf-8")
# 	# print(line)
# 	# convertfile.write(newline)
# 	print(line.encode("gb2312"))

# convertfile.close()
# file.close()
# mytext = "hello"
# with open("01.ass","w") as f:
# 	f.write(codecs.BOM_UTF16_LE)
# 	f.write(mytext.encode("utf-16-le"))
print(sys.maxunicode)
