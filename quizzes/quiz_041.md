# Quiz041



# 1. UML Diagram

![CommSci 23](https://github.com/Rokyyz/Unit3/assets/134658259/304e4428-3406-410e-aaa9-0e66b2c9ae76)



# 2. solutions


```.py
from kivymd.app import MDApp
class quiz_040(MDApp):
    def build(self):

        return

    def button_pressed(self):
        if self.root.ids.my_btn.text == 'Light mode':
            self.root.ids.my_btn.text = 'Dark mode'
            self.root.ids.my_btn.md_bg_color = [1, 1, 1, 1]  # White background
            self.root.ids.my_btn.text_color = [0, 0, 0, 1]  # Black text color
            self.root.ids.my_label.md_bg_color = [1, 1, 1, 1]  # White background
            self.root.ids.my_label.color = [0, 0, 0, 1]  # Black text color
        else:
            self.root.ids.my_btn.text = 'Light mode'
            self.root.ids.my_btn.md_bg_color = [0, 0, 0, 1]  # Black background
            self.root.ids.my_btn.text_color = [1, 1, 1, 1]  # White text color
            self.root.ids.my_label.md_bg_color = [0, 0, 0, 1]  # Black background
            self.root.ids.my_label.color = [1, 1, 1, 1]  # White text color


text = quiz_040()
text.run()
```

```.kv
Screen:
    size: 500, 500

    MDLabel:
        id:my_label
        text: 'Roky'
        font_size: "50pt"
        halign: "center"
        color: 'black'


    MDRaisedButton:
        id: my_btn
        pos: 0,0
        text: 'Dark mode'
        md_bg_color: "black"
        on_press:
            app.button_pressed()
```


# 3. proof of work
