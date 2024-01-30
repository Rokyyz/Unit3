# Quiz039



# 1. UML Diagram

![CommSci 22](https://github.com/Rokyyz/Unit3/assets/134658259/b57cddf2-81bf-4a6a-98f7-d150fb78465a)


# 2. solutions


```.py
from kivymd.app import MDApp

class quiz_039(MDApp):
    def build(self):
        self.num = 0
        return

    def button_pressed(self):
        label = self.root.ids.my_label
        self.num += 1
        label.text = f"Count {self.num}"
        label.color = "red"
        label.md_bg_color = "#ADD8E6"
        btn = self.root.ids.my_btn
        btn.md_bg_color = "blue"


text = quiz_039()
text.run()
```

```.kv
Screen:
    size: 500, 500


    MDBoxLayout:
        orientation: "horizontal"
        pos_hint: {"center_x":.5, "center_y":.5}
        size_hint: .7, .3

        MDLabel:
            id:my_label
            text: 0
            color: "red"
            md_bg_color: "#ADD8E6"
            text: "Count: 0"
            size_hint: .5, 1
            font_size: "34pt"
            halign: "center"

        MDRaisedButton:
            id: my_btn
            text: "Add +1"
            size_hint: 0.5, 1
            font_size: "34pt"
            color: "white"
            md_bg_color: "black"
            on_press:
                app.button_pressed()

```


# 3. proof of work

https://youtu.be/DVAV-D4TB6U
