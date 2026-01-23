from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError("Children missing")
        
        for child in self.children:
            if self.props is None:
                return f'<{self.tag}>{child.to_html()}</{self.tag}>'
            return f'<{self.tag}{self.props_to_html()}>{child.to_html()}</{self.tag}>'
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return f"{value}"
        if self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"HTMLNODE(tag='{self.tag}', value='{self.value}', props={self.props})"