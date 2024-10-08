class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = list(file_name)

    def get_all_words(self):
        all_words = {}
        for file in self.file_name:
            with open(file, encoding='utf-8') as file_list:
                file_all_str = []
                for line in file_list:
                    replace_ = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    line = line.lower()
                    for change in replace_:
                        line = line.replace(change, '')
                    for word in line.split():
                        file_all_str.append(word)
                all_words[file] = file_all_str
        return all_words

    def find(self, word):
        result_ = {}
        for file, word_ in self.get_all_words().items():
            change = 1
            for i in word_:
                if word.lower() == i:
                    result_[file] = change
                    break
                change += 1
        return result_

    def count(self, word):
        result_ = {}
        for file, word_ in self.get_all_words().items():
            counter = 0
            for i in word_:
                if word.lower() == i:
                    counter += 1
            result_[file] = counter
        return result_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
print('--------')
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
print('--------')
finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
print('--------')
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
print('--------')
finder1 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))
