# Batch download files

Download files in batches to the specified directory by config file.

## Download & Run (Mac or Linux)

```sh
# clone source code
git clone git@github.com:iportman/bdfiles.git
cd bdfiles
# enter venv env (Optional)
source venv/bin/activate
# install requirements
pip install -r requirements.txt
# run
python main.py
```

# write into requirements.txt 
```sh
pipreqs --force .
```

## generate Microsoft Windows executable file

```sh
pyinstaller -F -n dbfiles_v0.0.1.exe --distpath . main.py
```

## Config File

The configuration file conf.yml must be in the same directory as the running file (.exe or main.py)

configuration as follows

- save_dir:          The directory that you want to save
- download_url_path: The path prefix of the download URL, except for the last file name
- download_files:    The last file name of the url, supports multiple file names