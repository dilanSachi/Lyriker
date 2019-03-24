from SpellCorrectorNew import SpellCorrectorNew

class Controller():


    def __init__(self, aContext):
        self.aContext = aContext

    def processUInput(self, uInput, jsondb):
        spn = SpellCorrectorNew(self.aContext, jsondb)
        probableWords = []
        mostRelevantWords = []
        uInputWords = uInput.lower().strip().split(" ")
        for uInputWord in uInputWords:
            matchingWords = spn.checkMatchingWords(uInputWord)
            mostRelevantWords.append(spn.getMostRelevantWords(matchingWords))
        print(mostRelevantWords)