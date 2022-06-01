from errors import NoWords, SmallWord, Duplicate

class Repository:
    def __init__(self, file_name):
        self.sentences = []
        self.file_name = file_name
        self.load_file()
        self.save_file()

    def load_file(self):
        f = open(self.file_name,'r')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            self.sentences.append(line)
        f.close

    def write_sentence(self,sentence):
        '''
        writes a sentence to the file
        params:
            sentence - string
        errors:
            NoWords - sentence has less than two words
            SmallWord - at least one word has less than three letters
        '''
        if ' ' not in sentence:
            raise NoWords
        words = sentence.split(' ')
        for w in words:
            if len(w) < 3:
                raise SmallWord
        sentence += '\n'
        for s in self.sentences:
            if s == sentence:
                raise Duplicate
        self.sentences.append(sentence)
        self.save_file()


    def save_file(self):
        '''
        saves the file
        (writes all items from the repo into the file)
        '''
        f = open(self.file_name,'w')
        for o in self.sentences:
            f.write(o)
        f.close
