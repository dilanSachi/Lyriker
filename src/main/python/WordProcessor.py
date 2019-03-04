import glob
import os, sys
from LetterDeleter import LetterDeleter
from MySqlConnector import MySqlConnector

def splitLyrics(filename):

    print(filename)

    os.chdir("../../../../Songs/")
    file = open(filename, "r")

    songWords = []

    file.readline()
    song = file.readline()
    file.readline()
    artist = file.readline()
    file.readline()
    file.readline()
    for line in file:
        if(line[-1:] == "\n"):
            lineWords = line.split(" ")
            lineWords[-1] = lineWords[-1][:-1]
            songWords = songWords + lineWords
        else:
            lineWords = line.split(" ")
            lineWords[-1] = lineWords[-1]
            songWords = songWords + lineWords
    os.chdir("../GUI/src/main/python/")

    return song, artist, songWords

def removeDuplicated(words):
    uniqueWordSet = []
    for i in range(len(words)):
        if (words[i] not in uniqueWordSet):
            uniqueWordSet.append(words[i])
    return uniqueWordSet

def collectUniqueWordsInSong(wordToEdit, deleteDistance, uniqueWordSet):
    ld = LetterDeleter()
    editedWords = ld.deleter(wordToEdit, deleteDistance)
    uniqueWordSet = uniqueWordSet + editedWords
    uniqueWordSet = removeDuplicated(uniqueWordSet)
    return uniqueWordSet

def insertWordsToDatabase(uniqueWordSet, songName):
    msc = MySqlConnector()
    #errorCount = 0
    #print(len(uniqueWordSet))
    #try:
    for i in (uniqueWordSet):
        check = checkDatabaseForWord(i)
        a = False
        for word_id,word in check:
            print("blh")
            a = True
            query2 = "insert into songs(song_id,word_id) values(%s,%s)"
            msc.executeQuery(query2, songName,word_id)
        #if (check == False):

        if(a == False):
            #print("bladasdh")
            query1 = "insert into words(word) values(%s)"
            msc.executeQuery(query1, i)
            query2 = "select * from words where word=(%s)"
            result = msc.executeQuery(query2, i)
            for word_id, word in result:
                query3 = "insert into songs(song_id,word_id) values(%s,%s)"
                #print(word_id)
                msc.executeQuery(query3, songName, word_id)
    #except:
    #    print("Error")
    #    errorCount = errorCount + 1
    #print(errorCount)

def processSongsWithDatabase():
    for i in range(1,13):
        splittedSong = splitLyrics(str(i)+".txt")
        splittedLyrics = splittedSong[2]
        uniqueWordSet = []
        for word in (splittedLyrics):
            word = word.lower()
            uniqueWordSet = collectUniqueWordsInSong(word, 1, uniqueWordSet)
            #print(uniqueWordSet)
        print(str(i)+".txt")
        insertWordsToDatabase(uniqueWordSet, i)

def checkDatabaseForWord(word):
    msc = MySqlConnector()
    query = ("select * from words where word=%s")
    #"insert into songs(song_id,word_id) values('%s','%s')"
    result = msc.executeQuery(query, word)
    return result

processSongsWithDatabase()
#print(checkDatabaseForWord("'dilan"))
#insertWordsToDatabase("kakkiKolla", 2)