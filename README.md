StellaMateBundle
==================

Handy actions for TextMate 2

This bundle contains some actions I wrote to ease my work in [TextMate 2](https://github.com/textmate/textmate) editor.

### Actions
* #### CSSLintOnSave
When editing a CSS file, pressing CMD+S causes the document to be analysed by [CSSLint](http://csslint.net/) and saved.
CSSLint output is converted to HTML and presented nicely in a new window. Clicking on one of the listed problems causes the document to scroll to the related line.

* #### JSHintOnSave
When editing a Javascript file, pressing CMD+S causes the document to be analysed by [JSHint](http://jshint.com/) and saved.
JSHint output is converted to HTML and presented nicely in a new window. Clicking on one of the listed problems causes the document to scroll to the related line.

### Requirements
* CSSLintOnSave requires [npm version of CSSLint](https://github.com/CSSLint/csslint/wiki/Command-line-interface) to be installed.
* JSHintOnSave requires [npm version of JSHint](http://jshint.com/install/) to be installed.
* Actions are Python scripts, so Python 2.7 (or 2.6, or 2.5) needs to be available (Python comes pre-installed on Mac OS X).
* **The path**, where csslint and jshint scripts are, needs to be added to the PATH variable in the TextMate 2 preferences under the '*Variables*' tab (e.g. '*/usr/local/bin*').

### Installation
**If TextMate 2 is installed**, just double-click "StellaMateBundle.tmbundle".

### Screenshots
![csslint in action screenshot](https://raw.githubusercontent.com/mrgradyed/stella-mate-bundle/master/csslint_check.png)
![jshint in action screenshot](https://raw.githubusercontent.com/mrgradyed/stella-mate-bundle/master/jshint_check.png)

### License
The MIT License (MIT)

Copyright (c) 2014 Emiliano D'Alterio

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.**



- - -
[www.cocoadrops.com](http://www.cocoadrops.com/)
