
# Unit 3: "Airborne athletics" badminton shop center

![image](https://github.com/Rokyyz/Unit3/assets/134658259/8c89cf4d-453e-4023-8948-861f579cdafe)
[^1]

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

I chose to use SQLite as the database management system for the given task. SQLite is a free database that does not require any additional server process and is implemented on a single file. This database fits my client's needs as it is designed to handle large amounts of data efficiently [9]. It will be able to store all kinds of information safely and quickly, as it does not require going through long procedural routines that other databases such as IBM db2 use [10]. It also updates the content continuously, so little or no work is lost in case of power failure or crash, which is crucial for my client as the information being stored needs to be retrieved when they need it [11]. Furthermore, its cross-platform compatibility will benefit the client by allowing future developers to expand the program to onto other platforms. SQLite is the best option for my client as it is reliable, efficient, cost-friendly, and easy to use compared to other databases available.

I decided to use the Python language to develop the functions of the application because it is the most popular and widely used programming language and it is also among the fastest-growing programming languages in the tech industry [4]. As a result of its widespread use, the program is easier for many developers to understand than languages like C or Javascript. This will benefit applications being programmed in Python because it makes it simple for upcoming programmers to comprehend the code and advance its development. There are also a wide range of libraries that are available in Python which can be easily accessed using a basic syntax [5]. The Python programming language is adequate for developing my client's desired application.

I decided to use KivyMD for the application interface itself as it is both easy to learn and work with. One of KivyMD's main advantages is that it is a multi-platform application development framework that runs on different platforms like Android, iOS, Windows, and Linux, and is written in the Python programming language [6]. KivyMD already has a set of pre-built user-interface elements and styles that can be easily customized and integrated into Kivy-based applications [7]. This allows me to save the time and effort needed in creating user-interface elements from scratch, allowing me to focus on other aspects of the development to complete the application on time for my client. Even though there are many advantages to using KivyMD, there are also some disadvantages. For example, there are other alternatives such as Flutter or PyQt, which both have larger communities for support and are better at developing native applications, compared to KivyMD [8]. However, due to how easy it is to learn, customizability, and compatibility, I used the KivyMD library to construct the application's interface.
  
- general solution - "GUI" that is connected to the database
justification of tolls - python, SQLite, kivy

  **Design statement**

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


3 flow charts - easy, medium hard difficulty code
4-5 code fragment explenations, 1 for each criteria


[^1]: Dreamsite. "Badminton Smash Stock Photos, Images & Pictures" badminton smash,
https://thumbs.dreamstime.com/b/badminton-action-shuttlecock-fast-racket-motion-sport-167143387.jpg
