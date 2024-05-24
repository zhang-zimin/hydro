import streamlit as st



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


st.markdown('### 运算符')
st.markdown('运算符用于执行操作。Python 支持算术运算符（+、-、*、/）、比较运算符（==、!=、<、>、<=、>=）、逻辑运算符（and、or、not）和位运算符（&、|、^、~）。')
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

# 按位与
x = 10  # 0b1010
y = 5   # 0b0101

result = x & y
print(result)  # 输出：0b0000

# 按位或
x = 10  # 0b1010
y = 5   # 0b0101

result = x | y
print(result)  # 输出：0b1111

# 按位异或
x = 10  # 0b1010
y = 5   # 0b0101

result = x ^ y
print(result)  # 输出：0b1111

# 按位非
x = 10  # 0b1010

result = ~x
print(result)  # 输出：0b0101
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


st.markdown('### 模块和包')
st.markdown('在 Python 中，模块和包是组织代码的基本单元。模块是包含代码的文件，而包是包含模块的目录。使用模块和包可以提高代码的可重用性和可维护性。')
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
st.markdown('pip 是 Python 的包安装程序。它是大多数 Python 发行版中包含的标准工具。要使用 pip 安装包，请打开终端或命令提示符并运行以下命令：')
code = """
pip install package_name
"""
#
st.code(code, language="python")

st.markdown('### 流程控制')
st.markdown('Python 的流程控制语句用于控制程序的执行顺序。它们使您可以根据条件执行不同的代码块，循环重复代码以及处理错误。')
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



