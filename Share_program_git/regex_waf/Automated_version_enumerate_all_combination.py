import copy

import squre_identify
from my_reg_function import function_regex


def combine(A: list, B: list):
    '''
    example:
    :param A:["a","b","c"]
    :param B:["1","2","3"]
    :return: ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    '''
    List1 = []
    for _, v1 in enumerate(A):
        for _, v2 in enumerate(B):
            List1.append(v1 + v2)
    print(List1)
    return List1


class element(object):
    def __init__(self):
        self.left_index = None
        self.right_index = None
        self.symbol_or = []
        self.layer = None

    def Print(self):
        print("left boundary:", self.left_index, "right boundary:", self.right_index, "layer:", self.layer,
              "symbol_or:", self.symbol_or, len(self.symbol_or))


def differentiate_braceket_and_or(test_string: str) -> list:
    '''
    # braceket : ()
    #squar_brace :[]
    :param test_string: original string
    :return: 1 List_result: bracket location . 2
    '''
    List_result = []
    List_left_bracket, List_left_squar_brace, = [], []
    Left_record_squar_brace, Right_record_squar_brace = [], []
    Left_record_brace, right_record_brace = [], []

    # test_string = standarize_reg(test_string)

    for index, v in enumerate(test_string):
        if len(List_left_squar_brace) > 1:
            raise Exception("List_left_squar_brace > 1 wrong!!!")

        # identify "[" .
        if ((v == "[" and index == 0) or (v == "[" and test_string[index - 1] != "\\")) and len(
                List_left_squar_brace) == 0:
            List_left_squar_brace.append(index)
            Left_record_squar_brace.append(index)

        ##identify "]" ------------------------------------------------------------------
        # condition1 :

        if ((v == "]" and (
                test_string[index - 1] != "\\" or squre_identify.right_special3(index, test_string))) and len(
            List_left_squar_brace) == 1 and not squre_identify.right_special1(index, teststring=test_string)) or (
                squre_identify.right_special2(index, test_string) and len(List_left_squar_brace) == 1):
            Right_record_squar_brace.append(index)
            if len(List_left_squar_brace) > 0:
                List_left_squar_brace.pop()

        # elif v == "]" and test_string[index-1] == "[" and test_string[index-2] == "\\":
        #     if len(List_left_squar_brace) > 0:
        #         List_left_squar_brace.pop()
        #     Right_record_squar_brace.append(index)

        # identify "(" ------------------------------------------------------------------
        if (v == "(" and index == 0) or (v == "(" and test_string[index - 1] != "\\") and len(
                List_left_squar_brace) == 0:
            e = element()
            List_left_bracket.append(e)
            e.left_index = index
            Left_record_brace.append(index)

        # identify ")" ------------------------------------------------------------------
        if (v == ")" and test_string[index - 1] != "\\") and len(List_left_squar_brace) == 0:
            e = List_left_bracket[-1]
            e.right_index = index
            e.layer = len(List_left_bracket)
            List_result.append(List_left_bracket.pop())
            right_record_brace.append(index)

        if (v == "|" and test_string[index - 1] != "\\") and len(List_left_squar_brace) == 0:
            e = List_left_bracket[-1]
            e.symbol_or.append(index)

    # finally check module:
    print("debug log ----------------------------------------------->")
    print("def differentiate_braceket_and_or run over , let us check whether all lists go to Zero?")
    print("Left_record_squar_brace:", Left_record_squar_brace, len(Left_record_squar_brace))
    print("Right_record_squar_brace", Right_record_squar_brace, len(Right_record_squar_brace))
    print("List_left_squar_brace", List_left_squar_brace)
    print("List_left_bracket", List_left_bracket)
    print("Left_record_brace", Left_record_brace, len(Left_record_brace))
    print("right_record_brace", right_record_brace, len(right_record_brace))
    print("#######################################################################")

    if len(Left_record_squar_brace) != len(Right_record_squar_brace):
        raise Exception("left squre bracket != right squre bracket")

    if len(List_left_bracket) != 0:
        print("unbalanced bracket print------------------>")
        List_left_bracket[-1].Print()
        print("unbalanced bracket print------------------>")

    # print(test_string[256:256+10])
    return List_result


def list_all_combination_in_one_layer(test_string: str, left_boundary: int, right_boundary: int,
                                      OR_location_list: list):
    '''
    :param teststring: the string contains | in same layer().
    :param location_list:
    :offset the string is the substring, so the index has offset.
    :return: all combination.

    example:
    left boundary: 38 right boundary: 253 layer: 2 or's index: [124, 194]
    '''

    # check validation.  if OR_location_list length == 0. it only return one string in return:list
    if len(OR_location_list) == 0:
        print(left_boundary, right_boundary, OR_location_list)
        raise Exception("3 tuple has issue")

    # intinialize the data.
    result = []
    offset = left_boundary
    flag = True

    # check (?:)
    if test_string[left_boundary + 1] == "?":
        flag = False

    # OR_location_list= [124, 194]
    for i, v in enumerate(OR_location_list):
        option = ""
        if i == 0:
            option = test_string[(0 + offset):v]
            # print(0,v)
            # print(option)
            # ------------------------------add (A)|(B)|(C)

            result.append(r"{string1})".format(string1=option))

        if i > 0:
            option = test_string[OR_location_list[i - 1] + 1: v]
            # print(OR_location_list[i - 1]+1,v)
            if flag == False:
                result.append(r"(?:{string1})".format(string1=option))
            else:
                result.append(r"({string1})".format(string1=option))
            # print(option)

    option = test_string[OR_location_list[-1] + 1:right_boundary + 1]

    print("OR_location_list", len(OR_location_list))
    if flag == False:
        result.append(r"(?:{string1}".format(string1=option))
    else:
        result.append(r"({string1}".format(string1=option))
    # print(option)
    for _, v in enumerate(result):
        print(v)
    return result


def Return_order_set(test_string: str, layer: int):
    '''
    :param test_string: original string
    :param layer_list: the list containing:
    example:
    left boundary: 16 right boundary: 25 layer: 2 or's index: []
    left boundary: 38 right boundary: 253 layer: 2 or's index: [124, 194]
    [(16, 25), (38, 253)]
    '''
    List_order_layer_specific = []
    layer_list = differentiate_braceket_and_or(test_string)
    for e in layer_list:
        if e.layer == layer:
            List_order_layer_specific.append(e)

    # order
    def take_first(e: element):
        return e.left_index

    List_order_layer_specific.sort(key=take_first, reverse=False)

    #
    for i, v in enumerate(List_order_layer_specific):
        print(i)
        v.Print()

    # return
    return List_order_layer_specific


def Joint_the_wanted_string(teststring: str, layer: int):
    '''

    :param teststring:
    :param layer: specific layer
    :return:
    '''

    # order the List_bundary and make it from left to right.
    List_bundary = Return_order_set(test_string, layer)

    # remove elements without or's index
    '''
    example:
    0: left boundary: 16 right boundary: 25 layer: 2 symbol_or: []
    1: left boundary: 38 right boundary: 253 layer: 2 symbol_or: [124, 194]
    '''

    # remove tuples without "|" for example: 0: left boundary: 16 right boundary: 25 layer: 2 symbol_or: []
    List_bundary_ready = []
    # print("orginal List_bundary", List_bundary)

    for index, v in enumerate(List_bundary):
        if len(v.symbol_or) > 0:
            List_bundary_ready.append(v)

    List_bundary = List_bundary_ready
    # print("List_bundary_ready", List_bundary)

    for index, v in enumerate(List_bundary):
        print("-----------------------------------------")
        v.Print()

    if len(List_bundary) == 0:
        raise Exception("there is no or symbol in this layer")

    List_growing = []
    for index, v in enumerate(List_bundary):
        if index == 0:
            # def list_all_combination_in_one_layer(test_string:str,left_boundary: int, right_boundary: int, OR_location_list: list):
            List_temp = None
            List_temp = copy.copy(
                list_all_combination_in_one_layer(test_string, v.left_index, v.right_index, v.symbol_or))
            # (A|B|C) --- > A,B,C
            print(List_temp)

            List_growing = combine([copy.deepcopy(test_string[0:v.left_index])], List_temp)

        if index > 0:
            List_growing_temp = []
            middle_string = test_string[List_bundary[index - 1].right_index + 1:v.left_index]
            List_temp = None
            List_temp = list_all_combination_in_one_layer(test_string, v.left_index, v.right_index, v.symbol_or)
            # for _, v2 in enumerate(List_temp):
            #     middle_string += v2
            #     List_growing_temp.append(middle_string)
            List_growing_temp = combine([middle_string], List_temp)

            # List_temp2 = []
            List_growing = combine(List_growing, List_growing_temp)

    # add suffix
    tail_string = copy.deepcopy(test_string[List_bundary[-1].right_index + 1:])
    List_growing = combine(List_growing, [tail_string])

    print("Layer:{Layer}: ".format(Layer=layer), List_growing)
    return List_growing


# main
if __name__ == "__main__":
    # layer_number = int(sys.argv[1])
    # flag_do = int(sys.argv[2])
    # layer_number = 1
    # flag_do = 1

    with open("test_string.txt", "r", encoding="utf-8") as f:
        test_string = ""
        for i in f:
            test_string += i
    # print(test_string[90:110])
    # test_string = sys.argv[1]

    # test_string = "(A|(B|D)|C)"
    List_result = differentiate_braceket_and_or(test_string)

    # ------------------------------------------------------------->
    # step1 scout(whether this bracket layer has '|' list)
    layer_number = 1
    or_flag = False
    # layer_list = []
    while True:
        layer_list = []
        for e in List_result:
            if e.layer == layer_number:
                if len(e.symbol_or) > 0:
                    or_flag = True
                    break
                layer_list.append(e.left_index)
        if or_flag == True:
            print("hitting or_flag True")
            break
        elif len(layer_list) == 0:
            print("hitting no braceket!")
            break
        else:
            layer_number += 1

    # def Joint_whole_string(test_string:str,layer:int,all_options_list):
    # Return_order_set(test_string, 1)

    ###step2 do it
    if or_flag == True:
        print("do action: layer:is ", layer_number)
        L1 = Joint_the_wanted_string(test_string, layer_number)
        print("\n\n\nstart here!---------------------------------------->")
        for i, v in enumerate(L1):
            print(v, end="\n\n")

        print("###################################")

        #
        file = "result.txt"
        with open(file, "w", encoding="utf-8") as f:
            for index, v in enumerate(L1):
                v = v + "\n"
                f.write(v)

        # check which one match the regexp

        raw_string = r'''()"*/"7"z '''

        for _, value in enumerate(L1):
            # print(value)
            if function_regex(raw_string, value):
                #print("True----->")
                print(value)
            else:
                pass
                #print(False)
                #print(value)
