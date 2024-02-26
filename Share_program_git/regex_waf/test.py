with open("test_string.txt", "r", encoding="utf-8") as f:
    test_string = ""
    for i in f:
        test_string += i

'''
[12, 51, 77]
[31, 40, 49, 64, 73, 96, 105]
'''

#issue 149 ---183(184)
print(test_string[37:57])


