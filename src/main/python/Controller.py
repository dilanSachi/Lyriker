from SpellCorrector import SpellCorrector
from WordNormalizer import WordNormalizer

class Controller():

    def __init__(self, aContext):
        self.aContext = aContext

    def processLyricInput(self, uInput, jsondb):

        wn = WordNormalizer()
        uInputDict = wn.normalizeLyrics([uInput])

        spn = SpellCorrector(jsondb)
        originalWordsDB = jsondb.getOriginalWordsDB()
        
        probableSongs = []
        probableSongsFrequency = []
        mostFrequentWordList = []
        mostRelevantSongs = []
        mostRelevantSongFrquency = []
        editCounter = []
        #uInputWords = uInput.lower().strip().split(" ")
        for uInputWord in uInputDict:
            print(uInputWord)
            matchingWords = spn.checkMatchingWords(uInputWord)
            mostFrequentWordList.append(spn.getMostFrequentWords(matchingWords))
        print(mostFrequentWordList)
        
        for array in mostFrequentWordList:
            temp = []
            tempFrequency = []
            for word in array:
                try:
                    wordData = originalWordsDB[word]
                    temp.append(wordData[0])
                    tempFrequency.append(wordData[1])
                except:
                    print("some error")
            probableSongs.append(temp)
            probableSongsFrequency.append(tempFrequency)
        
        i = 0
        #print("len",len(probableSongs))
        for arr in probableSongs:
            #print("hey")
            for songarr in arr:
                #print("songarr",len(songarr))
                for song in songarr:
                    #print(song)
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
        for i in range(8):
            if(len(mostRelevantSongFrquency)==i):
                break
            ind = mostRelevantSongFrquency.index(max(mostRelevantSongFrquency))
            print(mostRelevantSongFrquency[ind])
            results.append(mostRelevantSongs[ind])
            mostRelevantSongFrquency[ind] = 0

        return results

    def processArtistNameInput(self, uInput, jsondb):

        mostFrequentArtists = []
        wn = WordNormalizer()
        uInputList = wn.normalizeArtistNames(uInput)
        originalNamesDB = jsondb.getOriginalNamesDB()
        probableSongs = []
        mostRelevantSongs = []
        mostRelevantSongFrquency = []
        editCounter = []



        for inp in uInputList:
            sp = SpellCorrector(jsondb)
            matchingArtists = sp.checkMatchingArtists(inp)
            mostFrequentArtists.append(sp.getMostFrequentArtistNames(matchingArtists))

        for array in mostFrequentArtists:
            temp = []
            for word in array:
                try:
                    wordData = originalNamesDB[word]
                    temp.append(wordData)
                except:
                    print("some error")
            probableSongs.append(temp)
        
        i = 0
        #print("len",len(probableSongs))
        for arr in probableSongs:
            #print("hey")
            for songarr in arr:
                #print("songarr",len(songarr))
                for song in songarr:
                    #print(song)
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
        for i in range(8):
            if(len(mostRelevantSongFrquency)==i):
                break
            ind = mostRelevantSongFrquency.index(max(mostRelevantSongFrquency))
            print(mostRelevantSongFrquency[ind])
            results.append(mostRelevantSongs[ind])
            mostRelevantSongFrquency[ind] = 0

        return results

    def getSongData(self, results, jsondb):
        songsDB = jsondb.getSongsDB()
        songData = []

        for song in results:
            songData.append(songsDB["Songs"][song-1])
        
        #print(songData['Title'])
        return songData