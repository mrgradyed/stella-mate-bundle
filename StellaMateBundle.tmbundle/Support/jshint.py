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

(jshint_status, jshint_path) = commands.getstatusoutput('which jshint')

if jshint_status != 0:
    print 'CSSLint NOT found.'

else:
    file_path = os.environ['TM_FILEPATH']
    result = commands.getoutput(
        '%s %s' % (jshint_path, file_path))

    if result:
        result = result.replace('&', '&amp;').replace('"', '&quot;').replace(
            "'", '&apos;').replace('>', '&gt;').replace('<', '&lt;')

        messages = result.split(file_path)
        number_of_errors = [
            int(s) for s in messages[-1].split() if s.isdigit()][-1]
        first_message = 'jshint: There are %s problems in %s' % (
            number_of_errors, file_path)

        style = '''
            .container {
                border-bottom: 1px solid lightgray;
            }
            .link {
                background: lavender;
                border: 1px solid lightgray;
                border-bottom: 0;
                padding:20px;
            }
            a {
                color: navy;
                text-decoration: none;
            }'''

        header = '''<html><head><style>%s</style></head><body>
            <h3>%s</h3><div class="container">''' % (style, first_message)

        link = '''<div class="link">
            <a href="txmt://open?url=file://%s&line=%s">%s</a></div>'''

        footer = '</div></body></html>'

        print header

        for msg in messages:
            line_start = msg.find('line ')
            if line_start != -1:
                msg = msg[line_start:]
                error_line = re.search('\d+', msg)
                if error_line:
                    print link % (file_path, error_line.group(0), msg)

        print footer
