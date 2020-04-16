import unittest
import metrichor_challenge
import sys
import os
import shutil
from io import StringIO
from contextlib import contextmanager

try:
    # python 3.4+ should use builtin unittest.mock not mock package
    from unittest.mock import patch
except ImportError:
    from mock import patch



def test_parse_args():
    testargs = ["prog", "-f", "/home/fenton/project/setup.py"]
    with patch.object(sys, 'argv', testargs):
        setup = get_setup_file()
        assert setup == "/home/fenton/project/setup.py"

import logging





@contextmanager
def capture(command, *args, **kwargs):
  out, sys.stdout = sys.stdout, StringIO()
  try:
    command(*args, **kwargs)
    sys.stdout.seek(0)
    yield sys.stdout.read()
  finally:
    sys.stdout = out


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        log = logging.getLogger('Temp')
        path = './data'
        filePath = path + '/temp'

        if os.path.exists(path):
            shutil.rmtree(path)
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            self.assertTrue(False,'Should not be here, folder should not exist!')
        filePath = path + '/temp'
        with open(filePath, 'w') as f:
            f.write('{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1459, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}'+
                    '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "db367858-24f8-46ec-b352-08cdf5388ad4", "seqlen": 1177, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.995, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}'+
                    '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853966, "read_id": "723b1945-74c3-40b3-a76a-ff6d6b3f8203", "seqlen": 1084, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.968, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}')
        testargs = ["prog", '-q']
        with patch.object(sys, 'argv', testargs):
            with capture(metrichor_challenge.main) as output:
                print(output)
                log.warning( "jay ******************** : {}".format(output))
        if os.path.exists(filePath):
            os.remove(filePath)
        if os.path.exists(path):
            shutil.rmtree(path)

    def test_case2(self):
        log = logging.getLogger('Temp')
        path = './data'
        filePath = path + '/temp.data.json'

        if os.path.exists(path):
            shutil.rmtree(path)
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            self.assertTrue(False, 'Should not be here, folder should not exist!')
        filePath = path + '/temp'
        with open(filePath, 'w') as f:
            f.write(
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "314309c0-09de-4291-a5e4-0ea288db74f3", "seqlen": 1, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 10.377, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}' +
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "db367858-24f8-46ec-b352-08cdf5388ad4", "seqlen": 2, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.995, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}' +
                '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853966, "read_id": "723b1945-74c3-40b3-a76a-ff6d6b3f8203", "seqlen": 3, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.968, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}')
        testargs = ["prog", '-q']
        with patch.object(sys, 'argv', testargs):
            with capture(metrichor_challenge.main) as output:
                print(output)
                log.warning("jay ******************** : {}".format(output))
        if os.path.exists(filePath):
            os.remove(filePath)
        if os.path.exists(path):
            shutil.rmtree(path)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("SomeTest.testSomething").setLevel(logging.DEBUG)
    unittest.main()
