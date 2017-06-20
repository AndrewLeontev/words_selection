import re

def return_dict(filename):
    """Функция разбивает текст на отдельные слова и возвращает словарь"""
    try:
        #Открываем  файл и считываем текст 
        with open(filename) as f_obj:
            contents = f_obj.read()
            
    except FileNotFoundError:
        #Если файл не найден, выдаем сообщение об ошибке и возвращаем
        # пустой словарь
        msg = "Sorry, the file " + filename + " does not exists."
        print(msg)
        words = ['Нет файла']
        return words
        
    else: 
        #Если все впорядке, то разбиваем текст на отдельны слова
        # и пакуем в словарь, который возвращает функция + удаляем "левые"
        # символы с помощью регулярных выражений
        words = re.split(r'[-_#$*=+@/;,.?!:\[\(\]\)\'\s\"1-9]', contents.lower())
        bad_word = return_reg_words()
        words_finaly = []
        for word in words:
            if len(word) > 2 and word not in bad_word:
                words_finaly.append(word.lower())
        return words_finaly

def return_reg_words():
    
    try:
        with open('reg_words.txt') as f_obj:
            contents = f_obj.read()
    except:
        print("Не найден файл исключающихся слов")
        with open('reg_words.txt', 'w') as f_obj:
            f_obj.write("")
        reg_words = ['Нет файла']
        return reg_words
    else:
        reg_words = contents.lower().split()
    """
    #список исключающихся слов
    reg_words = ['the', 'you', 'for', 'and', 'me', 'for', 'with', 
                'this', 'are', 'his', 'was', 'they', 'all', 'he', 
                'she', 'not', 'then', 'its', 'her', 'them', 'there',
                'that', 'god'
                ]
    """
    
    return reg_words
    
def return_sorted_words(words_main):
    words_sorted = []
    words_sorted = set(words_main)
    return words_sorted

def return_words(words_main, number_words,file_out):
    """
    подсчитываем количество слов в словаре и выводим встречающиеся более
    number_words раз
    """
    
    #Для начала отберем из words слова без повторения
    words_sorted = return_sorted_words(words_main)
    number = 0
    file_out_cut = file_out[:-4] + "_cut.txt"
    
    #Очистим файл вывода
    with open(file_out, 'w') as f_obj:
        f_obj.write("")
    with open(file_out_cut, 'w') as f_obj:
        f_obj.write("")
    
    #список исключающихся слов
    reg_words = []
    reg_words = return_reg_words()
    
    #перебираеет для каждого слова из списка сколько раз встречается
    # в основном списке затем выводит это слово и сколько раз 
    # попадается в тексте + результат записывает в файл
    # слова которые не вошли в диапазон пользователя - записывает
    # в отдельный файл с подписью вначале 'cut_'
    for word in words_sorted:
        if len(word) > 2 and word.lower() not in reg_words:
            number = words_main.count(word)
            if number >= number_words:
                prnt = word + " - встречается " + str(number) + " раз"
                print(prnt)
                with open(file_out, 'a') as f_obj:
                    f_obj.write(prnt + "\n")
            elif number >= 2 and number < number_words:
                prnt = word + " - встречается " + str(number) + " раз"
                with open(file_out_cut, 'a') as f_obj:
                    f_obj.write(prnt + "\n")
        number = 0
    print("Список сохранен в файл: " + file_out)

def return_words_limit(words_main, numbers_from, numbers_to,file_out):
    """
    подсчитываем количество слов в словаре и выводим встречающиеся более
    numbers_from и до numbers_to раз
    """
    
    #Для начала отберем из words слова без повторения
    words_sorted = return_sorted_words(words_main)
    number = 0

    #Очистим файл вывода
    with open(file_out, 'w') as f_obj:
        f_obj.write("")
    
    #список исключающихся слов
    reg_words = return_reg_words()
    
    #перебираеет для каждого слова из списка сколько раз встречается
    # в основном списке затем выводит это слово и сколько раз 
    # попадается в тексте + результат записывает в файл
    for word in words_sorted:
        if len(word) > 2 and word.lower() not in reg_words:
            number = words_main.count(word)
            if number >= numbers_from and number <= numbers_to:
                prnt = word + " - встречается " + str(number) + " раз"
                print(prnt)
                with open(file_out, 'a') as f_obj:
                    f_obj.write(prnt + "\n")

        number = 0
    print("Список сохранен в файл: " + file_out)

def return_maximum(words_main):
    #Ищем 80 процентов от макс числа
    max_number = 0
    words_sorted = return_sorted_words(words_main)
    for word in words_sorted:
        count_in_main = words_main.count(word)
        if count_in_main > max_number:
            max_number = count_in_main
    
    return max_number

def return_percent(filename_out, maximum, words_main):
    """
    Принимает на вход файл, после чего обрабатывает неаходя максимум и по 
    этому максимуму ищет слова которые попадаються чаще 80% раз
    """
    bad_word = return_reg_words()
    words_sorted = return_sorted_words(words_main)
    max_numb = maximum
    
    with open(filename_out, 'w') as f_obj:
        f_obj.write("")
    
    percent = int(max_numb * 0.2)
    
    for word in words_sorted:
        if words_main.count(word) > percent:
            print(word)
            with open(filename_out, 'a') as f_obj:
                f_obj.write(word + "\n")
    print("Список сохранен в файл: " + filename_out)
