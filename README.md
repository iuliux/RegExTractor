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

```python
from main import extract

extract(['skull', 'school'])
```


Examples
--------

Each row shows a list of input strings and the RegEx generated from them.
The generated pattern always matches every input string, and generalizes to
match similar strings too.

| Input strings | Generated RegEx |
| --- | --- |
| `['skull', 'school']` | `s[a-z]{2}[a-z]{0,2}l[a-z]?` |
| `['<div></div>', '<span></span>']` | `<[a-z]{3}[a-z]?></[a-z]{3}[a-z]?>` |
| `['RFC 821', 'RFC 6409']` | `RFC\ [0-9]{3}[0-9]?` |
| `['abc$1250', 'xby#340', 'sbs@00000']` | ``[a-z]b[a-z][!@#$%^&*()_+=-`~'";:,<.>/?\\]}\[{][0-9]{0,3}0[0-9]{0,4}`` |

You can reproduce these (and a few more) by running the demos in `main.py`:

```sh
python3 main.py
```


TODO
----

- include word-boundries where present
