# from abc import ABC, abstractmethod
# import re



class HTMLNode:#定义HTML节点
    def __init__(self):
        pass
    @property
    def toHTMLString(self):
        pass
    
    


class  HTMLElement(HTMLNode):
    def __init__(self, tag, **attribute):
        super().__init__()
        self.tag=tag
        self.attributes=attribute
        
    def setAttribute(self,key:str,value:str=""):
        self.attributes[key.lower()]=value
        return self
    
    def setBoolAttributes(self,value:str):
        self.setAttribute(value,value)
        return self

    def setClass(self,value:str):
        self.attributes["class"]=self.attributes["class"] if ("class" in self.attributes) else ""
        classList=self.attributes["class"].split()
        classList.append(value)
        self.setAttribute("class"," ".join(classList))
        return self
    
    def setStyle(self,key:str,value:str):
        self.attributes["style"]=self.attributes["style"] if ("style" in self.attributes) else ""
        classList=self.attributes["style"].split(r"[^;]+")
        classList.append(f"{key}:{value}")
        classList=[item for item in classList if item !=""]
        self.setAttribute("style",";".join(classList))
        return self
    
    
    def class_(self,value:str):
        self.attributes["class"]=value
        return self

    def id(self,value:str):
        self.attributes["id"]=value
        return self
    
    def style(self,value:str):
        self.attributes["style"]=value
        return self
    

    def __str__(self):
        return self.toHTMLString()
        
    def debug(self):
        return self.Debugger(self)
    
    def __getattr__(self,name:str):
        def set(value:str):
            self.setStyle(name.replace("_","-"),value)
            return self
        return set


    class Debugger():
        def __init__(self,element):
            self.element=element
        
        def getAttribute(self,key:str):
            if key.lower() in self.element.attributes:
                print(self.element.attributes[key.lower()])
            else:
                print(None)
            # return self.element

        def getClass(self):
            self.getAttribute("class")

        def getId(self):
            self.getAttribute("id")

        def __getattr__(self,name:str):
            self.getAttribute(name)
            return self.element
        
# class Nodes:
#     def __init__(self,*node:HTMLNode):
#         self.nodes:list=node
        
#     def __lshift__(self,node:HTMLNode):
#         self.nodes.append(node)
#         return self.nodes

class HTMLSet(list):#HTML标签节点集
    '''用于存放HTML节点'''
    def __init__(self,nodes:list[HTMLNode]=None):
        if nodes!=None:self.extend(nodes)
        pass
    def __lshift__(self,node):# <<运算符
        # if isinstance(node, ForEach):
        #     for item in node.items():
        #         self.nodes.add(item)
            
        # else:
        self.append(node)
        return self
    
    def toHTMLString(self):
        string=""
        if len(self) > 0:
            for node in self:
                string+=node.toHTMLString()
            return string
        else:
            return ""
    def __str__(self):
        return self.toHTMLString()
    # def __str__(self):
    #     pass


    



class SingleMarker(HTMLElement):#定义HTML单标记节点
    '''
    定义HTML单标记元素
    '''
    def __init__(self,tag:str,**attribute:dict):
        super().__init__(tag,**attribute)
    def toHTMLString(self):
        attributes=[f"{key}=\"{value}\"" for key,value in self.attributes.items()]
        return f"<{self.tag}{" "+" ".join(attributes) if len(attributes)>0 else ""}/>"
    
    def __str__(self):
        return self.toHTMLString()
    
class DoubleMarker(HTMLElement):#定义HTML双标记节点
    '''
    定义HTML双标记元素
    '''
    def __init__(self,tag:str,innerHTML:HTMLSet=None,**attribute:dict):
        super().__init__(tag,**attribute)
        self.HTMLSet = innerHTML if innerHTML!=None else HTMLSet()

    def __lshift__(self,node):# <<运算符
        self.HTMLSet.append(node)
        return self
    def toHTMLString(self):
        attributes=[f"{key}=\"{value}\"" for key,value in self.attributes.items()]
       
        
        return f"<{self.tag}{" "+" ".join(attributes) if len(attributes)>0 else ""}>{self.HTMLSet.toHTMLString() if len(self.HTMLSet)!=0 else ""}</{self.tag}>"
        
    def innerHTML(self,innerHTML:HTMLSet):
        for item in innerHTML:
            self.HTMLSet.append(item)
        
        return self
    
    def __str__(self):
        return self.toHTMLString()
    
    

class String(HTMLNode,str):
    '''
    定义HTML字符节点
    '''
    def __init__(self,string):
        super().__init__()
        self=string
        
    def toHTMLString(self):
        return self
    
    def __str__(self):
        return self
    
    def wrapped(self,by:DoubleMarker):
        by.innerHTML(HTMLSet()<<self)
        return String(by.toHTMLString())
        
        

# class ForEach:
#     '''
#     根据range批量生成HTML节点
#     '''
#     def __init__(self, data, HTMLNode):
#         self.data = data
#         self.HTMLNode = HTMLNode
    
   
#     def items(self):
#         return [self.HTMLNode(item) for item in self.data]
def ForEach(data,func)->HTMLSet:
    List=list()
    for item in data:
        List.append(func(item))
        # print(item)
    # print([value.value for value in Set])
    return HTMLSet(List)