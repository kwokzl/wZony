from ..core import *
from .. import HTMLNodes as nodes

# def html(self, innerText:str="", innerHTML:HTMLSet=None, lang:str="", **attribute)->HTMLElement:
#     return nodes.Html(innerText, innerHTML, lang, attribute)

def VStack(innerHTML:HTMLSet=None):
    return nodes.Div(innerHTML=innerHTML,class_="VStack")

def HStack(innerHTML:HTMLSet=None):
    return nodes.Div(innerHTML=innerHTML,class_="HStack")

def NavigationBar(title:str,navigationNodes:list[HTMLElement]):
    return nodes.Nav(HTMLSet([
        nodes.Div(HTMLSet([
            nodes.Div(title,class_="title"),
            nodes.Ul(
                
                ForEach(navigationNodes,lambda node: nodes.Li(node))
            )
        ]),class_="cont")
    ]))
    