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
import commands as COM
import xml.etree.ElementTree as ET
import htmlout as HO

(csslint_status, csslint_path) = COM.getstatusoutput('which csslint')
file_path = os.environ['TM_FILEPATH']

if csslint_status != 0:
    HO.printHeader('Error: csslint NOT FOUND.')
elif os.stat(file_path).st_size == 0:
    HO.printHeader('Error: FILE IS EMPTY.')
else:
    xmlOutput = COM.getoutput(
        '%s --format=csslint-xml %s' % (csslint_path, file_path))
    root = ET.fromstring(xmlOutput)
    file = root.find('file')

    if file is None:
        HO.printHeader('csslint: No errors in ', file_path)
    else:
        root = ET.fromstring(xmlOutput)
        file = root.find('file')
        issues = file.findall('issue')

        HO.printHeader('csslint: There are problems in ', file_path)

        for i in issues:
            HO.printErrorMsg(file_path, i.get('line'),
                             i.get('char'), i.get('reason'),
                             i.get('evidence'), i.get('severity'))

HO.printFooter()
