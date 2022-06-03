# PPSUC_WIKI_WEB

> PPSUC的WIKI

## GitToSphinx

为了生成可被[readthedocs](https://readthedocs.org/)读取的文件而手撕的一个翻译器

~~（类似于将一般的文件夹编译为可被read the docs读取的文件夹）~~

[readthedocs入门](https://blog.csdn.net/lu_embedded/article/details/109006380)

现在只考虑了三种文件情况：文件夹，markdown文件，非markdown非文件夹文件，将这三种文件按照规则分别写在rst文件内部

### 主代码

 - dirTools.py：文件夹操作
 - mkRST.py：写入rst文档，用于控制目录
 - pointer_main.py：定义文件指针对象，且控制文档的递归读取和生成

### 使用

 - step1：修改源文件
 - step2：保证编译文件存放地址是一个空文件夹
 - step3：在pointer_main.py中指定源文件地址和编译文件存放地址，然后运行此份代码即可