# Quiz037



# 1. UML Diagram




# 2. solutions


```.py
class CompoundInterest:
    def __init__(self,principal,rate,number_of_years):
        self.principal = principal
        self.rate = rate
        self.number_of_years = number_of_years

    def calculate(self):
        return self.principal * (1+self.rate)**self.number_of_years


class Accounting(CompoundInterest):
    def __init__(self, customer_name,customer_email,principal, rate, number_of_years):
        super(Accounting,self).__init__(principal,rate,number_of_years)
        self.customer_name = customer_name
        self.customer_email = customer_email
    def get_msg(self):
        message = f'{self.customer_name} will have ${self.calculate():.2f} in {self.number_of_years} years if the principal is ${self.principal} with {self.get_rate_percentage()} annual compound interest'
        return message

    def get_rate_percentage(self):
        percent = f'{self.rate*100} %'
        return percent

Edvards = Accounting("Edvards", "edvards@xy.z", 1000, 0.1, 10)
print(Edvards.get_msg())

```


# 3. proof of work

<img width="1440" alt="Screenshot 2024-01-30 at 22 17 04" src="https://github.com/Rokyyz/Unit3/assets/134658259/d9e20ff3-893c-4e50-a45b-7fb0a873f1b4">
