from os import listdir

class ErrorSameFiles(Exception):
	def __str__(self):
		return "You can not change original file! "

def avoid_empty_input(msg):

	def check_input_extension(fname):
		if not fname.endswith(".txt"):
			return fname+".txt"
		else:
			return fname
	
	s=check_input_extension(input(msg))
	while len(s)==4:
		s=check_input_extension(input(msg))
			
	return s


get_txt_files=[i for i in listdir() if i.endswith(".txt")]

if len(get_txt_files) > 0:
	print("Введіть ім'я файлу (наприклад, test) або ім'я файлу з розширенням (наприклад, test.txt)!")
	print("Програма працює виключно з файлами типу *.txt")
	print("Список доступних файлів виведено нижче!")
	for i in get_txt_files:
		print(i)

	select_first_file=avoid_empty_input("Select first file: ")

	
	with open(select_first_file, mode="r") as f:
		select_second_file=avoid_empty_input("Enter name : ")
		if select_first_file == select_second_file:
			raise ErrorSameFiles
		with open(select_second_file, mode="w") as fw:

			for c,i in enumerate(f, start=1):
				fw.write(f"{c}:  {i}")
else:
	print("No txt files inside this folder!")
