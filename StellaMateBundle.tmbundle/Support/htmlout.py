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

style = '''
    .container {
        border-bottom: 1px solid lightgray;
    }
    .bigtitle {
        font-size: 20px;
        color: sienna;
    }
    .msg {
        height: 8%;
        background: mistyrose;
        border: 1px solid lightgray;
        border-bottom: 0;
        padding: 2%;
    }
    .W, .warning, .E, .error {
        float: left;
        width: 3%;
        height: 100%;
        margin-right: 5%;
    }
    .W, .warning {
        background: orange;
    }
    .E, .error {
        background: red;
    }
    a {
        color: navy;
        text-decoration: none;
    }
    span
    {
       color: navy;
    }
    .linkdiv {
        height: 100%;
    }
    .evidencespan
    {
        font-style: italic;
        margin-left: 30px;
    }'''


def printHeader(msg, file_path=''):
    msg = escapeForHTML(msg)
    file_path = escapeForHTML(file_path)

    print '''<html><head><style>%s</style></head>
                <body><h1 class="bigtitle">%s %s</h1>
                    <div class="container">''' % (style, msg, file_path)


def printFooter():
    print '</div></body></html>'


def printErrorMsg(file_path, line, char, reason, evidence, severity):
    file_path = escapeForHTML(file_path)
    reason = escapeForHTML(reason)
    evidence = escapeForHTML(evidence)

    print '''
        <div class="msg">
            <div class="%s"></div>
            <div class="linkdiv">''' % (severity)

    if line:
        print '''<a href="txmt://open?url=file://%s&line=%s&column=%s">
                    At line %s: %s <br /><br />
                    <span class="evidencespan">%s</span>
                </a>
            </div>
        </div>''' % (file_path, line, char, line, reason, evidence)
    else:
        print '''<span>General warning: %s <br /><br />
                    <span class="evidencespan">%s</span>
                </span>
            </div>
        </div>''' % (reason, evidence)


def escapeForHTML(string):
    return string.replace(
        '&', '&amp;').replace(
        '"', '&quot;').replace(
        "'", '&apos;').replace(
        '>', '&gt;').replace(
        '<', '&lt;')
