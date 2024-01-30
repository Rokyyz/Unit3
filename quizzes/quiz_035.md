# Quiz035



# 1. UML Diagram



# 2. solutions


```.py
def mystery(list1: list, list2: list) -> list:
    output = []
    for i in list1:
        for e in list2:
            if i == e:
                output.append(i)
    return output

test1 = mystery('1', '2')
test2 = mystery('3','3')
print(test1, test2)

```

```.py
from quiz_035 import mystery

def test_mystery(list1=list, list2 = list):
    assert mystery([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [3, 4, 5]
    assert mystery([1, 2, 3], [4, 5, 6]) == []
    assert mystery([], [1, 2, 3]) == []
    assert mystery([1, 2, 3], []) == []
    assert mystery([1, 2, 3], [1, 2, 3]) == [1, 2, 3]

```

# 3. proof of work
<img width="1440" alt="Screenshot 2024-01-30 at 21 49 16" src="https://github.com/Rokyyz/Unit3/assets/134658259/ce8b32f1-4883-4802-9e23-f4365b4f3966">

<img width="1440" alt="Screenshot 2024-01-30 at 21 49 33" src="https://github.com/Rokyyz/Unit3/assets/134658259/322eef80-f503-4261-84a8-b4a41b6c8d67">

