def reverse_sentence(sentence):
    lst = sentence.split(" ")
    #print(lst) //debug
    lst.reverse()
    #print(lst) //debug
    return " ".join(lst)

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))