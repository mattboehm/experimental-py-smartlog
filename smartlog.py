#!/usr/bin/env python
#!/usr/bin/env python

"""logging utilities"""

import functools
import logging
import time
import traceback
import sys


FORMAT = """%(asctime)s,%(msecs)03d %(levelname)-5.5s [%(name)s] <<;
 %(message)s 
 ;>>"""
DATEFMT = "%H:%M:%S"
LEVEL = logging.DEBUG

def config_logging(**kwargs):
    """configure logging. takes same args as logging.basicConfig"""
    kwargs["format"] = kwargs.get("format", FORMAT)
    kwargs["datefmt"] = kwargs.get("datefmt", DATEFMT)
    kwargs["level"] = kwargs.get("level", LEVEL)
    logging.basicConfig(**kwargs)

def log_call(logger=None, log_result=True, log_exceptions=True, log_params=True):
    """decorator to log function calls and start/stop times to `logger`"""
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            """wrapper method that logs function calls"""
            log = logger or logging.getLogger(func.__module__)
            log.debug(u"<<: Call {fname}(args={args}, kwargs={kwargs}) ".format(fname=func.__name__, args=args if log_params else u'<suppressed>', kwargs=kwargs if log_params else u'<suppressed>'))
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                if log_result:
                    log.debug(u":>> Ret  {fname} ({time:.5f}s) result = {result}".format(fname=func.__name__, time=time.time() - start_time, result=result))
                else:
                    log.debug(u":>>")
                return result
            except Exception, err:
                msg = u":>> ERR! {fname}\n{trace}".format(fname=func.__name__, trace=traceback.format_exc() if log_exceptions else '')
                log.error(msg)
                raise err, None, sys.exc_info()[2]
        return inner
    return wrapper

