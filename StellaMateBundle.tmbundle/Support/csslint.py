#!/usr/bin/env python

# The MIT License (MIT)

# Copyright (c) 2014 Emiliano D'Alterio

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import commands

if commands.getstatusoutput('which csslint')[0] == 0:
    path_to_file = os.environ['TM_FILEPATH']
    result = commands.getoutput('csslint %s' % (path_to_file))

    dirty_messages = []
    messages = []
    error_lines = []
    general_warnings = []
    if result:
        file_name = os.environ['TM_FILENAME']
        dirty_messages = result.split(file_name)
        del dirty_messages[0:2]

        for dmsg in dirty_messages:
            line_start = dmsg.find('line')
            if line_start == -1:
                dmsg = dmsg[dmsg.find('warning'):]
                general_warnings.append(dmsg)
            else:
                messages.append(dmsg[line_start:])

        for msg in messages:
            error_line = re.search('\d+', msg)
            if error_line and msg.find('line') != -1:
                error_lines.append(error_line.group(0))

    style = '''
        div.container {
            border-bottom: 1px solid #a2a3a4;
        }
        div.link {
            background: #d2d3d4;
            border: 1px solid #a2a3a4;
            border-bottom: 0;
            padding:10px;
        }
        a {
            color: blue;
            text-decoration: none;
        }'''

    print '''<html><head><style>%s</style></head>
        <body><h3>csslint: %s errors</h3><div class="container">''' % (
        style, len(messages) + len(general_warnings))

    link = '''<div class="link">
        <a href="txmt://open?url=file://%s&line=%s">%s</a></div>'''

    for error_line, msg in zip(error_lines, messages):
        print link % (path_to_file, error_line, msg)

    for gen_warning in general_warnings:
        print '<div class="link"><span>%s</span></div>' % (gen_warning)

    print '</div></body></html>'

else:
    print 'CSSLint NOT found.'
