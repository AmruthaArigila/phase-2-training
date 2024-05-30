# stack implementation #
'''def push(stack,ele):
    stack.append(ele)
    print(ele,"inserted into stack successfully")

def pop(stack):
    if len(stack)==0:
        print("stack is empty")
        return
    print(stack[-1],"deleted successfully")
    stack.pop()
stack=[]
push(stack,10)
push(stack,20)
push(stack,30)
push(stack,40)
push(stack,50)

pop(stack)
pop(stack)
pop(stack)
pop(stack)
pop(stack)
pop(stack)'''

# balanced brackets #
'''def isbalenced(word):
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
print(result)'''

# valid paranthesis#
class Solution(object):
    def isValid(self,s):
        stack=[]
        openBrackets=["(","{","["]
        for ele in s:
            if ele in openBrackets:
                stack.append(ele)
            else:
                if len(stack)==0:
                    return False
                elif ele==')':
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        return False
                elif ele==']':
                    if stack[-1]=='[':
                        stack.pop()
                    else:
                        return False
                elif ele=='}':
                    if stack[-1]=='{':
                        stack.pop()
                    else:
                        return False
            if len(stack)==0:
                return True
            return False
value=Solution()
s=input()
print(value.isValid(s))
