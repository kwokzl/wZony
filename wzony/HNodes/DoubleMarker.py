from ..core import *


class HTMLDoubleTagFactory:
    @staticmethod
    def create_tag_class(tag_name, standard_attrs=None, bool_attrs=None):
        class DynamicHTMLTag(DoubleMarker):
            def __init__(self, innerText="", innerHTML=None, **attrs):
                super().__init__(
                    tag_name.lower(),
                    innerHTML if innerHTML is not None else HTMLSet() << String(innerText),
                    **attrs
                )
                
                if standard_attrs:
                    for attr in standard_attrs:
                        if attr in attrs:
                            self.setAttribute(attr, attrs[attr])
                
                if bool_attrs:
                    for attr in bool_attrs:
                        if attrs.get(attr, False):
                            self.setBoolAttributes(attr)
        
        return DynamicHTMLTag

    @staticmethod
    def __create_custom_tag_help__(tag_name, standard_attrs=None, bool_attrs=None):
        """Create and register a custom HTML tag dynamically.
        
        :param tag_name: (str) Name of the custom tag
        :param standard_attrs: (list) List of standard attributes
        :param bool_attrs: (list) List of boolean attributes
        
        :return: The created custom tag class
        :raises ValueError: If tag_name is not a string or is empty, or if the tag already exists

        Example:

            MyTag = HTMLDoubleTagFactory.create_custom_tag(
                'MyTag',
                standard_attrs=['data-id'],
                bool_attrs=['active']
            )
            tag = MyTag('Content', data_id='123', active=True)
        """
        if not isinstance(tag_name, str) or not tag_name:
            raise ValueError("Tag name must be a non-empty string")
            
        if tag_name in globals():
            raise ValueError(f"Tag '{tag_name}' already exists")
            
        tag_class = HTMLDoubleTagFactory.create_tag_class(
            tag_name,
            standard_attrs or [],
            bool_attrs or []
        )
        
        globals()[tag_name] = tag_class
        return tag_class

__TAG_CONFIGS = {
    'Html': {'standard_attrs': ['lang'], 'bool_attrs': []},
    'Head': {'standard_attrs': ['profile'], 'bool_attrs': []},
    'Body': {'standard_attrs': ['bgcolor', 'text', 'link', 'vlink', 'alink'], 'bool_attrs': []},
    
    'Title': {'standard_attrs': [], 'bool_attrs': []},
    'Script': {'standard_attrs': ['src', 'type', 'charset'], 'bool_attrs': ['async_', 'defer']},
    'Style': {'standard_attrs': ['type', 'media'], 'bool_attrs': []},
    'Noscript': {'standard_attrs': [], 'bool_attrs': []},
    'Template': {'standard_attrs': [], 'bool_attrs': []},
    
    'Div': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'Span': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'P': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    
    'H1': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'H2': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'H3': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'H4': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'H5': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'H6': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    
    'A': {'standard_attrs': ['href', 'target', 'rel', 'download'], 'bool_attrs': []},
    'Strong': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'B': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'I': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'EM': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'U': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'Sup': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'Sub': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    
    'Table': {'standard_attrs': ['id', 'class', 'style', 'border', 'cellpadding', 'cellspacing'], 'bool_attrs': []},
    'Thead': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'Tbody': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'Tr': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'Td': {'standard_attrs': ['id', 'class', 'style', 'colspan', 'rowspan'], 'bool_attrs': []},
    'Th': {'standard_attrs': ['id', 'class', 'style', 'colspan', 'rowspan'], 'bool_attrs': []},
    
    'Form': {'standard_attrs': ['action', 'method', 'id', 'class', 'style', 'enctype'], 'bool_attrs': []},
    'Input': {'standard_attrs': ['type', 'name', 'value', 'placeholder', 'id', 'class', 'style'], 'bool_attrs': ['disabled', 'readonly', 'required']},
    'Button': {'standard_attrs': ['type', 'id', 'class', 'style'], 'bool_attrs': ['disabled']},
    'Label': {'standard_attrs': ['for', 'id', 'class', 'style'], 'bool_attrs': []},
    'Textarea': {'standard_attrs': ['rows', 'cols', 'id', 'class', 'style'], 'bool_attrs': ['disabled']},
    
    'Ul': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'Ol': {'standard_attrs': ['id', 'class', 'style', 'start', 'type'], 'bool_attrs': []},
    'Li': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    
    'Article': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'Aside': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'Footer': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'Header': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'Nav': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
    'Section': {'standard_attrs': ['id', 'class', 'style'], 'bool_attrs': []},
}

for tag_name, config in __TAG_CONFIGS.items():
    globals()[tag_name] = HTMLDoubleTagFactory.create_tag_class(
        tag_name,
        config['standard_attrs'],
        config['bool_attrs']
    )


def customDoubleTag(tag_name, standard_attrs=None, bool_attrs=None):
    """Create and register a custom HTML tag dynamically.
        
        :param tag_name: (str) Name of the custom tag
        :param standard_attrs: (list) List of standard attributes
        :param bool_attrs: (list) List of boolean attributes
        
        :return: The created custom tag class
        :raises ValueError: If tag_name is not a string or is empty, or if the tag already exists

        Example:

            MyTag = customDoubleTag(
                'MyTag',
                standard_attrs=['data-id'],
                bool_attrs=['active']
            )
            tag = MyTag('Content', data_id='123', active=True)
    """
    return HTMLDoubleTagFactory.__create_custom_tag_help__(
        tag_name,
        standard_attrs or [],
        bool_attrs or []
    )
