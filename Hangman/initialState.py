import random

class Board:
    def __init__(self, repo):
        self.repo = repo
    
    def choose_sentence(self):
        sentence = random.choice(self.repo.sentences)
        return sentence

    def transform_word(self, word):
        first = word[0]
        last = word[len(word)-1]
        new_word = ''
        for i in word:
            if i != first and i != last:
                new_word += '_'
            else:
                new_word += i
        return new_word

    # def change_letter()

    def change_letter(self, sentence, transf_s, l):
        trans = ''
        for i in range(0,len(sentence)):
            if sentence[i] == transf_s[i] or sentence[i] == l:
                trans += sentence[i]
            else:
                trans += '_'
        return trans
    
    def sentence_to_hangman(self, sentence):
        letters = []
        new_sentence = ''
        letters.append(sentence[0])
        letters.append(sentence[len(sentence)-1])
        for l in range(0,len(sentence)):
            if sentence[l] == ' ':
                letters.append(sentence[l-1])
                letters.append(sentence[l+1])
        for i in sentence:
            if i not in letters and i != ' ':
                new_sentence += '_'
            else:
                new_sentence += i
        return new_sentence

'''
def transform_word(word):
        first = word[0]
        last = word[len(word)-1]
        new_word = ''
        for i in word:
            if i != first and i != last:
                new_word += '_'
            else:
                new_word += i
        return new_word

def sentence_to_hangman2(sentence):
        letters = []
        new_sentence = ''
        for l in range(0,len(sentence)):
            if sentence[l] == ' ':
                letters.append(sentence[l-1])
                letters.append(sentence[l+1])
        for i in sentence:
            if i not in letters:
                new_sentence += '_'
            else:
                new_sentence += i
        return new_sentence
        

def sentence_to_hangman(sentence):
        sentence = sentence.replace('\n','')
        words = sentence.split(' ')
        words_2 = []
        for w in words:
            w = transform_word(w)
            words_2.append(w)
        hangman_sentence = ''
        for w in words_2:
            hangman_sentence += w
            hangman_sentence += ' '
        return hangman_sentence

print(sentence_to_hangman2('ana has apples'))
'''