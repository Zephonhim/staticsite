class HTMLNode:
    def __init__(self,tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementdedError()
    def props_to_html(self):
        if self.props is None:
            return ""
        return f" tag={self.tag} value={self.value} children={self.children} props={self.props}"
    def __repr__(self):
        return print(f"{self.tag}")