import random
from collections import deque

alphas=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
word=input("Enter a text:-")
word=str(word)
word=word.lower()
word_char=list(word)
encno=['54','83','27','43','81','18','0','17','23','29','37','72','9','1','3','5','6','8','7','10','50','40','31','35','63','25','99']
len_word_list=len(word_char)
#encmsg=' '
len_alp_list=len(alphas)
#encno2=encno
encno2=encno

def shift_no_list(list_temp):
    shift_value=random.randint(1,10)
  #  print(shift_value)
    list_temp=deque(list_temp)
    list_temp.rotate(shift_value)
 #   print(list_temp)
    list_temp=list(list_temp)
#    print encno2
    return list_temp

encno2=shift_no_list(encno2)

#print "TEST:- ",encno2

def encode_message(encmsg):
    for j in range(0,len_word_list):
        index=alphas.index(word_char[j])
        encmsg+=encno2[index]+' '
    print(encmsg)

encode_message('')
