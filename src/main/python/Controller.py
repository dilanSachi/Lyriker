from SpellCorrectorNew import SpellCorrectorNew

class Controller():

    def __init__(self, aContext):
        self.aContext = aContext

    def processUInput(self, uInput, jsondb):
        spn = SpellCorrectorNew(self.aContext, jsondb)
        originalWordsDB = jsondb.getOriginalWordsDB()
        
        probableSongs = []
        probableSongsFrequency = []
        mostRelevantWordArray = []
        mostRelevantSongs = []
        mostRelevantSongFrquency = []
        editCounter = []
        uInputWords = uInput.lower().strip().split(" ")
        for uInputWord in uInputWords:
            matchingWords = spn.checkMatchingWords(uInputWord)
            mostRelevantWordArray.append(spn.getMostRelevantWords(matchingWords))
        print(mostRelevantWordArray)
        
        for array in mostRelevantWordArray:
            for word in array:
                try:
                    wordData = originalWordsDB[word]
                    probableSongs.append(wordData[0])
                    probableSongsFrequency.append(wordData[1])
                except:
                    print("some error")
        i = 0
        for array in probableSongs:
            for song in array:
                try:
                    ind = mostRelevantSongs.index(song)
                    if(i != editCounter[ind]):
                        mostRelevantSongFrquency[ind] +=1
                        editCounter[ind] += 1
                except:
                    mostRelevantSongs.append(song)
                    mostRelevantSongFrquency.append(1)
                    editCounter.append(i)
            i += 1
        results = []
        for i in range(5):
            if(len(mostRelevantSongFrquency)==i):
                break
            ind = mostRelevantSongFrquency.index(max(mostRelevantSongFrquency))
            results.append(mostRelevantSongs[ind])
            mostRelevantSongFrquency[ind] = 0

        return results

    def processSongResults(self, results, jsondb):
        songsDB = jsondb.getSongsDB()
        songData = []

        for song in results:
            songData.append(songsDB["Songs"][song-1]['Title'])
        
        print(songData)
        return songData