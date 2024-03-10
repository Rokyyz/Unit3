# Unit 3: "Airborne athletics" badminton shop center

![image](https://github.com/Rokyyz/Unit3/assets/134658259/8c89cf4d-453e-4023-8948-861f579cdafe) [^1]

# Criteria A: Planning
## Problem definition (Client identification)
My client owns a badminton racket company and plans to upgrade his store-running experience and his clients' shopping experience while shopping online. Since they have never had a preexisting online website they have faced **some consequences**: 

* Disorganized financial departments, do not have space to keep track of the economic transactions of their shop, thus using primitive functions, more effort, work hours, unsafe, and unorganized.
* Having problems overseeing the inventory of materials left for production, thus leading to future budget proposition problems
* Having problems seeing history records of orders, what they have ordered - materials and costs to better plan for future
* Concerns about company security breaches, someone unauthorized logging in
* Issue tackled: "As the factory grew and the owner required help from his coworkers, it was tough to figure out who was on factory grounds and who was not.
* A need to find an easier alternative to buy or make materials needed for the production as it takes too long and is too complicated to go to another side
(see evidence of consultation in Appendix A) 

## Design statement 

I plan to develop a system for a Badminton racket company using Python, Kivymd, and SQLite. This will provide a thought-out solution that would counter the challenges faced by the company CEO in maintaining accurate and up-to-date records of inventory storage, money tracking, and additional functions of the application that allows login, searching by filter, company, founder, and material description. This solution will provide a reliable and user-friendly tool to the Badminton company and its customers to manage and track all records of operations executed on the application as well as interface upgrades to ensure the program runs smoothly and effectively.

  ## Proposed solution
  
Considering the challenges my client is facing, to effectively filter orders, find workers on company grounds, track all relevant data regarding materials, and orders placed related to badminton rackets, I will develop an easy-to-use centralized manual system that will be designed and developed using SQLite, Python, and Kivy. This solution is designed to tackle the challenges originating from not having an efficient interface for my client to see the orders placed, and materials in the storage as well as lacking a worker check-in log.

The application will have a GUI (Graphical User Interface) output rather than text output. This is to meet the client's need for an easy-to-overs, user-friendly application that is capable of recording and showing the relevant information required. This is the justification behind choosing to use a GUI over a text output.

I chose to use SQLite as the database management system for the given task. SQLite is a free database that does not require any additional server process and is implemented on a single file. This database fits my client's needs as it is designed to handle large amounts of different types of data efficiently [^7]. It will be able to store all kinds of information safely and quickly, as it does not require going through long procedural routines that other databases such as IBM db2 use [^8]. It also updates the content continuously, so little or no work is lost in case of power failure or crash, which is crucial for my client as the information being stored needs to be retrieved when they need it as it is sensitive regarding transactions, login information, finances and more [^9]. Furthermore, the cross-platform compatibility will benefit the client by allowing future developers to expand, improve, and further develop the program onto other platforms. SQLite is the best option for my client as it is reliable, efficient, cost-friendly, and easy to use compared to other databases available.

I decided to use the Python language to develop the functions of the application because it is the most popular and widely used programming language and it is also among the fastest-growing programming languages in the tech industry [^2]. As a result of its widespread use, the program is easier for many developers to understand than languages like C or Javascript. This will benefit applications being programmed in Python because it makes it simple for upcoming programmers to comprehend the code and advance its development. There are also a wide range of libraries that are available in Python which can be easily accessed using a basic syntax [^3]. A big benefit is that Pyhton is quite easy to make compatible with other types of databases and, moreover, work/edit them which is majorly important for the development of this application. These are the arguments why Python programming language is adequate for developing my client's desired application.

I decided to use KivyMD for the application interface itself as it is both easy to learn and work with. One of KivyMD's main advantages is that it is a multi-platform application development framework that runs on different platforms like Android, iOS, Windows, and Linux, and is written in the Python programming language [^4]. KivyMD already has a set of pre-built user-interface elements and styles that can be easily customized and integrated into Kivy-based applications [^5]. This allows me to save the time and effort needed in creating user-interface elements from scratch, allowing me to focus on other aspects of the development to complete the application on time for my client. Even though there are many advantages to using KivyMD, there are also some disadvantages. For example, there are other alternatives such as Flutter or PyQt, which both have larger communities for support and are better at developing native applications, compared to KivyMD [^6]. However, due to how easy it is to learn, customizability, and compatibility, I used the KivyMD library to construct the application's interface.

  ## Sucess criteria
1. The application offers a feature to track money (tracking meaning that these transactions would be registered and safely saved in a database): orders, and purchases.

- [**Issue tackled: "Disorganized financial departments, do not have space to keep track of the economic transactions of their shop, thus using primitive functions, more effort, work hours, unsafe, and unorganized."**]
  
2. The application offers a feature to keep track of inventory (keeping track meaning that it is saved on a database and displayed to the owner on a separate GUI screen)

 - [**Issue tackled: "Having problems overseeing the inventory of materials left for production, thus leading to future budget proposition problems"**]
   
3. The application offers a virtual machine that allows the user to create an order and record the activity in a data table.

- [Issue tackled: "A need to find an easier alternative to place an order for the shop and thus start the production for it swiftly"]
  
4. The application offers a login page - register new accounts, and login existing accounts with responsive feedback messages.

- [**Issue tackled: "Concerns about company security breaches, someone unauthorized logging in"**]
  
5. The application offers an overview of the workers on the factory ground displaying ID, name, description, status, location, and message

- [**Issue tackled: "As the factory grew and the owner required help from his coworkers, it was tough to figure out who is on factory grounds and who is not as well as the issue of informing the workers of the tasks they need to execute."**]
  
6. The application provides a table to see messages given to any worker and their status, description, and name.

- [**Issue tackled: "As the factory grew bigger whenever the owner wanted some help or give a task to a worker, he had to call them by phone or walk to them and see them in person. Also because of company growth more and more workers were hired making the owner have difficulties in differentiating different workers."**]


# Criteria B: Design


## System Diagram

<img width="855" alt="Screenshot 2024-03-10 at 14 48 22" src="https://github.com/Rokyyz/Unit3/assets/134658259/47d12244-0a19-4892-9f4c-c55bc30e1677">

Fig. 1 This is the system diagram for the proposed solution.

The system diagram serves as a comprehensive visual depiction of the project's structure, showcasing its core components and their interconnectedness. It illustrates the application's functionality, highlighting key elements such as the programming languages employed (Python and KivyMD), the input (keyboard) , the output screen (application interface on the computer screen), the computer version and detail (Processor, version, memory, etc.), the database management system (SQLite), and the development environment (PyCharm). This graphical representation displays the intricate relationships within the system, offering a clear understanding of its architecture and operation.

## Wireframe Diagram
<img width="883" alt="Screenshot 2024-03-10 at 15 52 09" src="https://github.com/Rokyyz/Unit3/assets/134658259/a279ae6a-e01c-4a9f-bed9-98ddc7351942">

Fig. 2 This is the wireframe diagram for the application

The wireframe diagram serves a crucial purpose in providing a visual blueprint of the user interface design, representing the application's structure and layout clearly and in a simple manner. It offers insights into how different screens are accessed via designated buttons, with arrows indicating the corresponding screen transitions upon user interaction - navigation flow. Through this wireframe, users gain an understanding of the application's interface dynamics, facilitating efficient interaction and navigation within the system.

## ER Diagram


![CommSci 40](https://github.com/Rokyyz/Unit3/assets/134658259/756c1692-9844-48ce-8ba2-9d6b389674bf)
Fig. 3 This is the ER Diagram showing the 5 tables: workers, transactions, orders, users, and inventory.


## UML Diagram

![uml diagram project 3](https://github.com/Rokyyz/Unit3/assets/134658259/cc89218b-aede-4456-85dd-d584c01ba56d)

Fig 4. The UML diagram offers a comprehensive representation of the object-oriented programming (OOP) classes employed throughout the application's development journey.  Through the illustrated arrows, it is evident that all subclasses inherit essential methods and attributes from these parent classes, ensuring coherence and efficiency within the application's architecture. Additionally, the inclusion of specialized classes, such as the DatabaseWorker class, underscores their crucial role in facilitating database operations, including connection establishment, data retrieval, storage, and termination, thereby contributing significantly to the application's robustness and functionality.



## Flow Diagrams

![hard flowchart project 3 drawio](https://github.com/Rokyyz/Unit3/assets/134658259/68aa4db0-6e88-420d-bf90-7d5b1b54f9b0)


Fig. 5 This is the flow diagram that details the process of how the try_register method words

The method serves to register a user for the application to eventually allow the user to log into the application. This is achieved by first checking if passwords match (password, confirm password), then checking if the user has already been registered in the database. If they haven't the username and password are added and stored in the "users" database. To add, the password is also hashed for protection purposes.


![please work](https://github.com/Rokyyz/Unit3/assets/134658259/44f6f028-3544-4703-8b86-bbf9b55f717f)

Fig. 6 This is the flow diagram that details the process of how the add_order method works.

This method entails adding order details to a database systematically. Initially, it checks the input fields for completeness, ensuring they are not left empty. Upon validation, it establishes a connection with an SQLite database utilizing the DatabaseWoker class and executes an SQL query to incorporate the order information into the database. Subsequently, a notification pop-up confirms the successful addition of the order to the database. Lastly, it resets the input fields, enabling users to seamlessly input additional order data.



![flowchart](https://github.com/Rokyyz/Unit3/assets/134658259/2b0172c6-aa9a-44d5-b352-2b41c4d1e4a5)

Fig. 7 This is the flow diagram that details the process of how the delete method works.


The described method serves to remove selected rows from a table efficiently. Initially, it retrieves the checked rows within the table. Subsequently, it establishes a connection with an SQLite database, iterating through each selected row to execute a delete query based on its corresponding id field. Upon successful deletion, an alert dialog is generated and displayed to confirm the action. Finally, the database connection is terminated, and the table is refreshed to reflect the modifications.

## Test Plan

| Description                        | Test type        | Input                                                                                                                                                                                                                                                                                                                                     | Expected outcome                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Test for Signup System             | Unit test        | 1. Run login.py file 2. Click the Signup button on the application screen 3. Input the appropiate information in each textfield following the hint text 4. Click singup                                                                                                                                                                   | After clicking the register button, if the user already exists, a pop up message will appear letting the user know that the username already exists. If the password entered and the confirm password don't match, a red message will appear and notify the user that the passwords do not match. If all instructions were correctly followed it will take the user back to the Login screen. |
| Test for Login System              | Unit test        | 1. Run login.py file 2. Follow instructions and enter the appropiate information in each textfield following the hint text 3. Click Login                                                                                                                                                                                                 | After clicking login, if the account does not exist, a pop up message will appear letting the user know that the account was not found. If the account credentials do exist, it should take the user to the homepage.                                                                                                                                                                         |
| Test for Logout System             | Unit test        | 1. Login 2. Press the logout button on the homepage                                                                                                                                                                                                                                                                                       | When the logout button is pressed, it should direct the user back to the log in screen                                                                                                                                                                                                                                                                                                        |
| Test for Add Order System          | Integration test | 1. Login 2. Click Add Flight button 3. Enter the appropiate order information in the textfields according to the hint text. 4. Press add order button                                                                                                                                                                                     | When the user enters order information correctly, a pop up message should appear telling the user that the order has been added. When a piece of information is incorrect within the textfield, error hint texts in red will appear to show the user that the information entered was incorrect or not entered at all.                                                                        |
| Test for Inventory System          | Integration test | 1. Login 2. Click Inventory button 3. Click on the material that the user wants to buy 4. In the text field enter the quantity of the amount of the material that will be bought.                                                                                                                                                         | When the user enters the amount the cost of the material should match the one set previously, the price should respond to the quantity wanted to be bought. If the purchase was successful there should be a popup indicating that it was successful                                                                                                                                          |
| Test for See orders System         | Unit test        | 1. Login 2. Click See orders button 3. Monitor if the order that was placed previously has been recorded and updated to the table. 4. Test if an order can be deleted with checkbox press and delete button press                                                                                                                         | After clicking see orders all the previous as well as the new order should be able to be seen in the table. When deleting an order a popup message should appear and the table should be updated of the changes.                                                                                                                                                                              |
| Test for Transactions System       | Unit test        | 1. Login 2. Click the Transactions button 3.  Monitor if the inventory order that was placed previously has been recorded and updated to the table. 4. Test if a transaction can be deleted with the checkbox press and delete button press                                                                                               | After clicking transaction all the previous as well as the new transactions should be able to be seen in the table. When deleting a transaction a popup message should appear and the table should be updated of the changes.                                                                                                                                                                 |
| Test for Orders For Workers System | Integration test | 1. Login 2. Click the Orders for Workers button 3. Click on the input field to enter the worker's name 4. Click on the input field to enter the worker's description 5. Choose to click wether the worker is on or off factory grounds 6. Click on the input field to enter the message/order you want to leave for the respective worker | When the user enters order information correctly, a pop up message should appear telling the user that the message has been added. When a piece of information is incorrect within the textfield, error hint texts in red will appear to show the user that the information entered was incorrect or not entered at all.                                                                      |
| Test for Workers System            | Unit test        | 1. Login 2. Click Workers button 3. Monitor if the information that was placed for the respective worker previously has been recorded and updated to the table. 4. Test if information about a worker can be deleted with the checkbox press and delete button press                                                                      | Monitor if the information about a worker that was placed previously has been recorded and updated to the table. 4. Test if information entered about the worker can be deleted with the checkbox press and delete button press                                                                                                                                                               |
| Code Review                        | Code Review      | Reviewing if the code has adequate comments, function names, and variable names: 1. Open login.py file. 2. Review the code and make changes or add comments where it is necessary/if needed for my understanding and any further developer's understanding                                                                                | Revised version of the code that is easy to follow and understand                                                                                                                                                                                                                                                                                                                             |

## Record of Tasks

| Task No | Planned Action                                                                             | Planned Outcome                                                                                                                                                                                                                                                                             | Design cycle | Time estimate | Planned Outcome | Criterion |
|---------|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------|-----------------|-----------|
| 1       | First meeting with client                                                                  | To understand client problem and requirements                                                                                                                                                                                                                                               | Planning     | 30 min        | 15 Feb          | A         |
| 2       | Write down success criteria                                                                | To list down the first success criteria                                                                                                                                                                                                                                                     | Planning     | 20 min        | 16 Feb          | A         |
| 3       | Write problem definition                                                                   | Have problem definition which will identify who client is and the product that the client wants                                                                                                                                                                                             | Planning     | 40 min        | 16 Feb          | A         |
| 4       | Finalise success criteria                                                                  | Prepare a satisfactory criteria to present to client                                                                                                                                                                                                                                        | Planning     | 20 min        | 16 Feb          | A         |
| 5       | Meet with the client to discuss the success criteria.                                      | Receive the final approval to start creating the application                                                                                                                                                                                                                                | Planning     | 20 min        | 19 Feb          | A         |
| 6       | Research and develop a rationale for the proposed solution.                                | Finish rationale for proposed solution                                                                                                                                                                                                                                                      | Planning     | 30 min        | 20 Feb          | A         |
| 7       | Create UML diagram                                                                         | Develop a clear idea of the hardware and software requirements for the proposed solution                                                                                                                                                                                                    | Design       | 60 min        | 22 Feb          | B         |
| 8       | Create Wireframe diagram                                                                   | Develop a clear idea how the applications screens will look like as well as their functionality, navigation                                                                                                                                                                                 | Design       | 70 min        | 22 Feb          | B         |
| 9       | Create ER diagram                                                                          | Create an ER diagram that illustrates the tables and attributes of the solution                                                                                                                                                                                                             | Design       | 30 min        | 23 Feb          | B         |
| 10      | Create system diagram                                                                      | Develop a clear idea of the hardware and software requirements for the proposed solution                                                                                                                                                                                                    | Design       | 40 min        | 23 Feb          | B         |
| 11      | Produce Flowchart diagrams                                                                 | Develop flowcharts that is formal but at the same time simple enough to obtain a clearer understanding of the code's and other alogrithm's process                                                                                                                                          | Design       | 180 min       | 24 Feb          | B         |
| 12      | Code startup screeen                                                                       | Have an inviting screen for client to use                                                                                                                                                                                                                                                   | Development  | 120 min       | 25 Feb          | C         |
| 13      | Code Login and signup screen, welcome message for the company member using the application | Have a login and signup screen for client to use and register                                                                                                                                                                                                                               | Development  | 190 min       | 27 Feb          | C         |
| 14      | Add show password and check password, user name function                                   | Make the application more resilient towards security breaches and more simple for use                                                                                                                                                                                                       | Development  | 60 min        | 28 Feb          | C         |
| 15      | Create menu screen according to the wireframe diagram                                      | Screen that contains all the available functions of the program                                                                                                                                                                                                                             | Development  | 120 min       | 28 Feb          | C         |
| 16      | Create database with tables and attributes                                                 | Insert and store inputs of users, items, transactions, messages, inventory, and worker information into the database FactoryManager                                                                                                                                                         | Development  | 30 min        | 29 Feb          | C         |
| 17      | Create Add order screen                                                                    | A page that allows the user to place orders into the 'orders' table within the database                                                                                                                                                                                                     | Development  | 60 min        | 1 Mar           | C         |
| 18      | Code Add order screen                                                                      | A functional program that allows the client to enter an order to the respective information                                                                                                                                                                                                 | Development  | 120 min       | 1 Mar           | C         |
| 19      | Add date, time picker to add order system                                                  | A calendar, clock that users can click on to input the date, time of order                                                                                                                                                                                                                  | Development  | 60 min        | 3 Mar           | C         |
| 20      | Code See order screen                                                                      | A page that allows the manager to see the orders placed by the store's clients as well as  the option to delete an order if needed                                                                                                                                                          | Development  | 60 min        | 3 Mar           | C         |
| 21      | Code Inventory screen                                                                      | A functional program that allows the manager to manage their material inventory. If any material that is used in the racket creation process is out of stock or running out the manager can buy the respective material and see the according price based on the material type and quantity | Development  | 150 min       | 3 Mar           | C         |
| 22      | Code Transactions screen                                                                   | A page that allows the manager to see the material purchase history as well as the option to delete a transaction if needed                                                                                                                                                                 | Development  | 30 min        | 6 Mar           | C         |
| 23      | Code Orders for workers screen                                                             | A Functional program that allows the manager to enter information that needs to be expressed to the respective workers                                                                                                                                                                      | Development  | 80 min        | 7 Mar           | C         |
| 24      | Code Workers screen                                                                        | A page that allows the workers and the manager to see the messages placed by the manager as well as the option to delete message if requires                                                                                                                                                | Development  | 20 min        | 9 Mar           | C         |
| 25      | Code Logout option                                                                         | A popup screen that allows the user to choose to logout of the application                                                                                                                                                                                                                  | Development  | 70 min        | 9 Mar           | C         |
| 26      | Show the application to the client                                                         | Ensure that all elements and functions of the applications are tailor-made to the client's needs and wants                                                                                                                                                                                  | Evaluation   | 60 min        | 9 Mar           | A         |
| 27      | Finalise program, check for inefficiency, bugs                                             | Test all the functions, interface to make sure the application runs smoothly and seamlessly                                                                                                                                                                                                 | Development  | 60 min        | 9 Mar           | C         |
| 28      | Finish test plans                                                                          | Contains the procedures for testing the application as well as the expected results of each test.                                                                                                                                                                                           | Planning     | 130 min       | 9 Mar           | B         |
| 29      | Write Criteria B                                                                           | Finalize graphs, action and plan processes                                                                                                                                                                                                                                                  | Evaluation   | 70 min        | 9 Mar           | B         |
| 30      | Write Criteria C                                                                           | Write the code descriptions as well as the specifics of the techniques implemented.                                                                                                                                                                                                         | Evaluation   | 150 min       | 9 Mar           | C         |
| 31      | Film final video                                                                           | Video demonstration of all success criterias operating and functioning within the built application                                                                                                                                                                                         | Evaluation   | 60 min        | 10 Mar          | D         |

# Criteria C: Development

## Techniques Used

1. Object Oriented Programming (OOP): Classes, Inheritance
2. SQLite Database
3. Variables
4. For loops
5. If statements
6. Functions

## Computational thinking
1. decomposition
2. pattern recognition
3. abstraction
4. algorithm design

## Development of User Interface Using KivyMD

### Screen Manager

```.kv
ScreenManager:
    LoginScreen:
        name: "LoginScreen"

    SignupScreen:
        name: "SignupScreen"

    MenuScreen:
        name: "MenuScreen"

    InventoryScreen:
        name: "InventoryScreen"

    TransactionsScreen:
        name: "TransactionsScreen"

    WorkersScreen:
        name: "WorkersScreen"

    OrdersForWorkersScreen:
        name: "OrdersForWorkersScreen"

    AddOrdersScreen
        name: "AddOrdersScreen"


    SeeOrdersScreen
        name:"SeeOrdersScreen"
```

A quick and easy method to arrange and navigate between the various screens in your application is with the ScreenManager. Because each screen is specified using a unique class that derives from the Screen class, unique functionality and properties may be defined for every screen. I was able to manage multiple screens and quickly transition between them because to the use of abstraction.

### General Application Screen

```.kv
<LoginScreen>:
    canvas.before:
        Rectangle:
            source: "bad.jpeg"
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        margin: 'sdp50'

        MDLabel:
            text: "Welcome to Airborne Rackets"
            font_name: 'Copyduck.ttf'
            font_size: '30pt'
            bold: True
            color: 'black'
            pos_hint:{"center_x":.75, "center_y":.2}
            theme_text_color: 'Custom'
            text_color: 0,0,0,1
            halign: 'center'

    MDCard:
        size_hint: .35, .8
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .3, "center_y": .5}
        padding: dp(50)
        md_bg_color: [0,0,0,0.5]
```
This code block in the Kivy language defines the appearance of the "LoginScreen" screen. This is only one of the application's many screens. The KivyMD library contains an MDCard component, which simulates a rectangular card with rounded corners that holds other widgets. I used this as the overall basic configuration for every panel in the programme, making sure that every screen had the same background image and setup because my customer requested a polished and uncluttered appearance.

### MDFillRoundFlatIconButton

```.kv
MDFillRoundFlatIconButton:
                id: menu_add_order
                size_hint: 1, None
                size_hint_y: None
                height: "100dp"
                icon: 'plus-circle'
                text: "Add order"
                font_size: "20sp"
                on_press: root.go_to_add_orders()
```

One of the homepage buttons that will take the user to the specified screen in ScreenManager is displayed in the KV code above. This type of button is utilised on the homepage and satisfies the client's desire for a clean, professional look by being visually appealing and uncomplicated. I chose to utilise this button in order to provide some variation to the other button shapes I had. Another button I utilised is called MDRaisedButton; it is essentially the same as the button displayed in the code above, but it lacks an icon and a circular form.

### MDLabel

```.kv
MDLabel:  
                text: "Inventory Manager"
                font_style: "H3"
                halign: "left"
                pos_hint: {'center_x': 0.51, 'center_y': 1}
                size_hint: 1, 0.1
```

This is an MDLabel's KV code. Text labels known as MDLabels are displayed on the screen to help users navigate where they are in the programme. In this instance, I let the user know that they have reached the air traffic control programme by using the MDLabel as the headline for my homepage screen.


### MDTextField

```.kv
MDTextField:
        id: amount
        hint_text: "Enter amount of the material you want to buy"
        input_filter: 'int'
        on_text:
            self.text = str(max(0, min(100, int(self.text or 0))))
            root.update_amount_text()
```

I utilised an MDTextField similar to this one for my client's application. On the apps page, there are text boxes called MDTextFields that let users enter data using their keyboard. This is a crucial component of the application's user interface for my customer since it enables them to enter any data they desire into the system. I became aware that there is a good possibility that users will enter data into the MDTextField incorrectly when I was programming the MDTextFields. As previously mentioned, I have helper text, so if the user forgets to enter a piece of information, a red helper text error will appear to direct the user.

### MDCheckbox

```.kv
MDCheckbox:                      
        id: show_pass                
        size_hint_x: 0.1             
        on_active: passwd.password = not self.active  
        on_active: c_log_passwd.password = not self.active
        active: False
```

### MDIconButton

```.kv
MDIconButton:
                icon: "eye"
                size_hint_x: 0.08
```
MDIconButton is a button with an icon from the Material Design icon set, this allows for the application to appear more eye-appealing

### MDBoxLayout

```.kv
MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .1
```

A MDBoxLayout in KivyMD, is a box layout class that provides better compatibility with the Material Design specifications. This MDBoxLayout can be used to contain other widgets and arrange them horizontally within the application. It is a major help for the developer, this makes it easier to position other tools while designing the application.


## Development of Application Using Python

## Setting up the file

```.py
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

```
A number of libraries needed to construct the Refrigerator Manager application are imported by the code. The SQLite database, which will be used to store information about users, workers, transactions, inventory, orders, and messages, may be accessed and modified using the sqlite3 library and DatabaseWorker. Additionally, it allows for the password can be hashed and verified. The application's graphical user interface (GUI), which will be simple to use and navigate, is built using the various kivymd libraries.

## Database worker

```.py
    def update(self):
        db = DatabaseWorker("FactoryManager.db")
        query = "SELECT * FROM Orders"
        data = db.search(query, True)
        db.close()
        self.data_table.update_row_data(None, data)
```
Here we can see a function where DatabasWorker is utilized. It initializes a connection to a SQLite database with the given name. It simplifies the process of interacting with the manipulation of databases, thus making the code and time spent coding more efficient.
Firstly it establishes a connection, then the query selects every asset and its values from the table Orders, date variable is assigned to fetching these certain values from the table and lastly, when everything has been done it closes the connection to the database. 

## Login System

### User input information Verification

```.py
        if check_hash(hash, passwd):
            print("User logged in successfully")
            self.parent.current = "MenuScreen"  # Go to menu screen after successful login
        else:
            dialog = MDDialog(title="Invalid information",
                              text=f"Please check the username or password you entered.")
            dialog.open()

```

This code snippet is part of a login system. It checks whether the password entered by the user matches the password stored in the database for the corresponding username. First, it computes a hash of the entered password and compares it with the stored hash in the database. If the hashes match, indicating that the password is correct, the program proceeds to log the user in by changing the current screen to the "MenuScreen." However, if the hashes do not match, meaning the password is incorrect, it displays an error message prompting the user to check their username or password. This functionality ensures secure user authentication, a fundamental aspect of any login system. Similar methods can be applied in other parts of the codebase, such as registration and data validation, to ensure data integrity and system reliability.

### User Credential Verification

### Pop Up Message

## Add Orders System

### Missing Value Validation

### Time Picker

### Date Picker

### Checkboxes

### Insert Query






# Criteria D: Functionality
## Video Showcasing the Functionality of the Application

[^1]: Badminton racket review. "Latest Racket Reviews in the E-zone" How to choose a badminton racket?,
[https://thumbs.dreamstime.com/b/badminton-action-shuttlecock-fast-racket-motion-sport-167143387.jpg](https://www.google.com/url?sa=i&url=https%3A%2F%2Fbadmintonracketreview.com%2F&psig=AOvVaw2rEdTJQZrQ3b7EnWwVMIya&ust=1710081477001000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCKiFi46054QDFQAAAAAdAAAAABAE)https://www.google.com/url?sa=i&url=https%3A%2F%2Fbadmintonracketreview.com%2F&psig=AOvVaw2rEdTJQZrQ3b7EnWwVMIya&ust=1710081477001000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCKiFi46054QDFQAAAAAdAAAAABAE

[^2]: Sanyal, Sayantani. 10 Reasons Why Python Is One Of The Best Programming Languages. Accessed Feburary 10, 2023

[^3]: Advantages and disadvantages of python - how it is dominating Programming World. DataFlair. Accessed Feburary 10, 2023

[^4]: "Kivy vs Flutter." Educba, n.d., https://www.educba.com/kivy-vs-flutter/. Accessed Feburary 10, 2023

[^5]: "Building a Simple Application using KivyMD in Python." GeeksforGeeks, 17 Feb. 2021, https://www.geeksforgeeks.org/building-a-simple-application-using-kivymd-in-python/, Accessed Feb 10, 2023

[^6]: "Kivy vs PyQt." Educba, n.d., https://www.educba.com/kivy-vs-pyqt/. Accessed Feburary 10, 2023

[^7]: Gomathy, Kavya. "5 Reasons to Use SQLite, the Tiny Giant for Your Next Project." Medium, The Startup, 4 Jan. 2022, https://medium.com/swlh/5-reasons-to-use-sqlite-the-tiny-giant-for-your-next-project-a6bc384b2df4. Accessed Feburary 10, 2023

[^8]: Yegulalp, Serdar. "Why You Should Use SQLite." InfoWorld, IDG Communications, Inc., 13 Feb. 2019, https://www.infoworld.com/article/3331923/why-you-should-use-sqlite.html. Accessed Feburary 10, 2023

[^9]: "SQLite Advantages and Disadvantages." javatpoint, n.d., https://www.javatpoint.com/sqlite-advantages-and-disadvantages. Accessed Feburary 10, 2023




# Appendix
## Evidence of consultation
### Client approval of proposed success criteria

<img width="857" alt="Screenshot 2024-03-10 at 00 05 51" src="https://github.com/Rokyyz/Unit3/assets/134658259/9525e522-a8d3-474a-bc03-81f57250b140">

<img width="891" alt="Screenshot 2024-03-10 at 03 13 58" src="https://github.com/Rokyyz/Unit3/assets/134658259/ddab83fb-9766-4879-bf1f-2f80b95cc14d">

### Client's review of the application during the development process

<img width="887" alt="Screenshot 2024-03-10 at 14 44 24" src="https://github.com/Rokyyz/Unit3/assets/134658259/be116b58-fc5f-46b0-8c67-5ee57a9fe7b7">


### Client's review of final product
<img width="867" alt="Screenshot 2024-03-10 at 14 46 42" src="https://github.com/Rokyyz/Unit3/assets/134658259/732b38ee-828d-49b2-bc05-42cf1ec462bf">


