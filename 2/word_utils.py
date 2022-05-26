from string import punctuation



s="""Hello, world! How are you!!!? asd1*
seco choi, sad
"""
for i in s:
		for letter in i:

			if letter in punctuation:
				
				s=s.replace(letter,"")

print(s)
print("Список ",s.split())
d={}
for i in s.split():
	d[i]=len(i)

max_len_word = max(d.values())
max_word=([(k,v) for k,v in d.items() if v == max_len_word])
for i,j in max_word:
	print(f"Саме довге слово це ---> {i} складається з {j} символів!")
		



