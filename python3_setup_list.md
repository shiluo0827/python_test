//本环境中，已经配置好了apt的国内源，所以apt的下载速度是比较快的。可以不用多做配置。
//如果无法找到包，可以更新一下apt,  "bash:apt-get update"  或升级 apt "apt-get upgrade"

//安装python3
sudo apt-get install python3

//安装pip3
sudo apt-get install python3-pip

//这里下载的可能是pip 9的版本，所以可以指定下载版本，或者升级pip
python -m pip install --upgrade pip
sudo apt-get install python3-pip==20.1

//pip3 配置国内源，这里设置为清华大学的pip源
pip3 config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple
//pip config --help 可以查看配置文件的相关帮助，pip --help 可以查看pip命令帮助
