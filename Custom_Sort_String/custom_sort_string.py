# Task:
# order and str are strings composed of lowercase letters. In order, no letter
# occurs more than once.

# order was sorted in some custom order previously. We want to permute the 
# characters of str so that they match the order that order was sorted. More 
# specifically, if x occurs before y in order, then x should occur before y in 
# the returned string.

# Return any permutation of str (as a string) that satisfies this property.

# Example:
# Input: 
# order = "cba"
# str = "abcd"
# Output: "cbad"
# Explanation: 
# "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

# Constraints:
# 1. order has length at most 26, and no character is repeated in order.
# 2. str has length at most 200.
# 3. order and str consist of lowercase letters only.

def customSortString(order, str):
    linker = {k:v for (v,k) in enumerate(order)}
    linker = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25,'':26}
    str = list(str)

    for i in range(1, len(str)):
        key = str[i]
        j = i-1
        while j >=0:
            if key in linker and str[j] in linker:
                if linker[key] < linker[str[j]]:
                    str[j+1] = str[j]
                    j -= 1
                else:
                    break
            else:
                j -= 1
                
        str[j+1] = key
    return "".join(str)

print(customSortString("exv","xwvee"))

# TODO: INCOMPLETE. Issue is that it basically ignores the characters that arent
# in the map. Not sure how to solve this.