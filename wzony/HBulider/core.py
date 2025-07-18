from ..core import *
from .. import HNodes as nodes
import os
 
current_path = os.path.abspath(__file__)
package_dir = os.path.dirname(current_path)
# coreCss_path = os.path.join(package_dir+'/static', 'core.css')

class VStack(nodes.Div):
    def __init__(self,innerHTML:list=None,**attributes):
        super().__init__(innerHTML=None,**attributes)
        self.innerHTML(ForEach(innerHTML,lambda i:i))
        self.setClass('d-flex').setClass('flex-column').setClass('gap-3')

class HStack(nodes.Div):
    def __init__(self,innerHTML:list=None,**attributes):
        super().__init__(innerHTML=None,**attributes)
        self.innerHTML(ForEach(innerHTML,lambda i:i))
        self.setClass('d-flex').setClass('flex-row').setClass('gap-3')
        
    
class Page(nodes.Html):
    def __init__(self,body:list,head:list=None,title="",charset='utf-8',bootstrapCss=None,bootstrapScript=None):
        super().__init__(HTMLSet([
            nodes.Head(HTMLSet([
                HTMLSet(head) if head else HTMLSet(),
                nodes.Meta(charset=charset),
                nodes.Title(title),
                
                # nodes.Style("\n".join([style for style in body.specificStyle])),
                nodes.Link(href=bootstrapCss if bootstrapCss else 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css',rel='stylesheet'),
                nodes.Style(src=bootstrapScript if bootstrapScript else 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js')
            ])),
            nodes.Body(HTMLSet(body))
        ]))
    
