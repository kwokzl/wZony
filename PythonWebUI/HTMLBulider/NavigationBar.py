from ..core import *
from .. import HTMLNodes as nodes

def NavigationBar(title:str,navigationNodes:list[HTMLElement]):
    return nodes.Nav(HTMLSet([
        nodes.Div(HTMLSet([
            nodes.Div(title,class_="title"),
            nodes.Ul(
                
                ForEach(navigationNodes,lambda node: nodes.Li(node))
            )
        ]),class_="cont")
    ]))

