# 安装 pip

https://www.runoob.com/w3cnote/python-pip-install-usage.html

```shell
# Python2.x 版本命令
pip --version

# Python3.x 版本命令
pip3 --version


 # 下载安装脚本
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# 运行安装脚本
sudo python3 get-pip.py

# 升级
pip install -U pip
sudo easy_install --upgrade pip

# 最新版本
pip install SomePackage

# 指定版本
pip install SomePackage==1.0.4

# 最小版本
pip install 'SomePackage>=1.0.4'

# Django
pip install Django==1.7


# 升级安装包
pip install --upgrade SomePackage

# 卸载安装包
pip uninstall SomePackage

# 搜索安装包
pip search SomePackage


# 显示安装包信息
pip show

# 列出已安装的包
pip list
```

## 代理设置

```bash
pip install pip -U
pipe3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 代理升级
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U



```

或者

```bash

vim /etc/profile：
    export http_proxy='http://代理服务器IP:端口号'
    export https_proxy='http://代理服务器IP:端口号'
source /etc/profile

```
