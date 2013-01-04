lessc.py
========

Convenience operations for lessc in Python. _Very_ lightweight and intended to be used solely for convenience purposes.

Compiling LESS
---

Use `python lessc.py <name>` to compile `<name>.less` into `<name>.css`. Useful when you're working with a lot of different LESS files via command line and don't want to type out both filenames over and over.

Lessc.py uses the command `lessc` by default. If you do not have `lessc` in your path, you can use `python lessc.py -p /path/to/lessc <name>` to compile `<name>.less` into `<name>.css`.