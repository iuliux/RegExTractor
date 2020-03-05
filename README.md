RegExTractor
============

Python regex extractor (list of strings => Regex)

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/iuliux/RegExTractor?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Description
-----------

Takes 2 or more strings (or even a single one) and generates a RegEx that
matches similar strings.
The generated RegEx always matches the original strings, but it also
generalizes, usually matching more.

Usage
-----

First of all, you can run the demos found in `main.py` (in the `if __main__` part).

The main function is `extract(strs)` from `main.py` that takes a list of strings and returns a string representing
the generated regex.


TODO
----

- include word-boundries where present
