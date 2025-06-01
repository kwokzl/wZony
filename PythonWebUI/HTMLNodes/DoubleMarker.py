from ..core import *




class Html(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, lang:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("lang", lang) if lang else self

class Head(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, profile:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("profile", profile) if profile else self

class Body(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, bgcolor:str="", text:str="", link:str="", vlink:str="", alink:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("bgcolor", bgcolor) if bgcolor else self
        self.setAttribute("text", text) if text else self
        self.setAttribute("link", link) if link else self
        self.setAttribute("vlink", vlink) if vlink else self
        self.setAttribute("alink", alink) if alink else self


class Title(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)

class Script(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, src:str="", type:str="text/javascript", async_:bool=False, defer:bool=False, **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("src", src) if src else self
        self.setAttribute("type", type)
        if async_:
            self.setBoolAttributes("async")   
        if defer:
            self.setBoolAttributes("defer")   

class Style(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, type:str="text/css", media:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("type", type)
        self.setAttribute("media", media) if media else self

class Noscript(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)

class Template(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)

class Div(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class A(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, href:str="", target:str="", rel:str="", download:bool=False, **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("href", href) if href else self
        self.setAttribute("target", target) if target else self
        self.setAttribute("rel", rel) if rel else self
        if download:
            self.setBoolAttributes("download")   

class H1(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class H2(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class H3(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class H4(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class H5(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class H6(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class P(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Sup(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Sub(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class I(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class EM(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class B(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Strong(DoubleMarker):#粗体
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class U(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Span(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Table(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", border:str="", cellpadding:str="", cellspacing:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self
        self.setAttribute("border", border) if border else self
        self.setAttribute("cellpadding", cellpadding) if cellpadding else self
        self.setAttribute("cellspacing", cellspacing) if cellspacing else self

class Thead(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Tbody(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Tr(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Td(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", colspan:str="", rowspan:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self
        self.setAttribute("colspan", colspan) if colspan else self
        self.setAttribute("rowspan", rowspan) if rowspan else self

class Th(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", colspan:str="", rowspan:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self
        self.setAttribute("colspan", colspan) if colspan else self
        self.setAttribute("rowspan", rowspan) if rowspan else self

class Article(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Aside(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Footer(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Header(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Nav(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Section(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Button(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, type:str="button", id:str="", class_:str="", style:str="", disabled:bool=False, **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("type", type)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self
        if disabled:
            self.setBoolAttributes("disabled")   

class Form(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, action:str="", method:str="get", id:str="", class_:str="", style:str="", enctype:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("action", action)
        self.setAttribute("method", method)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self
        self.setAttribute("enctype", enctype) if enctype else self

class Label(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, for_:str="", id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("for", for_) if for_ else self
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Textarea(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, rows:str="", cols:str="", id:str="", class_:str="", style:str="", disabled:bool=False, **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("rows", rows) if rows else self
        self.setAttribute("cols", cols) if cols else self
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self
        if disabled:
            self.setBoolAttributes("disabled")   

class Ol(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", start:str="", type:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self
        self.setAttribute("start", start) if start else self
        self.setAttribute("type", type) if type else self

class Ul(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Li(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", value:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self
        self.setAttribute("value", value) if value else self

class Blockquote(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, cite:str="", id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("cite", cite) if cite else self
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Figure(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Figcaption(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Details(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, open:bool=False, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        if open:
            self.setBoolAttributes("open")   
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Summary(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Option(DoubleMarker):
    def __init__(self, innerText:str="", innerHTML:HTMLSet=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", innerHTML if innerHTML!=None else HTMLSet()<<String(innerText), **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Select(DoubleMarker):
    def __init__(self, options:list,dirt=None, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", ForEach(options,lambda option:Option(option)) if options!=None else HTMLSet()<<String(innerText), **attribute)
        if options:
            self.innerHTML=ForEach(options,lambda option:Option(option))
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self
