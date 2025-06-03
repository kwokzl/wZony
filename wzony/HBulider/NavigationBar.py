from ..core import *
from .. import HNodes as nodes

specificStyle="""
nav{
    border-top: rgb(218, 218, 218) 1px solid;
    border-bottom: rgb(218, 218, 218) 1px solid;
    box-shadow: 0px 0px 20px rgba(218, 218, 218,0.6);
}

nav *{
    display:inline-block;
    align-items:center;
}
nav .cont{
    display:flex;
    justify-content: space-around;
    font-size:20px;
    

}

nav div{
    padding:0;
}

nav .title{
    font-size:35px;
}
"""

def NavigationBar(title:str,navigationNodes:list[HTMLElement]):
    element=nodes.Nav(HTMLSet([
        nodes.Div(HTMLSet([
            nodes.Div(title,class_="title"),
            nodes.Ul(
                
                ForEach(navigationNodes,lambda node: nodes.Li(node))
            )
        ]),class_="cont")
    ]))
    element.specificStyle=specificStyle
    return element