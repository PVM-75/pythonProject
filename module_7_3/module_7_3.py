# name = "sample2.txt"
# with open(name, encoding='utf-8') as file:
#     for line in file:
#         print(line, end='')

class WordsFinder:
    file_names = []
    all_words = {}

    def __init__(self, *args):
        for item in args:
            self.file_names.append(item)
            with open(item, encoding='utf-8') as file:
                punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                text = ''.join(char for char in file if char not in punctuation) # очищаем от знаков пунктуации
                lowercase_text = text.lower() # переводим в нижний регистр
                words_list = lowercase_text.split() # текст в список
                self.all_words[item] = words_list # добавляем значение в словарь

    def get_all_words(self):
        return self.all_words

    def find(self, request):
        dict = {}
        for key, value in self.all_words.items():
            for item in value:
                if request.lower() == item:
                    dict[key] = value.index(item) + 1 # Плюс 1, так как индексы считаются с 0
                    break
        return dict

    def count(self, request):
        result = {}
        for key, value in self.all_words.items():
            counter = 0
            for item in value:
                if request.lower() == item:
                    counter += 1
                    result[key] = counter
        return result

if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))