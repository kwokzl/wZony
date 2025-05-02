from ..core import *

class Img(SingleMarker):
    def __init__(self, src:str="", alt:str="", width:str="", height:str="", id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", **attribute)
        self.setAttribute("src", src) if src else self
        self.setAttribute("alt", alt) if alt else self
        self.setAttribute("width", width) if width else self
        self.setAttribute("height", height) if height else self
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Meta(SingleMarker):
    def __init__(self, name:str="", content:str="", charset:str="", http_equiv:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", **attribute)
        self.setAttribute("name", name) if name else self
        self.setAttribute("content", content) if content else self
        self.setAttribute("charset", charset) if charset else self
        self.setAttribute("http-equiv", http_equiv) if http_equiv else self

class Br(SingleMarker):
    def __init__(self, id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Hr(SingleMarker):
    def __init__(self, id:str="", class_:str="", style:str="", size:str="", width:str="", align:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", **attribute)
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self
        self.setAttribute("size", size) if size else self
        self.setAttribute("width", width) if width else self
        self.setAttribute("align", align) if align else self

class Input(SingleMarker):
    def __init__(self, type:str="text", name:str="", value:str="", placeholder:str="", id:str="", class_:str="", style:str="", disabled:bool=False, readonly:bool=False, **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", **attribute)
        self.setAttribute("type", type)
        self.setAttribute("name", name) if name else self
        self.setAttribute("value", value) if value else self
        self.setAttribute("placeholder", placeholder) if placeholder else self
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self
        if disabled:
            self.setAttribute("disabled", "disabled")
        if readonly:
            self.setAttribute("readonly", "readonly")

class Link(SingleMarker):
    def __init__(self, href:str="", rel:str="", type:str="", sizes:str="", media:str="", id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", **attribute)
        self.setAttribute("href", href) if href else self
        self.setAttribute("rel", rel) if rel else self
        self.setAttribute("type", type) if type else self
        self.setAttribute("sizes", sizes) if sizes else self
        self.setAttribute("media", media) if media else self
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Base(SingleMarker):
    def __init__(self, href:str="", target:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", **attribute)
        self.setAttribute("href", href) if href else self
        self.setAttribute("target", target) if target else self

class Area(SingleMarker):
    def __init__(self, shape:str="", coords:str="", href:str="", alt:str="", target:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", **attribute)
        self.setAttribute("shape", shape) if shape else self
        self.setAttribute("coords", coords) if coords else self
        self.setAttribute("href", href) if href else self
        self.setAttribute("alt", alt) if alt else self
        self.setAttribute("target", target) if target else self

class Col(SingleMarker):
    def __init__(self, span:str="", width:str="", id:str="", class_:str="", style:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", **attribute)
        self.setAttribute("span", span) if span else self
        self.setAttribute("width", width) if width else self
        self.setAttribute("id", id) if id else self
        self.setAttribute("class", class_) if class_ else self
        self.setAttribute("style", style) if style else self

class Param(SingleMarker):
    def __init__(self, name:str="", value:str="", **attribute):
        super().__init__(f"{self.__class__.__name__.lower()}", **attribute)
        self.setAttribute("name", name) if name else self
        self.setAttribute("value", value) if value else self