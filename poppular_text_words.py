#from words_generator import return_dict, return_words, return_words_limit
from words_generator import *

filename = input("Введите название .txt файла: ")
filename = filename + ".txt"
filename_out = filename[:-4] + "_out.txt"

words_in = []
words_in = return_dict(filename)

print("\nВведите 1 - если вы хотите работать с диапозоном чисел от и до.")
print("Введите 2 если хотите работать с числами выше n.")
select_action = input("Введите 3 для автоматического вывода самых используемых слов: ")

if select_action == '1':
	number_words_from = int(input("\nВведите от скольки выпадений: "))
	number_words_to = int(input("Введите по какое количество выводить: "))
	return_words_limit(words_in, number_words_from, 
        number_words_to, filename_out)
    
elif select_action == '2':
	number_words = int(input("Сколько раз выпадает слово: "))
	return_words(words_in, number_words, filename_out)

elif select_action == '3':
    print("\nПодождите идет генерация списка")
    max_number = return_maximum(words_in)
    return_percent(filename_out, max_number, words_in)
    
