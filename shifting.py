import random
from collections import deque

alphas=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
word=input("Enter a text:-")
word=str(word)
word=word.lower()
word_char=list(word)
encno=['54','83','27','43','81','18','0','17','23','29','37','72','9','1','3','5','6','8','7','10','50','40','31','35','63','25','99']
len_word_list=len(word_char)
encmsg=''
len_alp_list=len(alphas)
#nolist=[]
encno2=encno

def encode_message(nolist): 
	for j in range(0,len_word_list):
		index=alphas.index(word_char[j])
		encmsg+=nolist[index]+' '
	print(encmsg)

encno2=encno

def shift_no_list():
	shift_value=random.randint(0,10)
	encno2=deque(encno2)
	encno2.rotate(shift_value)
	encno2=list(encno2)

shift_no_list()
encode_message(encno2)
