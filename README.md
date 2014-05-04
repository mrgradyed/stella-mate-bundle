StellaMateBundle
==================

Handy actions for TextMate 2

This bundle contains some actions I wrote to ease my work in TextMate 2.0 editor.

### CSSLintOnSave action
When editing a CSS file, pressing CMD+S causes the document to be analysed by CSSLint and saved.
CSSLint output is formatted and printed in a window under the document, clicking on one of the listed problems causes the document to scroll to the related line.

### JSHintOnSave action
When editing a Javascript file, pressing CMD+S causes the document to be analysed by JSHint and saved.
JSHint output is formatted and printed in a window under the document, clicking on one of the listed problems causes the document to scroll to the related line.

### Requirements
CSSLintOnSave requires npm version of CSSLint to be installed.
JSHintOnSave requires npm version of JSHint to be installed.
Actions are written in Python, so Python (2.7 or 2.6 or 2.5) needs to be installed and linked to the "python" command.
The path, where csslint and jshint are, needs to be added to the PATH variable in the TextMate 2 preferences.
