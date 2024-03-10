import sqlite3
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.pickers import MDTimePicker, MDDatePicker
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from mon_8_jan.my_lib import DatabaseWorker, make_hash, check_hash

class LoginApp(MDApp):
    db = DatabaseWorker('FactoryManager.db')
    current_user = []
    money = 0
    materials = {"carbon_fiber": 10, "graphite": 5, "wolfram": 10, "aluminum": 10, "titanium": 5, "nanocarbon": 25}
    def build(self):
        # x = LoginApp(transition=NoTransition())
        self.theme_cls.theme_style = 'Dark'
        Window.size = (1250, 1000)
        return

class MenuScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def go_to_inventory(self):
        self.manager.current = "InventoryScreen"

    def go_to_orders(self):
        self.manager.current = "OrdersScreen"

    def go_to_transactions(self):
        self.manager.current = "TransactionsScreen"

    def go_to_workers(self):
        self.manager.current = "WorkersScreen"

    def go_to_login(self):
        self.manager.current = "LoginScreen"

    def go_to_orders_for_workers(self):
        self.manager.current = "OrdersForWorkersScreen"

    def go_to_add_orders(self):
        self.manager.current = "AddOrdersScreen"

    def go_to_see_orders(self):
        self.manager.current = "SeeOrdersScreen"

    def try_logout(self):
        # Create an MDDialog to confirm whether the user wants to sign out or not
        self.sign_out_confirmation_dialog = MDDialog(
            title="Logout",
            text="Are you sure you want to logout?",
            buttons=[
                MDFlatButton(
                    text="Yes",
                    on_release=self.log_out_user
                ),
                MDFlatButton(
                    text="No",
                    on_release=self.dismiss_dialog
                ),
            ],
        )
        self.sign_out_confirmation_dialog.open()

    def log_out_user(self, instance):
        # Perform the signout actions
        print("User logging out")
        self.parent.current = "LoginScreen"
        login_screen = self.parent.get_screen('LoginScreen')
        login_screen.ids.uname.text = ""
        login_screen.ids.passwd.text = ""
        login_screen.ids.c_log_passwd.text = ""
        self.sign_out_confirmation_dialog.dismiss()


    def dismiss_dialog(self, instance):
        self.sign_out_confirmation_dialog.dismiss()
    pass


class PurchaseDialog(MDBoxLayout):
    cost = 0
    amount = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.material_cost = \
            LoginApp.db.search(query=f"select cost from Inventory where name='{InventoryScreen.current_material}'")[0]

    def update_amount_text(self):
        self.ids.total_cost.text = f"Total cost: ${int(self.ids.amount.text) * self.material_cost}"  # * LoginApp.materials[InventoryManager.current_material]
        PurchaseDialog.cost = int(self.ids.amount.text) * self.material_cost
        PurchaseDialog.amount = int(self.ids.amount.text)



class InventoryScreen(MDScreen):
    current_material = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None

    def purchase_popup(self, material):
        InventoryScreen.current_material = material
        print(self)
        self.dialog = MDDialog(
            title=f"Purchase {material}?",
            text=f"Cost per unit: ${LoginApp.materials[material]}\nCurrently have: ${LoginApp.money}",
            type="custom",
            content_cls=PurchaseDialog(),
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    on_press=lambda x: self.dialog.dismiss()
                ),
                MDFlatButton(
                    text="Purchase",
                    on_press=lambda x: self.purchase()  # purchase function comes here
                )
            ]
        )
        self.dialog.open()

    def show_popup(self, messages, text):
        # Create a layout for the popup content
        content = BoxLayout(orientation='vertical')

        # Add a label to display the error messages
        error_label = Label(text='\n'.join(messages))
        content.add_widget(error_label)

        # Add a button to dismiss the popup
        dismiss_button = Button(text=text)
        content.add_widget(dismiss_button)

        # Create the popup window
        popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))

        # Bind the button's on_press event to dismiss the popup
        dismiss_button.bind(on_press=popup.dismiss)

        # Open the popup window
        popup.open()

    def purchase(self):
        # Purchase (take away money and add materials)
        print("test")
        errors = []
        current_total = LoginApp.db.search(query="SELECT total FROM Transactions WHERE id=(SELECT max(id) FROM Transactions)")[0]
        print(current_total)
        if current_total < PurchaseDialog.cost:  # if not sufficient money
            errors.append("Not enough money!")
        else:
            query = f"""insert into Transactions (buy, sell, amount, total)
                        values (1, 0, {PurchaseDialog.cost}, {current_total - PurchaseDialog.cost})"""
            LoginApp.db.run_query(query=query)
            query = f"""update Inventory set amount=((select amount from Inventory where Inventory.name='{InventoryScreen.current_material}')+{PurchaseDialog.amount})
                        where name='{InventoryScreen.current_material}'"""
            LoginApp.db.run_query(query=query)
            errors.append("Purchase successful!")
        self.dialog.dismiss()
        self.show_popup(messages=errors, text="OK")



class SeeOrdersScreen(MDScreen):

    data_table = None

    # Gets all data from orders table from the database
    def update(self):
        db = DatabaseWorker("FactoryManager.db")
        query = "SELECT * FROM Orders"
        data = db.search(query, True)
        db.close()
        self.data_table.update_row_data(None, data)

    def delete(self):
        # Function to delete checked rows in the table
        checked_rows = self.data_table.get_row_checks()  # Get the checked rows
        print(checked_rows)
        # delete
        db = DatabaseWorker("FactoryManager.db")
        for r in checked_rows:
            id = r[0]  # use item_id instead of id
            print(id)
            query = f"delete from Orders where order_id = {id}"  # use item_id instead of id
            print(query)
            db.run_query(query)
            # Create and open the alert dialog to confirm item has been deleted
            dialog = MDDialog(title="Order deleted!",
                              text=f"Order {id} has successfully been deleted.")
            dialog.open()
        db.close()
        self.update()

    # Displays the table on the screen
    def on_pre_enter(self, *args):
        self.data_table = MDDataTable(
            size_hint=(.7, .6),
            pos_hint={"center_x": .5, "center_y": .5},
            use_pagination=True,
            check=True,
            column_data=[("order_id", 80), ("customer_name", 50), ("order_date", 60),
                         ("order_time", 45), ("racket_type", 70)]
        )
        self.data_table.bind(on_row_press=self.row_pressed)
        self.data_table.bind(on_check_press=self.check_pressed)
        self.add_widget(self.data_table)
        self.update()

    # When a row is pressed
    def row_pressed(self, table, row):
        print("Row pressed", row.text)
        # row.md_bg_color = "#FFF0000"

    # When a row is checked
    def check_pressed(self, table, current_row):
        print("Check pressed", current_row)

class AddOrdersScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_date = None
        self.selected_racket_type = None

    def show_time_picker(self):
        from datetime import datetime

        # Define default time
        default_time = datetime.strptime("12:00", '%H:%M').time()

        time_dialog = MDTimePicker(
            primary_color="#8dbcd6",
            accent_color="#f4f4f4",
            text_button_color="#f4f4f4",
        )
        # Set default Time
        time_dialog.set_time(default_time)
        time_dialog.bind(on_cancel=self.on_cancel, time=self.get_time, on_save=self.on_save_time)
        time_dialog.open()

    def on_save_time(self, instance, value):
        self.selected_time = value
        value = value.strftime("%H:%M")
        self.ids.order_time.text = f"{value}"

    def date(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        self.selected_date = value
        value = value.strftime("%m/%d/%Y")
        self.ids.date.text = f"{value}"

    def get_time(self, instance, time):
        self.ids.order_time.text = time.strftime("%H:%M")

    def on_cancel(self, instance, time):
        instance.dismiss()

    def select_racket_type(self, instance, value):
        self.selected_racket_type = value

    def checkbox_click(self, checkbox, value, racket):
        if value:  # if the check is true
            self.selected_racket = racket
            print(racket)
            self.ids.racket.text = f"{racket}"

    def checkbox_racket_type(self, checkbox, value, racket_type):
        if value:  # if the check is true
            self.selected_racket = racket_type
            print(racket_type)
            self.ids.racket_type.text = f"{racket_type}"

    def checkbox_click_status(self, checkbox, value, status):
        if value:  # if the check is true
            self.selected_racket = status
            print(status)
            self.ids.status.text = f"{status}"

    def add_order(self):
        checker = True
        customer_name = self.ids.customer_name.text
        order_date = self.ids.date.text
        order_time = self.ids.order_time.text
        racket_type = self.selected_racket_type

        # Customer name validation
        if customer_name == "":
            self.ids.customer_name.error = True
            checker = False

        if checker:
            db = DatabaseWorker("FactoryManager.db")
            query = f"INSERT into Orders(customer_name, order_date, order_time, racket_type) values('{customer_name}', '{order_date}', '{order_time}', '{racket_type}')"
            db.run_query(query)
            db.close()

            # Pop up message
            dialog = MDDialog(title="Order added",
                              text=f"Order for {customer_name} has been successfully added.")
            dialog.open()

            # Reset fields
            self.ids.customer_name.text = ""
            self.ids.date.text = ""
            self.ids.order_time.text = ""
            self.selected_racket_type = None

    def cancel(self):
        self.parent.current = "MenuScreen"

class TransactionsScreen(MDScreen):
    data_table = None

    # Gets all data from orders table from the database
    def update(self):
        db = DatabaseWorker("FactoryManager.db")
        query = "SELECT * FROM Transactions"
        data = db.search(query, True)
        db.close()
        self.data_table.update_row_data(None, data)

    def delete(self):
        # Function to delete checked rows in the table
        checked_rows = self.data_table.get_row_checks()  # Get the checked rows
        print(checked_rows)
        # delete
        db = DatabaseWorker("FactoryManager.db")
        for r in checked_rows:
            id = r[0]  # use item_id instead of id
            print(id)
            query = f"delete from Transactions where id = {id}"  # use item_id instead of id
            print(query)
            db.run_query(query)
            # Create and open the alert dialog to confirm item has been deleted
            dialog = MDDialog(title="Transaction deleted!",
                              text=f"Transaction {id} has successfully been deleted.")
            dialog.open()
        db.close()
        self.update()

    # Displays the table on the screen
    def on_pre_enter(self, *args):
        self.data_table = MDDataTable(
            size_hint=(.7, .6),
            pos_hint={"center_x": .5, "center_y": .5},
            use_pagination=True,
            check=True,
            column_data=[("id", 80), ("buy", 50), ("sell", 60),
                         ("amount", 45), ("total", 70)]
        )
        self.data_table.bind(on_row_press=self.row_pressed)
        self.data_table.bind(on_check_press=self.check_pressed)
        self.add_widget(self.data_table)
        self.update()

    # When a row is pressed
    def row_pressed(self, table, row):
        print("Row pressed", row.text)
        # row.md_bg_color = "#FFF0000"

    # When a row is checked
    def check_pressed(self, table, current_row):
        print("Check pressed", current_row)



class WorkersScreen(MDScreen):
    data_table = None

    # Gets all data from orders table from the database
    def update(self):
        db = DatabaseWorker("FactoryManager.db")
        query = "SELECT * FROM Workers"
        data = db.search(query, True)
        db.close()
        self.data_table.update_row_data(None, data)

    def delete(self):
        # Function to delete checked rows in the table
        checked_rows = self.data_table.get_row_checks()  # Get the checked rows
        print(checked_rows)
        # delete
        db = DatabaseWorker("FactoryManager.db")
        for r in checked_rows:
            id = r[0]  # use item_id instead of id
            print(id)
            query = f"delete from Workers where id = {id}"  # use item_id instead of id
            print(query)
            db.run_query(query)
            # Create and open the alert dialog to confirm item has been deleted
            dialog = MDDialog(title="Worker deleted!",
                              text=f"Worker {id} has successfully been deleted.")
            dialog.open()
        db.close()
        self.update()

    # Displays the table on the screen
    def on_pre_enter(self, *args):
        self.data_table = MDDataTable(
            size_hint=(.7, .6),
            pos_hint={"center_x": .5, "center_y": .5},
            use_pagination=True,
            check=True,
            column_data=[("id", 80), ("workername", 50), ("description", 60),
                         ("message", 45), ("status", 70)]
        )
        self.data_table.bind(on_row_press=self.row_pressed)
        self.data_table.bind(on_check_press=self.check_pressed)
        self.add_widget(self.data_table)
        self.update()

    # When a row is pressed
    def row_pressed(self, table, row):
        print("Row pressed", row.text)
        # row.md_bg_color = "#FFF0000"

    # When a row is checked
    def check_pressed(self, table, current_row):
        print("Check pressed", current_row)

class OrdersForWorkersScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_status = None

    def on_cancel(self, instance, time):
        instance.dismiss()

    def select_status_type(self, instance, status):
        self.selected_status = status

    def checkbox_click(self, checkbox, value, status):
        if value:  # if the check is true
            self.selected_status = status
            print(status)
            self.ids.racket.text = f"{status}"

    def checkbox_racket_type(self, checkbox, value, status):
        if value:  # if the check is true
            self.selected_status = status
            print(status)
            self.ids.racket_type.text = f"{status}"

    def add_order(self):
        checker = True
        workername = self.ids.workername.text
        description = self.ids.description.text
        message = self.ids.message.text
        status = self.selected_status


        # Customer name validation
        if workername == "":
            self.ids.workername.error = True
            checker = False

        if checker:
            db = DatabaseWorker("FactoryManager.db")
            query = f"INSERT into Workers(workername, description, message, status) values('{workername}', '{description}', '{message}', '{status}')"
            db.run_query(query)
            db.close()

            # Pop up message
            dialog = MDDialog(title="Order added",
                              text=f"Order for {workername} has been successfully added.")
            dialog.open()

            # Reset fields
            self.ids.workername.text = ""
            self.ids.description.text = ""
            self.ids.message.text = ""
            self.selected_status_type = None



class LoginScreen(MDScreen):


    def try_login(self):
        uname = self.ids.uname.text
        passwd = self.ids.passwd.text


        db = DatabaseWorker('FactoryManager.db')

        query = f"SELECT * FROM Users WHERE Username = '{uname}' "
        user = db.search(query, True)
        print(user)
        user = user[0]
        hash = user[2]

        if check_hash(hash, passwd):
            print("User logged in successfully")
            self.parent.current = "MenuScreen"  # Go to menu screen after successful login
        else:
            dialog = MDDialog(title="Invalid information",
                              text=f"Please check the username or password you entered.")
            dialog.open()
            print("Invalid username or password")

    def try_register(self):
        print("User trying registration")
        self.parent.current = "SignupScreen"

    def try_register(self):
        print("User trying registration")
        self.parent.current = "SignupScreen"

        # Function to toggle the password visibility
    def toggle_show_password(self):
        self.show_password = not self.show_password
        self.ids.passwd.password = not self.show_password

class SignupScreen(MDScreen):

    def try_cancel(self):
        self.parent.current = "LoginScreen"

    def try_register(self):
        checker = True
        uname = self.ids.uname.text
        passwd = self.ids.e_passwd.text
        c_passwd = self.ids.c_passwd.text


        if passwd != c_passwd:
            self.ids.e_passwd.error = True
            self.ids.c_passwd.error = True
            checker = False

        else:
            # Check if username exists
            db = DatabaseWorker("FactoryManager.db")
            query = f"SELECT * from Users WHERE Username ='{uname}'"
            result = db.search(query=query)
            # If user exists, a pop up message will appears

            if result:
                dialog = MDDialog(title="User exists",
                                  text=f"The username you entered: {self.ids.uname.text} already exists.")
                dialog.open()
                checker = False

            else:
                # Inserts the new user into the database and hashes their password
                hash = make_hash(passwd)
                query = f"INSERT into users(username, password) values('{uname}','{hash}')"
                db.run_query(query)
                db.close()
                dialog = MDDialog(title="Registration completed",
                                  text=f"Your account has been successfully registered.")
                dialog.open()
                print("Registration completed")
                self.parent.current = "LoginScreen"

        if not checker:
            self.ids.uname.text = ""
            self.ids.e_passwd.text = ""
            self.ids.c_passwd.text = ""

    def insert_user(self, username, password):
        conn = sqlite3.connect('FactoryManager.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL UNIQUE,
                Password TEXT NOT NULL
            )
        ''')
        cursor.execute('INSERT INTO Users (Username, Password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()


    def toggle_show_password(self):
        self.show_password = not self.show_password
        self.ids.passwd.password = not self.show_password
        self.ids.passwd_confirm.password = not self.show_password

login_app = LoginApp()
login_app.run()
