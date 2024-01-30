# Quiz036



# 1. UML Diagram

![CommSci 18](https://github.com/Rokyyz/Unit3/assets/134658259/1a70f00a-6b8b-4f6c-95d2-45b94e28e1e5)


# 2. solutions


```.py
class Convert:
    def __init__(self):
        self.roman_symbols = {
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def convert_to_roman(self, decimal) -> str:
        output = ""
        if 0 < decimal < 400:
            for key, value in self.roman_symbols.items():
                q = decimal // key
                output += value * q
                decimal = decimal % key
        return output

converter = Convert()
print(converter.convert_to_roman(93))

```


# 3. proof of work

<img width="1440" alt="Screenshot 2024-01-30 at 22 12 25" src="https://github.com/Rokyyz/Unit3/assets/134658259/801b628c-b4a2-48a9-b107-e7515d35ef93">
