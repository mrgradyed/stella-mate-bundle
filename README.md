StellaMateBundle
==================

Handy actions for TextMate 2

This bundle contains some actions I wrote to ease my work in [TextMate 2](https://github.com/textmate/textmate) editor.

### CSSLintOnSave action
When editing a CSS file, pressing CMD+S causes the document to be analysed by [CSSLint](http://csslint.net/) and saved.
CSSLint output is formatted and printed in a window under the document, clicking on one of the listed problems causes the document to scroll to the related line.

### JSHintOnSave action
When editing a Javascript file, pressing CMD+S causes the document to be analysed by [JSHint](http://jshint.com/) and saved.
JSHint output is formatted and printed in a window under the document, clicking on one of the listed problems causes the document to scroll to the related line.

### Requirements
CSSLintOnSave requires [npm version of CSSLint](https://github.com/CSSLint/csslint/wiki/Command-line-interface) to be installed.
JSHintOnSave requires [npm version of JSHint](http://jshint.com/install/) to be installed.
Actions are Python scripts, so Python 2.7 (or 2.6, or 2.5) needs to be available.
The path, where csslint and jshint are, needs to be added to the PATH variable in the TextMate 2 preferences.
