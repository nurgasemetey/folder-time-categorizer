#!/usr/bin/env python
import os, sys
import itertools
from datetime import datetime
from tabulate import tabulate

pathDirectory = sys.argv[1]
now = datetime.now()
timestamp = datetime.timestamp(now)

from pathlib import Path

week_threshold = 3600*24*7;
month_threshold = 3600*24*30;
six_months_threshold = 3600*24*30*6;

folder_categories = {
    "recent": [],
    "week_ago": [],
    "month_ago": [],
    "six_months_ago": [],
}

for path in Path(pathDirectory).iterdir():
    info = path.stat()
    week_ago = timestamp - week_threshold
    filename = os.path.basename(str(path))[:40]
    if(week_ago < info.st_mtime):
        folder_categories["recent"].append(str(filename))
        continue
    month_ago = timestamp - month_threshold
    if(month_ago < info.st_mtime):
        folder_categories["week_ago"].append(str(filename))
        continue
    six_months_ago = timestamp - six_months_threshold
    if(six_months_ago < info.st_mtime):
        folder_categories["month_ago"].append(str(filename))
        continue
    folder_categories["six_months_ago"].append(str(filename))


titles = ['recet','week_ago', 'month_ago', 'six_months_ago']
recent = folder_categories["recent"]
week_ago = folder_categories["week_ago"]
month_ago = folder_categories["month_ago"]
six_months_ago = folder_categories["six_months_ago"]


print(tabulate(reversed(list(itertools.zip_longest(recent, week_ago, month_ago, six_months_ago, fillvalue=""))), \
               headers=titles, tablefmt="fancy_grid", colalign=("right",)))
