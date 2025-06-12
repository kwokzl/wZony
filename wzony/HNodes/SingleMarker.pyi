
from ..core import *

class Img(SingleMarker):
    def __init__(self,src:str,alt:str,width:str,height:str,id:str,class_:str,style:str):...


class Meta(SingleMarker):
    def __init__(self,name:str,content:str,charset:str,http_equiv:str):...


class Br(SingleMarker):
    def __init__(self,id:str,class_:str,style:str):...


class Hr(SingleMarker):
    def __init__(self,id:str,class_:str,style:str,size:str,width:str,align:str):...


class Input(SingleMarker):
    def __init__(self,type:str,name:str,value:str,placeholder:str,id:str,class_:str,style:str,disabled:bool,readonly:bool):...


class Link(SingleMarker):
    def __init__(self,href:str,rel:str,type:str,sizes:str,media:str,id:str,class_:str,style:str):...


class Base(SingleMarker):
    def __init__(self,href:str,target:str):...


class Area(SingleMarker):
    def __init__(self,shape:str,coords:str,href:str,alt:str,target:str):...


class Col(SingleMarker):
    def __init__(self,span:str,width:str,id:str,class_:str,style:str):...


class Param(SingleMarker):
    def __init__(self,name:str,value:str):...

