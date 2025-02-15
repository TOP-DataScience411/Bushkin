from pathlib import Path
from re import compile, MULTILINE
from sys import path

text = (Path(path[0]) / "history_dates_ed.txt").read_text("utf-8")


months = (
    'января', 'январь',
    'февраля', 'февраль',
    'марта', 'март',
    'апреля', 'апрель',
    'мая', 'май',
    'июня', 'июнь',
    'июля', 'июль',
    'августа', 'август',
    'сентября', 'сентябрь',
    'октября', 'октябрь',
    'ноября', 'ноябрь',
    'декабря', 'декабрь'
)
           
day_str = r"(?:[1-9]|0[1-9]|[12]\d|3[01])"
month_str = f"(?:{'|'.join(months)})"
year_str = r"(?:1[89]\d\d|20[01]\d|202[0-5]) г\."

pattern = ( f"^{day_str} {month_str} {year_str}|" 
            f"^{day_str} {month_str} {year_str} – {day_str} {month_str} {year_str}|" 
            f"^{day_str}–{day_str} {month_str} {year_str}|"
            f"^{day_str} {month_str} – {day_str} {month_str} {year_str}|"
            f"^{month_str}–{month_str} {year_str}|"
            f"^{month_str} {year_str}|"
            f"^{year_str}|"
            fr"^\d\d\d\d.\d\d\d\d гг\."
           )
           
patern_dmy = compile(pattern, MULTILINE)


result = patern_dmy.findall(text)
print(len(result))
# print(*result,sep='\n')

# 250