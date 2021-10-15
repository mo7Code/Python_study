# python 的文件头

```py

#!/usr/bin/python3

```

## 指令

```bash
# 查看当前版本
python -V

# 安装python3
brew install python3

# 查看python的路径
which python


# 退出 py 终端
 exit()
```

## 打包

```bash
# 源码压缩包 生成dist文件
python3 setup.py sdist

# 二进制发布包 结果不包括setup.py的二进制文件
python3 setup.py bdist

# --formats=zip,tar 压缩成成不同格式的源文件
python3 setup.py sdist

#.egg格式
python3 setup.py bdist_egg

# .whl格式
python3 setup.py bdist_wheel

# windows下面的文件exe
python3 setup.py bdist_wininst

```
