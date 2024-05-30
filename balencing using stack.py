def isbalenced(word):
    stack=[]
    for element in word:
        if element =='(':
            stack.append(element)
        else:
            if len(stack)==0:
                return False
            else:
                stack.pop()
    if len(stack)==0:
        return True
    return False
word="()()()"
result=isbalenced(word)
print(result)
