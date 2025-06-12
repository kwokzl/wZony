DoubleMarkers = {
    'Html': {'standard_attrs': ['lang'], 'bool_attrs': []},
    'Head': {'standard_attrs': ['profile'], 'bool_attrs': []},
    'Body': {'standard_attrs': ['bgcolor', 'text', 'link', 'vlink', 'alink'], 'bool_attrs': []},
    
    'Title': {'standard_attrs': [], 'bool_attrs': []},
    'Script': {'standard_attrs': ['src', 'type', 'charset'], 'bool_attrs': ['async_', 'defer']},
    'Style': {'standard_attrs': ['type', 'media'], 'bool_attrs': []},
    'Noscript': {'standard_attrs': [], 'bool_attrs': []},
    'Template': {'standard_attrs': [], 'bool_attrs': []},
    
    'Div': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'Span': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'P': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    
    'H1': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'H2': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'H3': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'H4': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'H5': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'H6': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    
    'A': {'standard_attrs': ['href', 'target', 'rel', 'download'], 'bool_attrs': []},
    'Strong': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'B': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'I': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'EM': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'U': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'Sup': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'Sub': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    
    'Table': {'standard_attrs': ['id', 'class_', 'style', 'border', 'cellpadding', 'cellspacing'], 'bool_attrs': []},
    'Thead': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'Tbody': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'Tr': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'Td': {'standard_attrs': ['id', 'class_', 'style', 'colspan', 'rowspan'], 'bool_attrs': []},
    'Th': {'standard_attrs': ['id', 'class_', 'style', 'colspan', 'rowspan'], 'bool_attrs': []},
    
    'form': {'standard_attrs': ['action', 'method', 'id', 'class_', 'style', 'enctype'], 'bool_attrs': []},
    'Input': {'standard_attrs': ['type', 'name', 'value', 'placeholder', 'id', 'class_', 'style'], 'bool_attrs': ['disabled', 'readonly', 'required']},
    'Button': {'standard_attrs': ['type', 'id', 'class_', 'style'], 'bool_attrs': ['disabled']},
    'Label': {'standard_attrs': ['for_', 'id', 'class_', 'style'], 'bool_attrs': []},
    'Textarea': {'standard_attrs': ['rows', 'cols', 'id', 'class_', 'style'], 'bool_attrs': ['disabled']},
    
    'Ul': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'Ol': {'standard_attrs': ['id', 'class_', 'style', 'start', 'type'], 'bool_attrs': []},
    'Li': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    
    'Article': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'Aside': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'Footer': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'Header': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'Nav': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'Section': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
}

SingleMarkers = {
    'Img': {'standard_attrs': ['src', 'alt', 'width', 'height', 'id', 'class_', 'style'], 'bool_attrs': []},
    'Meta': {'standard_attrs': ['name', 'content', 'charset', 'http_equiv'], 'bool_attrs': []},
    'Br': {'standard_attrs': ['id', 'class_', 'style'], 'bool_attrs': []},
    'Hr': {'standard_attrs': ['id', 'class_', 'style', 'size', 'width', 'align'], 'bool_attrs': []},
    'Input': {'standard_attrs': ['type', 'name', 'value', 'placeholder', 'id', 'class_', 'style'], 'bool_attrs': ['disabled', 'readonly']},
    'Link': {'standard_attrs': ['href', 'rel', 'type', 'sizes', 'media', 'id', 'class_', 'style'], 'bool_attrs': []},
    'Base': {'standard_attrs': ['href', 'target'], 'bool_attrs': []},
    'Area': {'standard_attrs': ['shape', 'coords', 'href', 'alt', 'target'], 'bool_attrs': []},
    'Col': {'standard_attrs': ['span', 'width', 'id', 'class_', 'style'], 'bool_attrs': []},
    'Param': {'standard_attrs': ['name', 'value'], 'bool_attrs': []}
}

# DoubleMarkers
allMarkers=DoubleMarkers

allTags=[str(i) for i in DoubleMarkers.keys()]

code="""
from ..core import *
"""

for tag in allTags:
    attrs=",".join([str(i)+':str' for i in allMarkers[tag]['standard_attrs']]+[str(i)+':bool' for i in allMarkers[tag]['bool_attrs']])
    code+=f"""
class {tag}(DoubleMarker):
    def __init__(self,{attrs}):...

"""
with open('wzony/HNodes/DoubleMarker.pyi','w') as pyi:
    pyi.write(str(code))


# SingleMarkers
allMarkers=SingleMarkers

allTags=[str(i) for i in SingleMarkers.keys()]

code="""
from ..core import *
"""

for tag in allTags:
    attrs=",".join([str(i)+':str' for i in allMarkers[tag]['standard_attrs']]+[str(i)+':bool' for i in allMarkers[tag]['bool_attrs']])
    code+=f"""
class {tag}(SingleMarker):
    def __init__(self,{attrs}):...

"""
with open('wzony/HNodes/SingleMarker.pyi','w') as pyi:
    pyi.write(str(code))
# print(code)