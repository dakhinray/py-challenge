import unittest
import metrichor_challenge
import sys
import os
import shutil
from io import StringIO
from contextlib import contextmanager
import time

try:
    # python 3.4+ should use builtin unittest.mock not mock package
    from unittest.mock import patch
except ImportError:
    from mock import patch

from metrichor_challenge import logging

# Context manager to capture output of the test and revert back
@contextmanager
def capture(command, *args, **kwargs):
  out, sys.stdout = sys.stdout, StringIO()
  try:
    command(*args, **kwargs)
    sys.stdout.seek(0)
    yield sys.stdout.read()
  finally:
    sys.stdout = out

logbuffer = []
def myinfo(msg):
    logbuffer.append('INFO : ' + msg + '\n')

def myerror(err):
    logbuffer.append('ERROR : ' + str(err) + '\n')

class MyTestCase(unittest.TestCase):

    def test_case1(self):
        '''
        test with no matching filename
        :return: 0
        '''
        #log = logging.getLogger('Temp')
        path = './data'
        filePath = path + '/temp'

        if os.path.exists(path):
            shutil.rmtree(path)
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            self.assertTrue(False,'Should not be here, folder should not exist!')
        with open(filePath, 'w') as f:
            f.write('{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1459, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}'+
                    '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "db367858-24f8-46ec-b352-08cdf5388ad4", "seqlen": 1177, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.995, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}'+
                    '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853966, "read_id": "723b1945-74c3-40b3-a76a-ff6d6b3f8203", "seqlen": 1084, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.968, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}')
        testargs = ["metrichor_challenge.py", '-q', path]
        with patch.object(sys, 'argv', testargs):
            with capture(metrichor_challenge.main) as output:
                #log.warning( "jay ******************** : {}".format(output))
                self.assertEqual(str(output).strip(), '0')
        if os.path.exists(filePath):
            os.remove(filePath)
        if os.path.exists(path):
            shutil.rmtree(path)

    def test_case2(self):
        '''
        test with one matching filename and -q
        :return: 6
        '''
        #log = logging.getLogger('Temp')
        path = './data'
        filePath = path + '/temp.data.json'

        if os.path.exists(path):
            shutil.rmtree(path)
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            self.assertTrue(False, 'Should not be here, folder should not exist!')
        with open(filePath, 'w') as f:
            f.write(
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}\n' +
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "db367858-24f8-46ec-b352-08cdf5388ad4", "seqlen": 2, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.995, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}\n' +
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853966, "read_id": "723b1945-74c3-40b3-a76a-ff6d6b3f8203", "seqlen": 3, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.968, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}\n')
        testargs = ["metrichor_challenge.py", '-q', path]
        with patch.object(sys, 'argv', testargs):
            with capture(metrichor_challenge.main) as output:
                #log.warning("jay ******************** : {}".format(output))
                self.assertEqual(str(output).strip(), '6')
        if os.path.exists(filePath):
            os.remove(filePath)
        if os.path.exists(path):
            shutil.rmtree(path)

    def test_case3(self):
        '''
        test with one matching filename and no -q
        :return: 6
        '''
        #log = logging.getLogger('Temp')
        path = './data'
        filePath = path + '/temp.data.json'

        if os.path.exists(path):
            shutil.rmtree(path)
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            self.assertTrue(False, 'Should not be here, folder should not exist!')
        with open(filePath, 'w') as f:
            f.write(
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}\n' +
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "db367858-24f8-46ec-b352-08cdf5388ad4", "seqlen": 2, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.995, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}\n' +
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853966, "read_id": "723b1945-74c3-40b3-a76a-ff6d6b3f8203", "seqlen": 3, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.968, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}\n')
        testargs = ["metrichor_challenge.py", path]
        with patch.object(sys, 'argv', testargs):
            with capture(metrichor_challenge.main) as output:
                #log.warning("jay ******************** : {}".format(output))
                self.assertEqual(str(output).strip(), '6')
        if os.path.exists(filePath):
            os.remove(filePath)
        if os.path.exists(path):
            shutil.rmtree(path)

    def test_case4(self):
        '''
        test with one matching filename and no -q and no path
        :return: 6
        '''
        #log = logging.getLogger('Temp')
        path = './data'
        filePath = path + '/temp.data.json'

        if os.path.exists(path):
            shutil.rmtree(path)
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            self.assertTrue(False, 'Should not be here, folder should not exist!')
        with open(filePath, 'w') as f:
            f.write(
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}\n' +
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "db367858-24f8-46ec-b352-08cdf5388ad4", "seqlen": 2, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.995, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}\n' +
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853966, "read_id": "723b1945-74c3-40b3-a76a-ff6d6b3f8203", "seqlen": 3, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.968, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}\n')
        testargs = ["metrichor_challenge.py"]
        with patch.object(sys, 'argv', testargs):
            with capture(metrichor_challenge.main) as output:
                #log.warning("jay ******************** : {}".format(output))
                self.assertEqual(str(output).strip(), '6')
        if os.path.exists(filePath):
            os.remove(filePath)
        if os.path.exists(path):
            shutil.rmtree(path)

    def test_case5(self):
        '''
        test with one matching filename and -v and no path
        :return: 6
        '''
        #log = logging.getLogger('Temp')
        path = './data'
        filePath = path + '/temp.data.json'

        if os.path.exists(path):
            shutil.rmtree(path)
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            self.assertTrue(False, 'Should not be here, folder should not exist!')
        with open(filePath, 'w') as f:
            f.write(
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}\n' +
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "db367858-24f8-46ec-b352-08cdf5388ad4", "seqlen": "xx", "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.995, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}\n' +
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853966, "read_id": "723b1945-74c3-40b3-a76a-ff6d6b3f8203", "seqlen": 3, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.968, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}\n')
        testargs = ["metrichor_challenge.py", "-v"]
        with patch.object(sys, 'argv', testargs):
            stream = StringIO()
            x = logging.getLogger('metrichor_challenge')
            x.addHandler(logging.FileHandler("tmp.txt",'a'))
            with patch.multiple(logging,info=myinfo,error=myerror):
                with capture(metrichor_challenge.main) as output:
                    self.assertEqual(logbuffer.pop(0).strip(),'INFO : Processing file '+filePath.replace('/','\\'))
                    self.assertEqual(logbuffer.pop(0).strip(),'ERROR : invalid literal for int() with base 10: \'xx\'')
                    self.assertEqual(logbuffer.pop(0).strip(),'INFO : Skiping line because of above error.')
                    self.assertEqual(logbuffer.pop(0).strip(),'INFO : Total for file: '+filePath.replace('/','\\')+' is 4')
                    self.assertEqual(logbuffer.pop(0).strip(), 'INFO : Total : 4')
        if os.path.exists(filePath):
            os.remove(filePath)
        if os.path.exists(path):
            shutil.rmtree(path)


if __name__ == '__main__':
    unittest.main()

