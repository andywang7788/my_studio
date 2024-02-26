import re


def function_regex(raw_string: str, rex_string: str) -> bool:
    raw_string = raw_string
    pattern = re.compile(rex_string, re.M | re.I)
    maj01 = pattern.search(raw_string)
    maj02 = pattern.findall(raw_string)
    # print("------------------------------------------------------")
    if len(maj02) > 0:
        print(True)
        print(maj01.group(0))
        print(maj02)
        print("------------------------------------------------------")
        return True
    else:
        # print(False)
        return False


def Get_prefix(TestString: str) -> str:
    pattern = re.compile(r'^\(((\?i|m|im|mi:)|(\?=)|(\?!)|(\?<=)|(\?<!)|(\?:)).*', re.M | re.I)
    maj01 = pattern.match(TestString)
    if maj01:
        # print(maj01.group(1))
        return "(" + maj01.group(1)
    else:
        return "("


if __name__ == "__main__":
    Test = "(?im:gabcd|1234)"
    Test1 = "(?<=abcd|1234)"
    Test3 = "(?<!abcd|1234)"
    Test4 = "(?!abcd|1234)"
    result = Get_prefix(Test4)
    print(result)
