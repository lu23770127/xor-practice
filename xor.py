
print("請輸入編號（如:8a020a11）:")
data=input()
code1=data[0:4]
code2=data[4:]

result=hex(int(code1, 16) ^ int(code2, 16))
convert1=result[2:4]
convert2=result[4:]
print("hex 2 for : %(c1)s %(c2)s" % {"c1":convert1, "c2":convert2})
result2=hex(int(convert1, 16) ^ int(convert2, 16))

print("result2 :",result2[2:])
