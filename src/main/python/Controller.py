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
                        if(i != editCounter[ind]):
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
        for i in range(25):
            if(len(mostRelevantSongFrquency)==i):
                break
            ind = mostRelevantSongFrquency.index(max(mostRelevantSongFrquency))
            print(mostRelevantSongFrquency[ind])
            results.append(mostRelevantSongs[ind])
            mostRelevantSongFrquency[ind] = 0

        return results

    def processSongResults(self, results, jsondb):
        songsDB = jsondb.getSongsDB()
        songData = []
        print(songsDB['Songs'][11244]['Title'])

        for song in results:
            songData.append(songsDB["Songs"][song-1])
        
        #print(songData['Title'])
        return songData