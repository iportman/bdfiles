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

## Generate Windows executable file

```sh
pyinstaller -F -n dbfiles_v0.0.1.exe --distpath . main.py
```

## Config File

The configuration file conf.yml must be in the same directory as the running file (.exe or main.py)

configuration as follows

- save_dir: The directory that you want to save
- download_url_path: The path prefix of the download URL, except for the last file name
- download_files: The last file name of the url, supports multiple file names
