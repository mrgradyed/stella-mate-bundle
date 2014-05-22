#!/usr/bin/env python

# The MIT License (MIT)

# Copyright (c) 2014 Emiliano D'Alterio

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

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

if commands.getstatusoutput('which jshint')[0] == 0:
    path_to_file = os.environ['TM_FILEPATH']
    result = commands.getoutput('jshint %s' % (path_to_file))

    messages = []
    line_numbers = []
    if result:
        messages = result.replace(path_to_file+': ', '').split('\n')
        last_msg = messages[-1]
        del messages[-1]
        for msg in messages:
            line_number = re.search('\d+', msg)
            if line_number:
                line_numbers.append(line_number.group(0))
    else:
        last_msg = '0 errors'

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
        <body><h3>jshint: %s</h3><div class="container">''' % (style, last_msg)

    link = '<div class="link"><a href="txmt://open?url=file://%s&line=%s">%s</a></div>'
    for line_number, msg in zip(line_numbers, messages):
        print link % (path_to_file, line_number, msg)

    print '</div></body></html>'

else:
    print 'JSHint NOT found.'
