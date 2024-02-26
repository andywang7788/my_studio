# test_string = r'''(?i:(?:(?:(?:(?:trunc|cre|upd)at|renam)e|(?:inser|selec)t|de(?:lete|sc)|alter|load)\s*?\(\s*?space\s*?\(|,.*?[)\da-f\"'`][\"'`](?:[\"'`].*?[\"'`]|[^\"'`]+|\Z)|\Wselect.+\W*?from))'''
import copy
import sys

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
    return List1


class element(object):
    def __init__(self):
        self.left_index = None
        self.right_index = None
        self.symbol_or = []
        self.layer = None

    def Print(self):
        print("left boundary:", self.left_index, "right boundary:", self.right_index, "layer:", self.layer,
              "symbol_or:", self.symbol_or)


def differentiate_braceket_and_or(test_string: str):
    '''

    :param test_string: original string
    :return: 1 List_result: bracket location . 2
    '''
    List_result = []
    List_left_bracket, List_left_squar_brace = [], []

    for index, v in enumerate(test_string):
        if v == "[":
            List_left_squar_brace.append(index)
        if v == "]":
            List_left_squar_brace.pop()

        if (v == "(" and index == 0) or (v == "(" and test_string[index - 1] != "\\") and len(
                List_left_squar_brace) == 0:
            e = element()
            List_left_bracket.append(e)
            e.left_index = index

        if (v == ")" and test_string[index - 1] != "\\") and len(List_left_squar_brace) == 0:
            e = List_left_bracket[-1]
            e.right_index = index
            e.layer = len(List_left_bracket)
            List_result.append(List_left_bracket.pop())

        if v == "|":
            e = List_left_bracket[-1]
            e.symbol_or.append(index)
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



    result = []
    offset = left_boundary

    # OR_location_list= [124, 194]
    for i, v in enumerate(OR_location_list):
        option = ""
        if i == 0:
            option = test_string[(0 + offset):v]
            # print(0,v)
            # print(option)

            result.append(r"{string1})".format(string1=option))
        if i > 0:
            option = test_string[OR_location_list[i - 1] + 1: v]
            # print(OR_location_list[i - 1]+1,v)
            result.append(r"{string1}".format(string1=option))
            # print(option)

    option = test_string[OR_location_list[-1] + 1:right_boundary + 1]
    result.append(r"({string1}".format(string1=option))
    # print(option)
    for _,v in enumerate(result):
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
    List_bundary = Return_order_set(test_string, layer)


    # remove elements without or's index
    '''
    example:
    0: left boundary: 16 right boundary: 25 layer: 2 symbol_or: []
    1: left boundary: 38 right boundary: 253 layer: 2 symbol_or: [124, 194]
    '''
    for index, v in enumerate(List_bundary):
        if len(v.symbol_or) == 0:
            List_bundary.pop(index)
    if len(List_bundary) == 0:
        raise Exception("there is no or symbol in this layer")


    List_growing = []
    for index, v in enumerate(List_bundary):
        if index == 0:
            # def list_all_combination_in_one_layer(test_string:str,left_boundary: int, right_boundary: int, OR_location_list: list):
            List_temp = None
            List_temp = copy.copy(list_all_combination_in_one_layer(test_string, v.left_index, v.right_index, v.symbol_or))
            # (A|B|C) --- > A,B,C
            print(List_temp)


            List_growing = combine([copy.deepcopy(test_string[0:v.left_index])],List_temp)

        if index > 0:
            List_growing_temp = []
            middle_string = test_string[List_bundary[index-1].right_index+1:v.left_index]
            List_temp = None
            List_temp = list_all_combination_in_one_layer(test_string, v.left_index, v.right_index, v.symbol_or)
            # for _, v2 in enumerate(List_temp):
            #     middle_string += v2
            #     List_growing_temp.append(middle_string)
            List_growing_temp = combine([middle_string],List_temp)

            #List_temp2 = []
            List_growing = combine(List_growing,List_growing_temp)

    #add suffix
    tail_string = copy.deepcopy(test_string[List_bundary[-1].right_index+1:])
    List_growing = combine(List_growing,[tail_string])

    print("Layer:{Layer}: ".format(Layer=layer),List_growing)
    return List_growing


#main
if __name__ == "__main__":


    # test_string = r'''(?i:(?:(?:(?:(?:trunc|cre|upd)at|renam)e|(?:inser|selec)t|de(?:lete|sc)|alter|load)\s*?\(\s*?space\s*?\(|,.*?[)\da-f\"'`][\"'`](?:[\"'`].*?[\"'`]|[^\"'`]+|\Z)|\Wselect.+\W*?from))'''

    #test_string = r'''(?i:[\s'\"`()]*?([\d\w]++)[\s'\"`()]*?(?:<(?:=(?:[\s'\"`()]*?(?!\1)[\d\w]+|>[\s'\"`()]*?(?:\1))|>?[\s'\"`()]*?(?!\1)[\d\w]+)|(?:not\s+(?:regexp|like)|is\s+not|>=?|!=|\^)[\s'\"`()]*?(?!\1)[\d\w]+|(?:(?:sounds\s+)?like|r(?:egexp|like)|=)[\s'\"`()]*?(?:\1)))'''
    with open("test_string.txt","r",encoding="utf-8") as f:
        test_string = ""
        for i in f:
            test_string += i


    #test_string = sys.argv[1]
    layer_number = int(sys.argv[1])
    flag_do = int(sys.argv[2])

    # test_string = "(A|(B|D)|C)"
    List_result = differentiate_braceket_and_or(test_string)


#------------------------------------------------------------->
    #step1 scout(whether this bracket layer has '|' list)
    layer_list = []
    for e in List_result:
        if e.layer == layer_number  :
            e.Print()

    # def Joint_whole_string(test_string:str,layer:int,all_options_list):
    #Return_order_set(test_string, 1)

    ###step2 do it
    if flag_do != None and flag_do == 1 :
        L1 = Joint_the_wanted_string(test_string, layer_number)
        print("---------------------------------------->")
        for i,v in enumerate(L1):
            print(v)



        print("###################################")
    #list_all_combination_in_one_layer(test_string,38,253,[124, 194])
