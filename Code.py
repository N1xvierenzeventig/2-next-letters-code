# The idea of the program is for somebody to give you a sentence or code and you have to convert is in the sentence but every single letter makes 2 steps to the right alphabetically.
a = (input("Your sentence: "))
b = []
list = {"a":"1", "b":"2", "c":"3", "d":"4", "e":"5", "f":"6", "g":"7", "h":"8", "i":"9", "j":"10", "k":"11", "l":"12", "m":"13", "n":"14", "o":"15", "p":"16", "q":"17", "r":"18", "s":"19", "t":"20", "u":"21", "v":"22", "w":"23", "x":"24", "y":"25", "z":"26"}
list2 = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e",6:"f", 7:"g", 8:"h",9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}
def ab(a,b):
    for letter in a:
        if letter in "' ',''',1,2,3,4,5,6,7,8,9,0":
            letter_is_nothing = True
        else:
            letter_is_nothing = False

        if letter.isupper() and letter_is_nothing is False:
            Upper_Letter = True
            letter = letter.lower()
        elif letter.islower and letter_is_nothing is False:
            Upper_Letter = False
        else:
            letter = letter



        if letter_is_nothing == False:
            qwerty = list[letter]
            s = int(qwerty)
            s += 2
            if s == 27:
                s = s-26
            elif s == 28:
                s = s-26
            if Upper_Letter == True:
                t = list2[s]
                t = t.upper()
            elif Upper_Letter == False:
                t = list2[s]
            b.append(t)
        else:
            b.append(letter)









def io():
        c = "".join(str(x) for x in b)
        print(c)



ab(a,b)
io()
