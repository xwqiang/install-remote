install from github

### 1. install from github
eg. 

pip install git+https://github.com/xwqiang/install-remote.git@main


### 2. install from source code

eg.
git clone https://github.com/xwqiang/install-remote.git
cd install-remote
python3 -m venv .venv
./.venv/bin/python -m pip install -e .

其中 -e 理解为 editable，修改本地文件，调用的模块以最新文件为准。
