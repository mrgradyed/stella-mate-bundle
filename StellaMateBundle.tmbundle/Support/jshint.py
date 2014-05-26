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
import htmlcss

(jshint_status, jshint_path) = commands.getstatusoutput('which jshint')
file_path = os.environ['TM_FILEPATH']

if jshint_status != 0:
    print htmlcss.header % (htmlcss.style, 'Error: jshint NOT FOUND.')
    print htmlcss.footer
elif os.stat(file_path).st_size == 0:
    print htmlcss.header % (htmlcss.style, 'Error: FILE IS EMPTY.')
    print htmlcss.footer
else:
    result = commands.getoutput(
        '%s %s' % (jshint_path, file_path))
    if not result:
        print htmlcss.header % (
            htmlcss.style, 'jshint: No errors in %s') % file_path
        print htmlcss.footer
    else:
        result = result.replace('&', '&amp;').replace('"', '&quot;').replace(
            "'", '&apos;').replace('>', '&gt;').replace('<', '&lt;')

        messages = result.split(file_path)

        if messages[0].find('ERROR') != -1:
            first_message = 'jshint%s' % (messages[0][messages[0].find(':'):])
        else:
            first_message = 'jshint: There are problems in %s' % (file_path)

        print htmlcss.header % (htmlcss.style, first_message)

        for msg in messages:
            line_start = msg.find('line ')
            if line_start != -1:
                msg = msg[line_start:]
                error_line = re.search('\d+', msg)
                if error_line:
                    print htmlcss.linkmsg % (
                        file_path, error_line.group(0), msg)

        print htmlcss.footer
