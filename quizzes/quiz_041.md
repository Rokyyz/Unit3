# Quiz041



# 1. UML Diagram

![CommSci 27](https://github.com/Rokyyz/Unit3/assets/134658259/7ee8b06b-fb69-4528-9564-13b1089ba1a3)


# 2. solutions


```.py
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton

class MyButton(MDFlatButton):
    pass
class quiz_041(MDApp):
    def build(self):
        Window.size = (500, 500)
        pass
    def button_pressed(self, btn):
        btn.md_bg_color = "white"
        if self.root.ids.player_turn.text == "X player's turn":
            btn.text = "X"
            self.root.ids.player_turn.text = "Y player's turn"
        else:
            self.root.ids.player_turn.text = "X player's turn"
            btn.text = "O"
            btn.md_bg_color = "purple"


test = quiz_041()
test.run()

```

```.kv
Screen:
    size: 500, 500
    MDBoxLayout:
        size_hint: 0.8, 0.8
        pos_hint: {"center_x":0.5, "center_y":0.5}
        md_bg_color:"black"
        orientation: "vertical"


        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, 0.25
            md_bg_color:"white"


            MDLabel:
                id: player_turn
                text: "X player's turn"
                font_size: "30pt"
                halign: "center"

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, 0.25
            md_bg_color:"yellow"
            MyButton:
            MyButton:
            MyButton:

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, 0.25
            md_bg_color:"white"
            MyButton:
            MyButton:
            MyButton:

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, 0.25
            md_bg_color:"yellow"
            MyButton:
            MyButton:
            MyButton:

<MyButton>:
    size_hint: 1, 1
    color: "white"
    md_bg_color:"grey"
    font_size: "35pt"
    on_press:
        app.button_pressed(self)
```


# 3. proof of work

https://youtube.com/shorts/h-fr2mKFUd8?feature=share
