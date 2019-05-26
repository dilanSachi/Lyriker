class LetterDeleter():

    def __init__(self):
        self.edits = []

    def deleteLetter(self, word, index):
        newWord = word[0:index] + word[index+1:]
        return newWord

    def delete(self, word, distance):
        if(distance == 0):
            return self.edits
        for i in range(len(word)):
            newWord = self.deleteLetter(word, i)
            if(len(newWord)>0 and newWord not in self.edits):
                #if(distance == 1):
                self.edits.append(newWord)
                self.delete(newWord, distance-1)
        return self.edits

    def removeDuplicates(self, words):
        uniqueWordSet = []
        for i in words:
            if (i not in uniqueWordSet):
                uniqueWordSet.append(i)
        return uniqueWordSet

