http://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/

另一个 yield 的例子来源于文件读取。如果直接对文件对象调用 read() 方法，会导致不可预测的内存占用
。好的方法是利用固定长度的缓冲区来不断读取文件内容。
通过 yield，我们不再需要编写读文件的迭代类，就可以轻松实现文件读取：

def read_file(fpath): 
    BLOCK_SIZE = 1024 
    with open(fpath, 'rb') as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
            if block: 
                yield block 
            else: 
                return
