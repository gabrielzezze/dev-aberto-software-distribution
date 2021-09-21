#!/usr/bin/env python3
import datetime
import babel.dates
from dev_aberto import hello
import gettext

if __name__ == "__main__":
    gettext.install("cli", localedir="locale")
    date, name = hello()
    date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").date()
    print(_("Last commit at:"), babel.dates.format_datetime(date), _(" by"), name)
