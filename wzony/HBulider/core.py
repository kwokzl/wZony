from ..core import *
from .. import HNodes as nodes
import os
 
current_path = os.path.abspath(__file__)
package_dir = os.path.dirname(current_path)
coreCss_path = os.path.join(package_dir, 'core.css')

# def html(self, innerText:str="", innerHTML:HTMLSet=None, lang:str="", **attribute)->HTMLElement:
#     return nodes.Html(innerText, innerHTML, lang, attribute)

class VStack(nodes.Div):
    def __init__(self,innerHTML:HTMLSet=None,innerText:str='',**attributes):
        super().__init__(innerHTML=innerHTML if innerHTML else HTMLSet()<<String(innerText),class_='VStack')
        self.tag='div'

class HStack(nodes.Div):
    def __init__(self,innerHTML:HTMLSet=None,innerText:str='',**attributes):
        super().__init__(innerHTML=innerHTML if innerHTML else HTMLSet()<<String(innerText),class_='HStack')
        self.tag='div'



    
def Page(body:HTMLSet,head:HTMLSet=None,charset='utf-8'):
    with open(coreCss_path) as coreCss:
        return nodes.Html(HTMLSet([
            nodes.Head(HTMLSet([
                head if head else HTMLSet(),
                nodes.Meta(charset=charset),
                nodes.Style(coreCss.read()),
                nodes.Style("\n".join([style for style in body.specificStyle]))
            ])),
            nodes.Body(body)
        ]))