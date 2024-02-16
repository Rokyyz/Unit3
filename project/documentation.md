
# Unit 3: Badminton racket economic transaction system

![image](https://github.com/Rokyyz/Unit3/assets/134658259/3c97f3c4-5331-40dc-87a3-ed900b3e7f75) [^1]

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
  
Considering the challenges my client is facing, in order to effectively filter orders, find workers on company grounds, track all relevant data regarding materials, orders placed related to badminton rakcets, I will develop an easy-to-use centralized manual system that will be designed and developed using SQLite, Python, and Kivy. This solution is designed to tackle the challenges originating from not having an efficient interface for my client to see the orders placed, materials in the storage as well as lacking a worker check-in log .

The application will have a GUI (Graphical User Interface) output rather than text output. This is to meet the client's need for a easy to oversee, user frienmdly application that is capable of recording and showing the relevant information required. This is the justification behind chosing to use a GUI over a text output.

I made a choice to use SQLite as the database management system for the given task. SQLite is a free database that does not require any additional server process, and is implemented on a single file. This database fits my client's needs as it is designed to handle large amounts of data efficiently [9]. It will be able to store all kinds of information safely and quickly, as it does not require to go through long procedural routines other databases such as IBM db2 use [10]. It also updates the content continuously, so little or no work is lost in a case of power failure or crash, which is crucial for my client as the information being stored needs to be retrieved when they need it [11]. Furthermore, its cross-platform compatibilty will allow benefit the client by allowing future developers to expand the program to onto other platforms. SQLite is the best option for my client as it is reliable, efficient, and cost-friendly, and easy to use compared to other databases available.

I decided to use the Python language to develop the functions of the appliction because it is the most popular and widely used programming language and it is also among the fastest-growing programming languages in the tech industry [4]. As a result of its widespread use, the program is easier for many developers to understand than languages like C or Javascript. This will benefit application in being programmed in Python because it makes it simple for upcoming programmers to comprehend the code and advance its development. There are also a wide range of libraries that are available in Python which can be easily accessed using a basic syntax [5]. The Python programming language is adequate for developing my client's desired application.

For the application interface itself, I decided to use KivyMD as it is both easy to learn and work with. One of KivyMD's main advantages is that it is a multi-platform application development framework that runs on different platforms like Android, iOS, Windows, Linux, and is written in the Python programming language [6]. KivyMD already has a set of pre-built user-interfacce elements and styles that can be easily customized and integrated into Kivy-based applications [7]. This allows me to save the time and effort needed in creating user-interface elements from scratch, allowing me to focus on other aspects of the development so I can complete the application on time for my client. Even though there are many advantages of using KivyMD, there are also some disadvantages. For example, there are other alternatives such as Flutter or PyQt, which both have larger communities for support and are better at developing native applications, compared to KivyMD [8]. However, due to how easy it is to learn, customizability, and compatibility, I chose to use KivyMD library to construct the application's interface.
  
- general solution - "GUI" that is connected to the database
justification of tolls - python, SQLite, kivy

  **Design statement**

  ## Sucess criteria
1. The application offers a feature to track money (tracking meaning that these transactions would be registered and safely saved in a database): orders, purchases [**Issue tackled: "Disorganized financial departments, do not have space to keep track of the economic transactions of their shop, thus using primitive functions, more effort, work hours, unsafe, and unorganized."**]
2. The application offers a feature to keep track of inventory (keeping track meaning that it is saved on a database and displayed to the owner on a separate GUI screen) [**Issue tackled: "Having problems overseeing the inventory of materials left for production, thus leading to future budget proposition problems"**]
3. The application offers a machine that allows the user to create an item, thus altering the inventory [Issue tackled: "A need to find an easier alternative to buy or make materials needed for the production as it takes too long and is too complicated to go to another side"]
4. The application offers a login page - register new accounts, and existing accounts [**Issue tackled: "Concerns about company security breaches, someone unauthorized logging in"**] 
5. The application offers an overview of the workers on the factory ground displaying ID, name, description, status, and location [**Issue tackled: "As the factory grew and the owner required help from his coworkers, it was tough to figure out who is on factory grounds and who is not."**]
6. The application offers a feature to filter customer orders of the shop based on name and or ID, displaying materials and budget used [**Issue tackled: "Having problems seeing history records of orders, what they have ordered - materials and costs to better plan for future"**]


[^1]: Dreamsite. "Badminton Smash Stock Photos, Images & Pictures" badminton smash,
https://thumbs.dreamstime.com/b/badminton-action-shuttlecock-fast-racket-motion-sport-167143387.jpg
