class Widget:
    
    def __init__(self, label, value=None):
        self.label = label
        self.value = value

    def set_value(self, value): 
        self.value = value

    def __repr__(self):
        return f"{self.label}, {self.value}"

class TextField(Widget):
    def __init__(self, label, value=None):
        super().__init__(label, value)
        self.label = label
        self.value = value

    def set_value(self, value):
        super().set_value(value)

class Button(Widget):
    def __init__(self, label):
        super().__init__(label, None)

    def on_click(self, cb):
        if not callable(cb):
            raise TypeError("provide function as callback")
        cb()


if __name__ == "__main__":
    field = TextField("name")
    field.set_value("ujwal")

    button = Button("submit")
    button.on_click(lambda : print("hello from fucntion"))
    print(field, button)
