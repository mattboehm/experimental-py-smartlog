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

