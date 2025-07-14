class Language:
    def __init__(self,languageCode="",strDict:dict=None):
        self.languageCode=languageCode
        self.strDict=strDict if strDict else dict()

