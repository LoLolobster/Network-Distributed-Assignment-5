import matplotlib.pyplot as plt

#add two binary numbers (in string form)
def add_binary(str1, str2):
    a = int(str1, 2)
    b = int(str2, 2)
    res = bin(a+b)[2:]
    if len(res) < 16:
        res = '0'*(16-len(res)) + res
    return res

#get the checksum of the words
def check_sum(words):
    _sum = '0'
    checksum = ''
    for word in words:
        _sum = add_binary(_sum, word)
    if len(_sum) > 16:
        wrap_around = _sum[:-16]
        _sum = add_binary(_sum[-16:], wrap_around)
    for i in range(0, 16):
        checksum += str(abs(1-int(_sum[i])))
    return _sum,checksum


words = ['0110011001100000', '0101010101010101','1000111100001100']
_sum, checksum = check_sum(words)

res = []
for i in range(0,16):
    res.append(int(_sum[i]) + int(checksum[i]))
plt.plot([0,16],[1,1], 'g', label = "y = 1")
plt.scatter(range(0,16), res, label = "validation by bit")
plt.axis([0,15,0,2])
plt.title("checksum validation")
plt.xlabel("bit position")
plt.legend()
plt.show()
print(res)
