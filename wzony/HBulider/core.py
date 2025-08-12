from ..core import *
from .. import HNodes as nodes
import os,enum
 
current_path = os.path.abspath(__file__)
package_dir = os.path.dirname(current_path)
# coreCss_path = os.path.join(package_dir+'/static', 'core.css')

class VStackAlignment(enum.Enum):
        leading='align-items-start'
        center='align-items-center'
        trailing='align-items-end'

class VStack(nodes.Div):

    def __init__(self,innerHTML:list=None,alignment:VStackAlignment=VStackAlignment.center,**attributes):
        super().__init__(innerHTML=None,**attributes)
        self.setInnerHTML(ForEach(innerHTML,lambda i:nodes.Div(i).setClass('gap-2').setClass('w-auto')))
        self.setClass('d-flex').setClass('flex-column').setClass('gap-2').setClass(alignment.value)

class HStackAlignment(enum.Enum):
        top='align-items-start'
        center='align-items-center'
        bottom='align-items-end'

class HStack(nodes.Div):

    def __init__(self,innerHTML:list=None,alignment:HStackAlignment=HStackAlignment.center,**attributes):
        super().__init__(innerHTML=None,**attributes)
        self.setInnerHTML(ForEach(innerHTML,lambda i:nodes.Div(i).setClass('p-2').setClass('gap-2')))
        self.setClass('d-flex').setClass('gap-2').setClass(alignment.value).setClass('justify-content-center')

class ButtonStyle(enum.Enum):
        primary='btn-primary'
        secondary='btn-secondary'
        danger='btn-danger'

class Button(nodes.Button):

    def __init__(self,innerHTML:str='',**attributes):
        super().__init__(innerHTML=None,**attributes)
        self.setInnerHTML(HTMLSet([String(innerHTML)]))
        self.setClass('btn').setClass(ButtonStyle.primary.value).setClass('transition-colors')
        
    def butStyle(self,style:ButtonStyle=ButtonStyle.primary):
         self.setClass(style.value)
         return self

class FontSize:
     def __init__(self,size:float):
          self.value=f'{size}px'

def getSize(size:float):
     return FontSize(size)

class TextFontStyle(enum.Enum):
        default=''
        h1='h1'
        h2='h2'
        h3='h3'
        # caption='text-muted'
        bold='fw-bold'
        italic='fst-italic'
        size=getSize

class RGBAColor:
    def __init__(self,red:int,green:int,blue:int,alpha):
        self.red = max(0, min(255, red))
        self.green = max(0, min(255, green))
        self.blue = max(0, min(255, blue))
        self.alpha = max(0.0, min(1.0, alpha))
        self.value=f"rgba({self.red},{self.green},{self.blue},{self.alpha})"

def getRGBAColor(red:int,green:int,blue:int,alpha:int=1):
     return RGBAColor(red=red,green=green,blue=blue,alpha=alpha)

class HTMLColor(enum.Enum):
        red='red'
        blue='blue'
        rgba=getRGBAColor

class Text(nodes.P):

    def __init__(self,innerHTML:str='',**attributes):
        super().__init__(innerHTML=None,**attributes)
        self.setInnerHTML(HTMLSet([String(innerHTML)]))
        self.setClass('mb-2')

    def fontStyle(self,style:TextFontStyle=TextFontStyle.default):
        if isinstance(style,FontSize):
            self.setStyle("font-size",style.value)
        else:
            self.setClass(style.value)
        return self
    
    def fontColor(self,color:HTMLColor):
         self.setStyle('color',color.value)
         return self



    
class Page(nodes.Html):
    def __init__(self,body:list,head:list=None,title="",charset='utf-8',bootstrapCss=None,bootstrapDarkCss=None,bootstrapScript=None):
        super().__init__(HTMLSet([
            nodes.Head(HTMLSet([
                HTMLSet(head) if head else HTMLSet(),
                nodes.Meta(charset=charset),
                nodes.Title(title),
                
                # nodes.Style("\n".join([style for style in body.specificStyle])),
                nodes.Link(href=bootstrapCss if bootstrapCss else 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',rel='stylesheet'),
                nodes.Link(href=bootstrapDarkCss if bootstrapDarkCss else 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap-dark.min.css',rel='stylesheet'),
                nodes.Style(src=bootstrapScript if bootstrapScript else 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js')
            ])),
            nodes.Body(HTMLSet(body))
        ]))
    
