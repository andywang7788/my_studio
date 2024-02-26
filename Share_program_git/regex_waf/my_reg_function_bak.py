import re


def function_regex(raw_string: str, rex_string: str) -> bool:
    raw_string = raw_string
    pattern = re.compile(rex_string, re.M | re.I)
    maj01 = pattern.search(raw_string)
    maj02 = pattern.findall(raw_string)
    #print("------------------------------------------------------")
    if len(maj02) > 0 :
        print(True)
        print(maj01.group(0))
        print(maj02)
        print("------------------------------------------------------")
        return True
    else:
        #print(False)
        return False


# if __name__ == "__main__":
#     test_string = r'''( )$ ""/e"v'al'''
#     pattern = re.compile(r'''(?:\(\s*\))\s*(?:\$)*\s*(?:\")*(?:[\?\*\[\]\(\)\-\|+\w'\"\.\/\\\\]+\/)?[\\\\'\"]*(?:e[\\\\'\"]*(?:v[\\\\'\"]*a[\\\\'\"]*l))\b''', re.M | re.I)
#     maj02 = pattern.match(test_string)
#     if maj02:
#         print(True)
#     else:
#         print(False)



