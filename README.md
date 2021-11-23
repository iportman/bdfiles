# Batch download files

Download files in batches to the specified directory by config file.

通过配置可以批量下载文件到指定目录

## Installation

Generate requirements.txt 
```sh
pipreqs --force .
```
Install all packages listed in the file
```sh
pip install -r requirements.txt
```

## Generate executable file

```sh
pyinstaller -F -n dbfiles_v0.0.1.exe --distpath . main.py
```