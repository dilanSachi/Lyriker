from WordNormalizer import WordNormalizer

class LyricsFormatter():

    def __init__(self, aContext):
        self.aContext = aContext
        self.normalizer = WordNormalizer()

    def formatLyrics(self):
        