from .language import *

class Localization(dict):
    def __init__(self,langCode:str,languages:list[Language]=None,debug=False):
        self.langCode=langCode
        self.strDicts:dict[str,dict[str,str]]={}
        self.debug=debug
        for lang in languages:
            self.strDicts[lang.languageCode]=lang.strDict
        super().__init__()
        if langCode in self.strDicts:
            self.update(self.strDicts[langCode])
        else:
            raise ValueError()
         
    def addLanguage(self,language:Language):
        self.strDicts[language.languageCode]=language.strDict

    def addLanguages(self,languages:list[Language]):
        for lang in languages:
            self.strDicts[lang.languageCode]=lang.strDict

    def otherLang(self,langCode:str):
        return self.strDicts[langCode]
    
    def changeLang(self,langCode:str):
        self.update(self.strDicts[langCode])

    def __missing__(self,key):
        print(f"{key} is undefined")
        return key
