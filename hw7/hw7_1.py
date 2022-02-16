#Make a program that has some sentence (a string) on input and returns a dict
#containing all unique words as keys and the number of occurrences as values.

def add_word(out_dict, word):
    if word == "":
        return ""

    l_word = word.lower()

    if out_dict.get(l_word):
        out_dict[l_word] = out_dict.get(l_word) + 1
    else:
        out_dict[l_word] = 1

#main code

usr_str = input("Write your text: ")

word = ""
out_dict = {}

for i in usr_str:
    if i.isalpha():
        word = word+ i
    else:
        add_word(out_dict, word)
        word = ""

add_word(out_dict, word)      #after all add the last word

print(out_dict)

#Understand there is an easier way to do this, but dont know how at this time