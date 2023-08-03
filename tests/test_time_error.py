from lib.TimeError import *
from unittest.mock import Mock

def test_get_server_time():
    req_mock = Mock()
    time_mock = Mock()
    resp_mock = Mock()
    req_mock.get.return_value = resp_mock
    time_mock.time.return_value = 5666
    resp_mock.json.return_value = {"abbreviation":"BST","client_ip":"82.163.117.26","datetime":"2023-08-03T11:12:57.280239+01:00","day_of_week":4,"day_of_year":215,"dst":True,"dst_from":"2023-03-26T01:00:00+00:00","dst_offset":3600,"dst_until":"2023-10-29T01:00:00+00:00","raw_offset":0,"timezone":"Europe/London","unixtime":1691057577,"utc_datetime":"2023-08-03T10:12:57.280239+00:00","utc_offset":"+01:00","week_number":31}
    time_error = TimeError(req_mock, time_mock)
    assert time_error._get_server_time() == 1691057577

def test_get_error():
    req_mock = Mock()
    time_mock = Mock()
    resp_mock = Mock()
    req_mock.get.return_value = resp_mock
    time_mock.time.return_value = 1691058772.368284
    resp_mock.json.return_value = {"abbreviation":"BST","client_ip":"82.163.117.26","datetime":"2023-08-03T11:12:57.280239+01:00","day_of_week":4,"day_of_year":215,"dst":True,"dst_from":"2023-03-26T01:00:00+00:00","dst_offset":3600,"dst_until":"2023-10-29T01:00:00+00:00","raw_offset":0,"timezone":"Europe/London","unixtime":1691057577,"utc_datetime":"2023-08-03T10:12:57.280239+00:00","utc_offset":"+01:00","week_number":31}
    time_error = TimeError(req_mock, time_mock)
    assert time_error.error() == (1691057577 - 1691058772.368284)