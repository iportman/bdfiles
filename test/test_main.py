"""
    单元测试主文件

    ~~~~~~~~~
    暂时只支持Mac/Linux
    TODO: 支持Windows
"""
import os
import unittest
import main
import time
import shutil


class TestMain(unittest.TestCase):

    def setUp(self):
        save_dir = '/tmp/dbfiles/' + str(time.time_ns()) + '/'
        self.save_dir = save_dir

        if os.path.exists(save_dir):
            raise Exception(save_dir + ' already exists.')

        os.makedirs(save_dir)

    def test_main(self):
        save_dir = self.save_dir

        main.download(save_dir, True)

        conf_dict = main.get_conf(True)
        download_files = conf_dict['download_files']

        for file_name in download_files:
            self.assertTrue(os.path.exists(save_dir + file_name))
            print('assert: ' + file_name + ' download success.')

    def tearDown(self):
        shutil.rmtree(self.save_dir)
        print('Dir has been deleted. ' + self.save_dir)
        print('\nDone.')
