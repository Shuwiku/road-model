<p align="center">
    <img alt="Широ ^-^" width="500" src="https://i.ibb.co/gyjPNyr/shiro.gif"/>
</p>

<p align="center">
    <img alt="Python Version" src="https://img.shields.io/badge/Python%20-%203.10%20-%20yellow"/>
    <img alt="Pygame" src="https://img.shields.io/badge/Pygame%20-%202.5.0%20-%20green"/>
    <img alt="Version" src="https://img.shields.io/badge/Version%20-%201.0%20-%20purple"/>
    <img alt="License" src="https://img.shields.io/badge/License%20-%20MIT%20-%20aqua">
</p>

## Содержание

- [О Проекте](#о-проекте)
- [Установка](#установка)
    - [Для Windows](#windows)
    - [Для Linux](#linux)
- [Возможности Проекта](#возможности-проекта)
    - [Режим отладки](#режим-отладки)
    - [Плеер](#плеер)
- [Возможные улучшения](#возможные-улучшения)
- [Напутствие](#напутствие)
- [Используемая музыка](#используемая-музыка)

## О Проекте

Вариант №13 летней практики 2023г. **"Модель движения на круговой автомобильной развязке"**

Работу выполнил студент группы ПИЭ-21 Дряхлов Олег

<p align="center">
    <img alt="Пример работы программы" width="500" src="https://i.ibb.co/QMYm5vz/program-example.png"> <br>
    Пример работы программы
</p>

## Установка

### Windows

1. Клонирование репозитория **`git clone https://github.com/Shuwiku/road-model.git`**
2. Переход в папку проекта **`cd road-model`**
3. Создание виртуального окружения **`python -m venv venv`**
4. Активация виртуального окружения **`venv\Scripts\activate`**
5. Установка зависимостей **`pip install -r requirements.txt`**
6. Запуск **`python main.py`**

```
git clone https://github.com/Shuwiku/road-model.git
cd road-model
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Linux

Описание шагов не отличается от установки на Windows.

```
git clone https://github.com/Shuwiku/road-model.git
cd road-model
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```

## Возможности Проекта

### Режим отладки

Вообще "режим отладки" - это слишком крутое название для того, чтобы называть это так, но, в любом случае, сочетанием клавиш
`Left Ctrl + D` вы можете его запустить. По сути он просто выводит имеющуюся у него информацию на экран в удобном для чтения виде.
Настроить вывод можно только в коде, в файле [main.py](main.py), переменная *debug* (строка 44 для версии 1.0).

<p align="center">
    <img alt="Пример работы режима отладки" width="500" src="https://i.ibb.co/W0stSCk/debug-mode-example.png"> <br>
    Пример работы режима отладки
</p>

### Плеер

В приложении также есть плеер, можно сказать что это дорожное радио. Все композиции, которые используются плеером находятся в папке 
[sounds](Shiro/engine/sounds). Если хотите использовать свои треки в общем пуле (или удалить уже имеющиеся в нём) - взаимодействуйте с
файлами в папке. **В папке должны находиться __только__ файлы с расширениями __waw__, __mp3__ и __ogg__.**

Для управления плеером в приложении, используйте следующие сочетания клавиш:

- **`Left Ctrl + Arrow Left`** - Переключение на предыдущую композицию
- **`Left Ctrl + Arrow Right`** - Переключение на следующую композицию
- **`Left Ctrl + Arrow Up`** - Снять плеер с паузы
- **`Left Ctrl + Arrow Down`** - Поставить плеер на паузу

## Возможные улучшения

- [ ] Увеличить размер карты. Сделать перемещение по карте с помощью камеры со смещением всех объектов при движении.
- [ ] Добавить больше транспортных средств. Например, автобус, который будет останавливаться на остановках.
- [ ] Улучшить костыль с вектором направления движения автомобиля. Сделать его Т-образным для улучшения обнаружения возможной коллизии.
- [ ] Сделать так, чтобы автомобиль не трясло на дороге.
- [ ] Добавить светофоры.
- [ ] Добавить возможность вывода данных по объекту при нажатии на него ЛКМ. (автомобиль, светофор, спавнер).
- [ ] Добавить возможность ставить симуляцию на паузу.
- [ ] Добавить возможность изменения громкости плеера.
- [ ] Добавить кнопки пользовательского интерфейса.
- [ ] Добавить возможность изменять основные настройки с помощью тектового конфигурационного файла (config.json / config.ini)

## Напутствие

Если вдруг этот проект когда-нибудь попадёт в руки другому человеку, который делает проект для сдачи, хочу сказать пару слов.

**Во-первых**, этот проект я сделал за 4 дня, хотя мне для его реализации было дано 2 или 3 месяца. Преподаватель принял проект, но лично
я результатом не особо доволен, и, возможно, я его буду немного улучшать (в разумных пределах). Так о чём я хотел сказать - чёрт возьми, не
надо откладывать проект до последнего. Эти 4 дня работы были самыми напряжёнными в моей жизни.

**Во-вторых**, если вы тоже новичок на GitHub, и хотите сделать красивое оформление для репозитория - посмотрите гайды на ютубе сначала.
html? css? bootstrap? Забудьте! (Ну, почти). А, ещё есть функция предпросмотра для редактируемого файла. Найдите её, и не
позорьтесь как я, с тысячей коммитов "Update README.md".

## Используемая музыка

- [Blacklite District](https://www.youtube.com/@BlackliteDistrict) -  [Preach to the Choir](https://www.youtube.com/watch?v=Xoor-OWCbBY)
- [Imagine Dragons](https://www.youtube.com/@ImagineDragons) - [Follow You](https://www.youtube.com/watch?v=k3zimSRKqNw)
- Kagamine Rin – Regret Message **(?)**
    - [Harmony Team](https://www.youtube.com/@HarmonyTeamChannel) - [Кавер на русском](https://www.youtube.com/watch?v=dsJODqGJtuk)
- Suzuki Konomi — [This game](https://www.youtube.com/watch?v=8mByCL-6RTk) **(?)**
    - [LeeandLie (AmaLee)](https://www.youtube.com/@LeeandLie) - [English cover](https://www.youtube.com/watch?v=DxWjE4doQjg)
- [Mystery Skulls](https://www.youtube.com/channel/UC0jd1RjiMOAbs4CikoADJGA) - [The Future](https://www.youtube.com/watch?v=pBndx99Ho50)
- [We are Fury](https://www.youtube.com/channel/UC6l-ZBVy89t2VirZt2QG3aQ) (feat. Derek Joel) - [Poison](https://www.youtube.com/watch?v=J0J_jB40Dnw)
