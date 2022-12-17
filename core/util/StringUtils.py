def splitAtFirstLevelMultipleDelimiters(txt:str, delimiters:list[str])->list[str]:
    """
    Splits a string at the first level of multiple delimiters
    :param txt:
    :param [delimiters]:
    :return [split]:
    """
    
    level = 0
    index = 0
    split = []

    for n,c in enumerate(list(txt)):
        if c in delimiters and level==0:
            split.append(txt[index:n])
            index = n
        elif c=="(": level += 1
        elif c==")": level -= 1
    
    split.append(txt[index+1:])
    
    return split

def containsAny(txt:str,chars:list[str])->bool:
    """
    Checks if a string contains any of the given characters
    :param txt:
    :param chars:
    :return bool:
    """
    for c in chars:
        if c in txt: return True
    return False
