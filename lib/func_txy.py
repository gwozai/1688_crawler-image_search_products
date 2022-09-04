# !/usr/bin/python
# -*- coding: utf-8 -*-


import time
import random
import string
import requests
import contextlib


def request_post(url, params=None, data=None, files={}, headers={}, timeout=10, cookies=None):
    with contextlib.closing(
            requests.post(
                url=url,
                params=params,
                data=data,
                files=files,
                headers=headers,
                cookies=cookies,
                timeout=timeout
            )
    ) as req:
        return req


def request_get(url, params, headers, timeout=10, cookies=None):
    with contextlib.closing(
            requests.get(
                url=url,
                params=params,
                headers=headers,
                cookies=cookies,
                timeout=timeout
            )
    ) as req:
        return req


def get_random_str(k):
    return ''.join(random.choices(string.ascii_letters, k=k))


def get_random_digits(k):
    return ''.join(random.choices(string.digits, k=k))


def now():
    return int(time.time() * 1000)
