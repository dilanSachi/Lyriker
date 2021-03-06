from SpellCorrector import SpellCorrector
from WordNormalizer import WordNormalizer

class Controller():

    def __init__(self, aContext):
        self.aContext = aContext

    def processInput(self, uType, uInput, jsondb):
        print(uInput)
        wn = WordNormalizer()
        uInputDict = wn.normalizeLyrics([uInput])

        spn = SpellCorrector(jsondb)
        if(uType == "lyric"):
            originalDB = jsondb.getOriginalWordsDB()
        elif(uType == "artist"):
            originalDB = jsondb.getOriginalNamesDB()
        elif(uType == "album"):
            originalDB = jsondb.getOriginalAlbumsDB()
        
        probableSongs = []
        probableSongsFrequency = []
        mostFrequentWordList = []
        mostRelevantSongs = []
        mostRelevantSongFrquency = []
        editCounter = []
        #uInputWords = uInput.lower().strip().split(" ")
        for uInputWord in uInputDict:
            #print(uInputWord)
            matchingWords = spn.checkMatches(uType, uInputWord)
            data = spn.getMostFrequentWords(matchingWords)
            mostFrequentWords = data[0]
            
            if(uType != "artist" and data[1] == 1):
                mostFrequentWords = mostFrequentWords + spn.stemInputAndCheckMatch(uType, uInputWord)

            mostFrequentWordList.append(mostFrequentWords)
        print(mostFrequentWordList)
        print(len(mostFrequentWordList))
        
        for array in mostFrequentWordList:
            temp = []
            tempFrequency = []
            for word in array:
                try:
                    wordData = originalDB[word]
                    temp.append(wordData)
                    #tempFrequency.append(wordData[1])
                except:
                    print("some error")
            probableSongs.append(temp)
            probableSongsFrequency.append(tempFrequency)
        
        i = 0
        for arr in probableSongs:
            for songarr in arr:
                for song in songarr:
                    try:
                        ind = mostRelevantSongs.index(song)
                        #print("i",i)
                        if(i > editCounter[ind]):
                            mostRelevantSongFrquency[ind] +=1
                            editCounter[ind] = i
                    except:
                        mostRelevantSongs.append(song)
                        mostRelevantSongFrquency.append(1)
                        editCounter.append(i)
            i = i + 1
        results = []
        #print(mostRelevantSongs)
        #print(mostRelevantSongFrquency)
        for i in range(15):
            if(len(mostRelevantSongFrquency)==i):
                break
            ind = mostRelevantSongFrquency.index(max(mostRelevantSongFrquency))
            #print(mostRelevantSongFrquency[ind])
            results.append(mostRelevantSongs[ind])
            mostRelevantSongFrquency[ind] = 0

        return results

    def getSongsData(self, results, jsondb):
        songsDB = jsondb.getSongsDB()
        songsData = []

        for song in results:
            #print(song)
            songsData.append(songsDB["Songs"][song-1])
        
        #print(songData['Title'])
        return songsData