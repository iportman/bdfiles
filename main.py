"""
    Batch download files main
"""

import requests
import yaml
import os
import time


def download(save_dir=None, is_test=False):
    # load config file
    conf_dict = get_conf(is_test)

    # get config info
    if save_dir is None:
        save_dir = conf_dict['save_dir']

    download_url_path = conf_dict['download_url_path']
    download_files = conf_dict['download_files']

    # create dir
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # download files
    for file_name in download_files:
        download_url = download_url_path + file_name
        print('download url: ' + download_url)

        r = requests.get(download_url, verify=False)
        with open(save_dir + file_name, 'wb') as f:
            f.write(r.content)

        print(file_name + ' download success.')

    print('all files download success!')

    if not is_test:
        print('program exit after 5 seconds...')
        time.sleep(5)


def get_conf(is_test=False):
    conf_file_name = os.sep + 'conf.yml'
    if is_test:
        conf_file_name = os.sep + '..' + conf_file_name

    conf_file_path = os.getcwd() + conf_file_name
    if not os.path.exists(conf_file_path):
        raise Exception('config file does not exists.')

    conf_file = open(conf_file_path, 'r')
    conf_data = conf_file.read()
    conf_file.close()

    return yaml.safe_load(conf_data)


if __name__ == "__main__":
    download()
