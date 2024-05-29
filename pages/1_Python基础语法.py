import streamlit as st


'### 语言特性'
"""
- 代码简洁易读：Python的语法简洁明了，易于学习和使用。
- 跨平台：Python支持多种操作系统，包括Windows、Linux和Mac OS等。
- 丰富的库和框架：Python拥有大量的第三方库和框架，可以满足各种开发需求。
- 开源和免费：Python是一种开源语言，可以免费使用和分发。
- 数据科学：Python在数据分析、机器学习和人工智能等领域有广泛应用，如NumPy、Pandas、SciPy、Scikit-learn和TensorFlow等库。
"""


'### 变量与赋值'
"""
- 变量名可以由字母、数字和下划线组成，但不能以数字开头。
- 变量名是大小写敏感的。
- Python是动态类型语言，不需要在定义变量时指定数据类型，会根据赋给变量的值自动确定数据类型。
- 赋值使用 = 符号。

"""

'### 注释'
"""
- 单行注释使用 # 符号。
- 多行注释虽然不像其他语言那样有特定的语法，但可以使用三引号

"""

# 基本数据类型

st.markdown('### 基本数据类型')

st.markdown("""  
- 数字类型: 整数 (int)、浮点数 (float)、复数 (complex)
- 布尔类型: True 和 False
- 字符串类型: 由字符组成的序列
""")
code = """
#声明变量
number = 10
string = "Hello, world!"
boolean = True

"""
#
st.code(code, language="python")

'##### 数据类型转换'
code = """
# 整数转浮点数  
int_num = 10  
float_num = float(int_num)  # 结果为 10.0  
  
# 浮点数转整数（注意：这会舍去小数部分）  
float_num = 10.5  
int_num = int(float_num)  # 结果为 10

# 字符串转整数  
str_num = "123"  
int_num = int(str_num)  # 结果为 123  
  
# 字符串转浮点数  
str_num = "123.45"  
float_num = float(str_num)  # 结果为 123.45  
  
# 注意：如果字符串不能被转换为数字，将会引发 ValueError 异常

"""
st.code(code, language="python")

st.markdown('### 运算符')
st.markdown('运算符用于执行操作。Python 支持算术运算符（+、-、*、/、//、%、**）、比较运算符（==、!=、<、>、<=、>=）、逻辑运算符（and、or、not）、成员运算符（in, '
            'not in）、身份运算符（is, is not）。')
code = """
# 算术运算符
result = 10 + 5
print(result)  # 输出：15

# 比较运算符
is_equal = 10 == 5
print(is_equal)  # 输出：False

# 逻辑运算符
is_true = True and not False
print(is_true)  # 输出：True

"""
#
st.code(code, language="python")

st.markdown('### 数据结构')
st.markdown('数据结构用于组织和存储数据。Python 支持列表、元组、字典和集合。')
st.markdown("""  
- 列表类型: 可变的有序集合
- 元组类型: 不可变的有序集合
- 字典类型: 无序的键值对集合
- 集合类型: 无序的唯一元素集合
""")
code = """
# 列表
numbers = [1, 2, 3, 4, 5]
print(numbers)  # 输出：[1, 2, 3, 4, 5]

# 元组
fruits = ("apple", "banana", "orange")
print(fruits)  # 输出：('apple', 'banana', 'orange')

# 字典
person = {"name": "John Doe", "age": 30, "city": "New York"}
print(person)  # 输出：{'name': 'John Doe', 'age': 30, 'city': 'New York'}

# 集合
set1 = {1, 2, 3, 4, 5}
print(set1)  # 输出：{1, 2, 3, 4, 5}
"""
#
st.code(code, language="python")

st.markdown('Python的列表（list）和字典（dict）都有许多内置方法，用于操作这些数据结构。')

'##### 列表内置方法'
"""
- append(x): 将一个元素添加到列表的末尾。
- extend(iterable): 将可迭代对象的所有元素添加到列表的末尾。
- insert(index, value): 在指定索引处插入元素。
- remove(value): 移除列表中第一个出现的指定值。
- pop([index]): 移除并返回指定索引处的元素（默认为最后一个元素）。
- clear(): 移除列表中的所有元素。
- index(value, [start, [stop]]): 返回列表中第一个出现的指定值的索引。
- count(value): 返回列表中指定值出现的次数。
- sort([key, reverse]): 对列表进行排序。
- reverse(): 反转列表中的元素。
- copy(): 返回列表的浅拷贝。

"""
'##### 字典内置方法'
"""
- clear(): 移除字典中的所有键值对。
- copy(): 返回字典的浅拷贝。
- fromkeys(iterable[, value]): 创建一个新字典，以序列中的元素作为键，value作为值（默认为None）。
- get(key[, default]): 返回指定键的值，如果键不存在则返回默认值（默认为None）。
- items(): 返回一个包含字典中所有键值对的视图对象。
- keys(): 返回一个包含字典中所有键的视图对象。
- pop(key[, default]): 如果键在字典中，移除它并返回它的值；否则返回默认值（默认为引发KeyError）。
- update([other]): 使用来自其他字典或键值对（可迭代）的项更新字典。
- del 操作符: 删除指定的键。
- len(): 返回字典中的键-值对数量。
- in 和 not in: 检查键是否在字典中。
"""

st.markdown('### 模块和包')
st.markdown(
    '在 Python 中，模块和包是组织代码的基本单元。模块是包含代码的文件，而包是包含模块的目录。使用模块和包可以提高代码的可重用性和可维护性。')
code = """
#math 模块：此模块包含许多数学函数，例如 sin、cos、tan、sqrt 和 log。
import math

result = math.sqrt(25)
print(result)  # 输出：5.0
"""
#
st.code(code, language="python")

code = """

#random 模块：此模块包含用于生成随机数的函数。
import random

number = random.randint(1, 10)
print(number)  # 输出：随机整数介于 1 和 10 之间
"""
#
st.code(code, language="python")

code = """
#os 模块：此模块包含用于与操作系统交互的函数。
import os

filename = "myfile.txt"

if os.path.exists(filename):
    print("文件存在")
else:
    print("文件不存在")

"""
#
st.code(code, language="python")

# 函数的含义

st.markdown('### 使用 pip')
st.markdown(
    'pip 是 Python 的包安装程序。它是大多数 Python 发行版中包含的标准工具。要使用 pip 安装包，请打开终端或命令提示符并运行以下命令：')
code = """
pip install package_name
"""
#
st.code(code, language="python")

st.markdown('### 流程控制')
st.markdown(
    'Python 的流程控制语句用于控制程序的执行顺序。它们使您可以根据条件执行不同的代码块，循环重复代码以及处理错误。')
st.markdown('1. if语句')
code = """
number = 15

if number > 10:
    print("数字大于 10")
else:
    print("数字小于或等于 10")
"""
#
st.code(code, language="python")
st.markdown('2. elif 语句')
code = """
number = 10

if number > 10:
    print("数字大于 10")
elif number == 10:
    print("数字等于 10")
else:
    print("数字小于 10")
"""
#
st.code(code, language="python")
st.markdown('3. while循环')
code = """
i = 1

while i <= 10:
    print(i)
    i += 1
"""
#
st.code(code, language="python")
st.markdown('4. for循环')
code = """
string = "Hello, world!"

for i, char in enumerate(string):
    print(f"索引：{i}，字符：{char}")
"""
#
st.code(code, language="python")
st.markdown('5. break语句')
code = """
#break 语句用于跳出循环。
#它会立即退出当前循环并继续执行程序的其余部分。

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print(f"找到偶数：{number}")
        break
"""
#
st.code(code, language="python")
st.markdown('6. continue语句')
code = """
#continue 语句用于跳过循环的当前迭代并继续下一个迭代。
#它将跳过剩余的代码块并立即开始下一次迭代。

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
"""
#
st.code(code, language="python")

# 函数的含义

st.markdown('### 函数')

code = """
#函数用于封装代码块并可重复调用

def hello_world():
  print("Hello, world!")

hello_world()
"""
st.code(code, language="python")
st.write('接收参数并返回')
code = """
def square(number):
    #计算数字的平方

    #参数:
        #number: 要计算平方的数字

    #返回值:
        #数字的平方
    return number * number

result = square(5)
print(result)  # 输出：25
"""
st.code(code, language="python")
'#### 匿名函数'
code = """
add = lambda x, y: x + y  # 定义一个匿名函数  
print(add(3, 4))  # 调用并打印结果
"""
st.code(code, language="python")

'#### 异常处理'
'在Python中，try/except块通常用于处理可能失败的操作，如文件读写、网络请求等。'
code = """
try:  
    # 尝试执行的代码块  
    # 如果在这里发生了异常，那么程序会立即跳转到对应的except块（如果有的话）  
    result = 10 / 0  # 这将引发一个ZeroDivisionError异常  
except ZeroDivisionError:  
    # 处理ZeroDivisionError异常的代码块  
    print("不能除以零！")  
except Exception as e:  
    # 处理其他所有异常的代码块（可选）  
    print(f"发生了一个错误: {e}")  
else:  
    # 如果没有异常发生，将执行这个代码块（可选）  
    print("没有发生异常")  
finally:  
    # 无论是否发生异常，都将执行这个代码块（可选）  
    print("这是finally块")
"""
st.code(code, language="python")

'#### 类'
'在Python中，类（Class）是用于创建对象的模板或蓝图。通过类，我们可以定义对象的属性和方法。'

code = """ class Watershed:
    def __init__(self, name, area, rainfall, runoff_coefficient):
        self.name = name  # 流域名称  
        self.area = area  # 流域面积（单位：平方千米）  
        self.rainfall = rainfall  # 降雨量（单位：毫米）  
        self.runoff_coefficient = runoff_coefficient  # 径流系数  

    def calculate_runoff(self):
        # 计算径流量（单位：立方米）  
        # 径流量 = 流域面积 * 降雨量 * 径流系数 / 1000
        runoff_volume = self.area * self.rainfall * self.runoff_coefficient / 1000
        return runoff_volume

    def display_info(self):
        print(f"流域名称: {self.name}")
        print(f"流域面积: {self.area} 平方千米")
        print(f"降雨量: {self.rainfall} 毫米")
        print(f"径流系数: {self.runoff_coefficient}")
        print(f"径流量: {self.calculate_runoff()} 立方米")

    # 创建一个流域对象  


watershed1 = Watershed("潏河流域", 100, 50, 0.6)

# 显示流域信息  
watershed1.display_info()"""
st.code(code, language="python")

'#### 讨论：什么时候使用函数，什么时候时候类'
"""
- 当你要模拟现实世界中的事物或概念时，使用类是很自然的。类可以表示具有属性和行为的对象，这些属性和行为可以反映现实世界中实体的特征和行为。
- 当对象需要维护自己的状态时，使用类是很有用的。类的实例（即对象）可以有自己的属性和方法，这些属性和方法可以访问和修改对象的状态。
- 类提供了一种封装数据（属性）和行为（方法）的方式。通过将数据和行为组合在一个类中，你可以隐藏数据的实现细节，并提供一个清晰的接口来访问和操作数据。
- 如果你需要创建具有层次结构的对象（即子类继承父类的属性和方法），或者你需要支持不同的对象以不同的方式执行相同的操作（多态性）。
- 当你有多个对象需要相互交互，并且这些交互涉及复杂的逻辑和状态时，使用类可以更好地组织和管理这些交互。
- 如果设计一个大型的应用程序或系统，并且希望利用面向对象设计的优势（如模块化、可重用性、可扩展性等），那么使用类是合适的。
- 许多常见的软件设计模式（如工厂模式、单例模式、观察者模式等）都是基于类的。当你需要实现这些模式时，使用类可以简化代码结构并提高可维护性。
"""


st.markdown("[Pandas](https://cheat-sheet.cn/post/pandas-cheat-sheet/#pandas%E5%AE%89%E8%A3%85)")
# '### Pandas'
# 'Pandas 是一个强大的 Python 库，用于数据分析和数据处理。它提供了许多数据结构，如 Series（一维数组）和 DataFrame（二维表格），以及一系列用于数据清洗、转换、分析和可视化的方法。'
# '#### Series'
# 'Series 是一个一维的、标签化的数组，可以包含任何数据类型（整数、字符串、浮点数、Python 对象等）。'
# code = """
# s = pd.Series([1, 2, 3, 4, 5])
# print(s)
# """
# st.code(code, language="python")
#
# '#### DataFrame'
# 'DataFrame 是一个二维的、大小可变且可以包含异构类型列的表格结构。你可以从多种来源创建 DataFrame，例如列表、字典、CSV 文件等。'
# code = """
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Paris', 'London']
# }
# df = pd.DataFrame(data)
# print(df)
# """
# st.code(code, language="python")
#
# '#### 读取和写入文件'
# 'Pandas 支持多种文件格式，如 CSV、Excel、SQL 数据库等。'
# code ="""
# # 读取 CSV 文件
# df = pd.read_csv('data.csv')
# print(df)
#
# # 将 DataFrame 写入 CSV 文件
# df.to_csv('output.csv', index=False)
# """
# st.code(code, language="python")
