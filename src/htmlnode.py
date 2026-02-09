
class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if self.props is None or len(self.props) == 0:
            return result
        for key in self.props:
            result += f' {key}="{self.props[key]}"'
        return result
    
    def __repr__(self):
        return f"HTMLNODE(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None,props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return f"{value}"
        if self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"HTMLNODE(tag='{self.tag}', value='{self.value}', props={self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"