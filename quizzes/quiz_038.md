# Quiz038



# 1. UML Diagram
![CommSci 21](https://github.com/Rokyyz/Unit3/assets/134658259/5770bb0f-b5eb-4fbe-aff4-0d532ada7675)


# 2. solutions


```.py
import matplotlib.pyplot as plt
import random
class SalemanMap:
    def __init__(self):
        self.x = []
        self.y = []
        self.name = []


    def generate_data(self, name):
        self.name = name
        for i in range(len(name)):
            self.x.append(random.randint(0,100))
            self.y.append(random.randint(0,100))
    def get_map(self):
        plt.scatter(self.x, self.y)
        for i, city in enumerate(self.name):
            plt.text(self.x[i], self.y[i], city, fontsize=10)
        plt.xlabel('Distance (km)')
        plt.ylabel('Distance (km)')
        plt.show()

test = SalemanMap()
test.generate_data(['Kobe', 'Tokyo', 'Nagoya', 'Kyoto', 'Saitama', 'Yokohama', 'Kawasaki', 'Sapporo', 'Fukuoka'])
test.get_map()

```


# 3. proof of work
<img width="1440" alt="Screenshot 2024-01-30 at 22 28 26" src="https://github.com/Rokyyz/Unit3/assets/134658259/1752bcb6-2375-4a29-8757-82495edee88d">
