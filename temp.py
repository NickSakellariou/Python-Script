import operator



def removeDuplicates(x):
  return list(dict.fromkeys(x))



def reverseList(x):
    print(sorted(x,reverse=True))



def RemoveDuplicates(x):
    result = {}
    for key,value in x.items():
        if value not in result.values():
            result[key] = value
    return result



def reverseDict(x):
    sorted_a_dict = sorted(x.items(), key=operator.itemgetter(1),reverse=True)
    print(sorted_a_dict)


a_list =[10,12,14,14,16,28,28,30]

a_list = removeDuplicates(a_list)
print(a_list)

reverseList(a_list)

a_dict={"a":10,"b":12,"c":14,"d":14,"e":16,"f":28,"g":28,"h":30}

a_dict = RemoveDuplicates(a_dict)
print(a_dict)

reverseDict(a_dict)