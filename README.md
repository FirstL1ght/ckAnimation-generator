# ckAnimation generator 2.0

[***English README.md***](https://github.com/FeelinVoids/ckAnimation-generator/blob/master/README_ENG.md)

Эти скрипты позволяют генерировать файлы анимаций подсветки для некоторых клавиатур от A4 Bloody. Я тестировал на Bloody B975, должно работать на похожих моделях с RGB подсветкой. Изменяя algorithms.py, можно изменять или писать свои анимации, наследуя класс `AlgorithmBase`.

### ВНИМАНИЕ!
Если вы решили опробовать данные скрипты - ВЫ ДЕЛАЕТЕ ВСЁ НА СВОЙ СТРАХ И РИСК! Если вдруг с Вашей клавиатурой или компьютером что-то случится, ответственность за это несёте только Вы сами.

## Использование

Установка программы осуществляется командой в cmd:

    pip install git+https://github.com/FeelinVoids/ckAnimation-generator.git

Теперь в консоли станет доступна команда `ckAnimationGenerator`, запускающая программу.

При запуске будет предложено ввести имя файла, но можно это пропустить, нажав Enter. Далее программа потребует ввести номер желаемого алгоритма из списка, после чего сгенерируется файл (Алгоритм Waves требует ещё ввести цветовой код). После этого будет выведен путь к файлу анимации. Файл следует импортировать в KeyDominator2 во вкладке RGB Animation и назначить в таблице слот Fn от 0 до 9.

![Импорт](https://i.imgur.com/66R2urN.png)

![Waves](https://i.imgur.com/gO0a5b3.gif)

![Starfall](https://i.imgur.com/Og8kqrh.gif)