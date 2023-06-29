import os

'''
1. 有两个同名模块默认只能导入其中一个
   访问两个同名的文件，分别放入子目录中，
2. 选择在路径 sys.path 最左边的那一项
3. 顶层脚本的主目录总是模块搜索路径中的第一项
4. 程序主目录（或是模块路径中考前的里一个目录）下的本地模块会隐藏和体会标准库模块

代码中的语句次序：
1. 当模块首次被导入（重载）时,Python会从头到尾执行他的语句, 前向引入(forward reference)细节：
    导入时，模块文件顶部程序代码(不再函数内),在Python运行到时会立刻执行,因此这些语句无法引用文件底部位置赋值的变量名
    位于函数体中的代码知道函数被调用后才会执行,因为函数内的变量名在函数实际执行前都不会被解析，所有在函数体中常常可以引用文件中任意位置的变量。


From 复制名称，而不是链接：
1. from语句在导入者的作用域内对名称赋值,也就是名称赋值运算，不是名称的别名机制；
它的韩语和Python所有赋值运算都一样，但考虑到共用对象的代码位于不同文件中，因此from语句会更加微妙；

reload 不能作用于from导入：
因为from会在执行时复制(赋值)名称，所有不会链接到名称所在的模块，通过from导入的名称就直接称为对象引用；

正是由于这种行为，重载被导入模块模块不能作用于通过from导入模块名称的程序，即：客户端的名称依然引用了
通过from取出的原始对象即使原始模块中的名称之后进行了重置；
'''


import tkinter
os.popen('xxxx.py',tkinter).read()