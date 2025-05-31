from ..core import *
from .. import HTMLNodes as nodes

# def html(self, innerText:str="", innerHTML:HTMLSet=None, lang:str="", **attribute)->HTMLElement:
#     return nodes.Html(innerText, innerHTML, lang, attribute)

class VStack(nodes.Div):
    def __init__(self,innerHTML:HTMLSet=None,innerText:str='',**attributes):
        super().__init__(innerHTML=innerHTML if innerHTML else HTMLSet()<<String(innerText),class_='VStack')
        self.tag='div'

class HStack(nodes.Div):
    def __init__(self,innerHTML:HTMLSet=None,innerText:str='',**attributes):
        super().__init__(innerHTML=innerHTML if innerHTML else HTMLSet()<<String(innerText),class_='VStack')
        self.tag='div'



def NavigationBar(title:str,navigationNodes:list[HTMLElement]):
    return nodes.Nav(HTMLSet([
        nodes.Div(HTMLSet([
            nodes.Div(title,class_="title"),
            nodes.Ul(
                
                ForEach(navigationNodes,lambda node: nodes.Li(node))
            )
        ]),class_="cont")
    ]))
    