#!/usr/bin/env python
from colorama import Fore, Back, Style
import os, sys
pathDirectory = sys.argv[1]
from datetime import datetime
now = datetime.now()
timestamp = datetime.timestamp(now)

from pathlib import Path
time_categories = [
    {"timeframe": "recent", "color" : Fore.GREEN},
    {"timeframe": "week_ago", "color" : Fore.YELLOW},
    {"timeframe": "month_ago", "color" : Fore.MAGENTA},
    {"timeframe": "six_months_ago", "color" : Fore.RED}
    ]
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
    
    if(week_ago < info.st_mtime):
        folder_categories["recent"].append(str(path))
        continue
    month_ago = timestamp - month_threshold
    if(month_ago < info.st_mtime):
        folder_categories["week_ago"].append(str(path))
        continue
    six_months_ago = timestamp - six_months_threshold
    if(six_months_ago < info.st_mtime):
        folder_categories["month_ago"].append(str(path))
        continue
    folder_categories["six_months_ago"].append(str(path))
for time_category in time_categories:
    print(time_category["color"] + "--------------------------------------------------------------------")
    print(time_category["timeframe"].upper())
    for folder_category in folder_categories[time_category["timeframe"]]:
        print(os.path.basename(folder_category))
    print("--------------------------------------------------------------------")
