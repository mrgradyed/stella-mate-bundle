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

(csslint_status, csslint_path) = commands.getstatusoutput('which csslint')
file_path = os.environ['TM_FILEPATH']

if csslint_status != 0:
    print htmlcss.header % (htmlcss.style, 'Error: csslint NOT FOUND.')
    print htmlcss.footer
elif os.stat(file_path).st_size == 0:
    print htmlcss.header % (htmlcss.style, 'Error: FILE IS EMPTY.')
    print htmlcss.footer
else:
    result = commands.getoutput(
        '%s --format=text %s' % (csslint_path, file_path))

    if result:
        result = result.replace('&', '&amp;').replace('"', '&quot;').replace(
            "'", '&apos;').replace('>', '&gt;').replace('<', '&lt;')

        file_name = os.environ['TM_FILENAME']
        messages = result.split(file_name)
        first_message = '%s%s' % (messages[0], file_name)

        print htmlcss.header % (htmlcss.style, first_message)

        for msg in messages:
            line_start = msg.find('line ')
            if line_start != -1:
                msg = msg[line_start:]
                error_line = re.search('\d+', msg)
                if error_line:
                    print htmlcss.linkmsg % (
                        file_path, error_line.group(0), msg)
            else:
                warning_start = msg.find('warning')
                if warning_start != -1:
                    print htmlcss.othermsg % (msg[warning_start:])

        print htmlcss.footer
