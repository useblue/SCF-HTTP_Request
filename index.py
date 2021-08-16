# -*- coding: utf8 -*-
import os

from wx import wx

def main_handler(event, context):
    
    SESSIONDATA = os.environ.get('SESSIONDATA')

    wx(SESSIONDATA).run()

    return 'DONE'