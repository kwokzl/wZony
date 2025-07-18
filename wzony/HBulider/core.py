from ..core import *
from .. import HNodes as nodes
import os
 
current_path = os.path.abspath(__file__)
package_dir = os.path.dirname(current_path)
coreCss_path = os.path.join(package_dir+'/static', 'core.css')

# def html(self, innerText:str="", innerHTML:HTMLSet=None, lang:str="", **attribute)->HTMLElement:
#     return nodes.Html(innerText, innerHTML, lang, attribute)

# class VStack(nodes.Div):
#     def __init__(self,innerHTML:HTMLSet=None,innerText:str='',**attributes):
#         super().__init__(innerHTML=innerHTML if innerHTML else HTMLSet()<<String(innerText),class_='VStack')
#         self.tag='div'

# class HStack(nodes.Div):
#     def __init__(self,innerHTML:HTMLSet=None,innerText:str='',**attributes):
#         super().__init__(innerHTML=innerHTML if innerHTML else HTMLSet()<<String(innerText),class_='HStack')
#         self.tag='div'

def VStack(innerHTML:list=None,innerText:str='',**attributes):
    element=nodes.Div()
    element.innerHTML(ForEach(innerHTML,lambda i:i))
    element.setClass('d-flex').setClass('flex-column').setClass('gap-3')
    

    return element

def HStack(innerHTML:list=None,innerText:str='',**attributes):
    element=nodes.Div()
    element.innerHTML(ForEach(innerHTML,lambda i:i))
    element.setClass('d-flex').setClass('flex-row').setClass('gap-3')
    return element

    
def Page(body:list,head:list=None,title="",charset='utf-8',bootstrapCss=None,bootstrapScript=None):
    with open(coreCss_path) as coreCss:
        return nodes.Html(HTMLSet([
            nodes.Head(HTMLSet([
                HTMLSet(head) if head else HTMLSet(),
                nodes.Meta(charset=charset),
                nodes.Title(title),
                nodes.Style(coreCss.read()),
                # nodes.Style("\n".join([style for style in body.specificStyle])),
                nodes.Link(href=bootstrapCss if bootstrapCss else 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css',rel='stylesheet'),
                nodes.Style(src=bootstrapScript if bootstrapScript else 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js')
            ])),
            nodes.Body(HTMLSet(body))
        ]))