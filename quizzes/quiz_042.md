# Quiz042



# 1. UML Diagram

![CommSci 26](https://github.com/Rokyyz/Unit3/assets/134658259/a5fcd98f-d8ae-4904-a03b-4eca9ec9d0b9)



# 2. solutions


```.py
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class MysteryPageA(MDScreen):
    def message1(self):
        self.parent.current = "MysteryPageB"


class MysteryPageB(MDScreen):
    def message2(self):
        self.parent.current = "MysteryPageA"

class quiz_042(MDApp):
    def build(self):
        Window.size = (400,700)

    def changed(self):
        print("Page was changed")
test = quiz_042()
test.run()

```

```.kv
ScreenManager:
    MysteryPageA:
        name: "MysteryPageA"
    MysteryPageB:
        name: "MysteryPageB"

<MysteryPageA>
    MDLabel:
        text: "This is mystery page A, you pressed the button"
        font_size: "32pt"
    MDFloatingActionButton:
        icon: "pencil-outline"
        style: "standard"
        on_press:
            root.message1()

<MysteryPageB>:
    MDLabel:
        text: "This is mystery page B, you pressed the button"
        font_size: "32pt"
    MDFloatingActionButton:
        icon: "pencil-outline"
        style: "standard"
        on_press:
            root.parent.current = "MysteryPageA"
```


# 3. proof of work

https://youtube.com/shorts/5ebg_pOsb7Q?feature=share
