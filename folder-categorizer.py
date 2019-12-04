#!/usr/bin/env python
import os, sys
from prettytable import PrettyTable
import itertools
from datetime import datetime

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
    filename = os.path.basename(str(path))
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



t = PrettyTable()
titles = ['recet','week_ago', 'month_ago', 'six_months_ago']
t.field_names = titles
recent = folder_categories["recent"]
week_ago = folder_categories["week_ago"]
month_ago = folder_categories["month_ago"]
six_months_ago = folder_categories["six_months_ago"]
for row in reversed(list(itertools.zip_longest(recent, week_ago, month_ago, six_months_ago, fillvalue=""))):
    t.add_row(list(row))
print(t)
