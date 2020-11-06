Hello Andrii

python3 .
We are in the __main__
2020-11-06 12:41:02.862958
linux

python3 . -h

usage: . [-h] [-o OPT] [-l]

Приклад передачі аргументів у Python програму.

optional arguments:
  -h, --help            show this help message and exit
  -o OPT, --optional OPT
                        Цей параметр є вибірковим.
  -l, --logs            Якщо виконати команду з цим параметром будуть
  
                        виводитись логи.
                     
python3 . -o "Цей текст також має вивестись"
 ========== >> Цей текст також має вивестись << ==========

python3 . --logs
2020-11-06 12:45:54,430 root INFO: Тут буде просто інформативне повідомлення
2020-11-06 12:45:54,430 root WARNING: Це Warning повідомлення
2020-11-06 12:45:54,430 root ERROR: Це повідомлення про помилку

