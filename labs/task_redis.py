#!/usr/bin/env python
# -*- coding: utf-8 -*-


import redis


REDIS_CLIENT = redis.Redis()


def single_one(function=None, key="", timeout=None):
    def _dec(run_func):
        def _caller(*args, **kwargs):
            ret_value = None
            have_lock = False
            lock = REDIS_CLIENT.lock(key, timeout=timeout)
            try:
                have_lock = lock.acquire(blocking=False)
                if have_lock:
                    ret_value = run_func(*args, **kwargs)
            finally:
                if have_lock:
                    lock.release()
            return ret_value
        return _caller
    return _dec(function) if function is not None else _dec
