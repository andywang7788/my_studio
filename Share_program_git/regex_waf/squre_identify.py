# condition0  []]
def right_special1(index: int, teststring: str) -> bool:
    '''
    #condition0  []]
    :param index:
    :param teststring:
    :return: bool
    '''
    if teststring[index] == "]" and teststring[index - 1] == "[" and teststring[index - 2] == "[" and teststring[
        index - 3] != "\\":
        print("trigger macth []] ---- right_special1", index)
        print(teststring[index - 3:index + 1])
        return True
    else:
        return False


# condition1 [[]
def right_special2(index: int, teststring: str, ) -> bool:
    '''
    #condition1 [[]
    :param index:
    :param teststring:
    :return:
    '''
    if teststring[index] == "]" and teststring[index - 1] == "[" and teststring[index - 2] == "[" and teststring[
        index - 3] != "\\":
        print("trigger macth [[]----right_special2", index)

        return True
    else:
        return False


def right_special3(index: int, teststring: str) -> bool:
    '''
    \\\\]
    :param index:
    :param teststring:
    :return:
    '''
    hit = 0
    while True:
        index -= 1
        if teststring[index] == "\\":
            hit += 1
        else:
            break
    if hit > 0 and hit % 2 == 0:
        print("match right_special3")
        return True
    else:
        print(" not match right_special3")
        return False


def left_special1(index: int, teststring: str) -> bool:
    '''
    [[]
    :param index:
    :param teststring:
    :return:
    '''
    if teststring[index] == "[" and teststring[index - 1] == "[" and teststring[index - 2] != "\\":
        print("trigger macth [[")
        return False
    else:
        return True
