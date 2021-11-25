# 批量下载文件

通过配置可以批量下载文件到指定目录

## 下载和运行 (Mac or Linux)

```sh
# 克隆源代码
git clone git@github.com:iportman/bdfiles.git
cd bdfiles
# 进入虚拟环境（可选）
source venv/bin/activate
# 安装依赖
pip install -r requirements.txt
# 运行
python main.py
```

# 依赖列表写入 requirements.txt 
```sh
pipreqs --force .
```

## 生成Windows可执行文件

```sh
pyinstaller -F -n dbfiles_v0.0.1.exe --distpath . main.py
```

## 配置文件

配置文件conf.yml必须和运行文件(.exe or main.py)在同一目录

配置如下

- save_dir:          下载文件要保存的目录
- download_url_path: 下载URL的路径前缀，除了最后的文件名
- download_files:    URL最后的文件名，支持多个文件名
