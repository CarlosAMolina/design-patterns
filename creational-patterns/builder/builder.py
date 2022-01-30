class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    # We can call HtmlBuilder from HtmlElement to facilitate its usage.
    # This can be a violation of the Open Close principle but, as 
    # these clases have a tight relation and will always be defined
    # together, it's ok.
    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    # Class attribute _root will point to the same memory address, 
    # and clear() must be called each time we want to initialize
    # the text and elements values for different HTML root elements.
    #__root = HtmlElement()

    def __init__(self, root_name):
        self.root_name = root_name
        # To avoid call clean() at each HTML root element
        self._init_root_element()

    def _init_root_element(self):
        self.__root = HtmlElement(name=self.root_name)

    # not fluent
    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    # fluent
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def clear(self):
        self._init_root_element()

    def __str__(self):
        return str(self.__root)


# if you want to build a simple HTML paragraph using a list
print('HTML element <p> with a list:')
hello = 'hello'
parts = ['<p>', hello, '</p>']
print(''.join(parts))

# now I want an HTML list with 2 words in it
print('HTML element <ul> with a list:')
words = ['hello', 'world']
parts = ['<ul>']
for w in words:
    parts.append(f'  <li>{w}</li>')
parts.append('</ul>')
print('\n'.join(parts))

# HTML element with tag ul
# ordinary non-fluent builder
# builder = HtmlBuilder('ul') # creation option 1
builder_ul = HtmlElement.create('ul') # creation option 2
builder_ul.add_child('li', 'hello')
builder_ul.add_child('li', 'world')
print('HTML element <ul> with ordinary builder:')
print(builder_ul)

# Other HTML ul element with different values
# fluent builder
builder_ul.clear()
builder_ul.add_child_fluent('li', 'hello 2') \
    .add_child_fluent('li', 'world 2')
print('HTML element <ul> with fluent builder:')
print(builder_ul)

## HTML element with tag ol
print('HTML element <ul> with fluent builder:')
builder_ol = HtmlElement.create('ol')
builder_ol.add_child_fluent('li', 'hello ol').add_child_fluent('li', 'world ol')
print(builder_ol)