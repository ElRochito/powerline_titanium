from __future__ import absolute_import
from subprocess import Popen, PIPE
from powerline.theme import requires_segment_info

import os
import sys
import subprocess
import commands
from xml.dom import minidom

@requires_segment_info
def version(pl, segment_info):
    #sys.path.insert(1, '/Users/julien/.config/bin')
    #print sys.path
    try:
        if os.path.isfile("tiapp.xml") == False:
            return None

        status, alloy_version = commands.getstatusoutput("alloy --version")

        xmldoc = minidom.parse('tiapp.xml')
        itemlist = xmldoc.getElementsByTagName('sdk-version')

        tiversion = itemlist[0].childNodes[0].data

        if tiversion != '':
            return [{
                'contents': str(tiversion) + ' | ' + str(alloy_version),
                'highlight_groups': ['version']
            }]
        else:
            return None

    except OSError as e:
        if e.errno == 2:
            pass
        else:
            raise
