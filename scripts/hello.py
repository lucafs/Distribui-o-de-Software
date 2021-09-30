#!/usr/bin/env python3
from dev_aberto import hello
from babel.dates import format_datetime
import gettext


gettext.install('cli',localedir='locale')

if __name__ == '__main__':
    date, name = hello()
    date = format_datetime()
    print(_('Último commit feito em:'), date, _(' por'), name)
