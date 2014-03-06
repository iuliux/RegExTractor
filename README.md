RegExTractor
============

<img align="right" src="http://www.iuliux.ro/images/tractor_silhouette.png" width="150px" />
Python regex extractor (list of strings => Regex)

Description
-----------

Takes 2 or more strings (or even a single one) and generates a RegEx that
matches similar strings.
The generated RegEx always matches the original strings, but it also
generalizes, usually matching more.

Iulius Curt, 2014

Usage
-----

First of all, you can run the demos found in `main.py` (in the `if __main__` part).

The main function is `extract(strs)` from `main.py` that takes a list of strings and returns a string representing
the generated regex.

Demo
----

`TODO`


TODO
----

- include word-boundries where present
