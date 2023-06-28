<h1 text-align="center">Модель движения на круговой автомобильной развязке </h1>
<h4><u>Вариант №13</u> учебной практики 2023 г.</h4>
<h4>Работу выполнил студент группы <u>ПИЭ-21 Дряхлов Олег</u></h4>

<div id="header" align="center">
  <hr align="center" width="650" size="3"/>
</div>

<div id="header" align="center">
  <img src="https://pa1.aminoapps.com/7227/7c4263a0187cbbb2c105b64973655dc6e668a39br1-500-281_hq.gif" width="400"/>
</div>

<div id="header" align="center">
  <hr align="center" width="650" size="3"/>
</div>

<h2>Начало работы</h2>

<h3>Шаг 1.</h3> Скопируйте репозиторий к себе на компьютер.<br><br>
<code>git clone https://github.com/Shuwiku/road-model.git</code><br><br>

<h3>Шаг 2.</h3> После окончания загрузки перейдите в рабочий каталог и создайте виртуальное окружение.<br><br>
<code>cd road-model<br>
python -m venv venv</code><br><br>
<b>или</b><br><br>
<code>cd road-model<br>
python3 -m venv venv</code><br><br>

<h3>Шаг 3.</h3> Активируйте виртуальное окружение, установите необходимые зависимости и запустите приложение<br><br>
<code>venv\Scripts\activate<br>
pip install -r requirements.txt<br>
python main.py</code><br><br>
<b>или</b><br><br>
<code>source venv/bin/activate<br>
python3 -m pip install -r requirements.txt<br>
python3 main.py</code><br>

<div id="header" align="center">
  <hr align="center" width="650" size="3"/>
</div>

<h2>Возможности</h2><br>
На самом деле, управлять там особо нечем. Это же модель, она работает сама по себе! Но кое-что мы сделать можем. <br>

<h3>Debug-mode</h3><br>
На самом деле, "дебаг-режим" это слишком громко для этой жалкой подделки. Оно просто выводит всю имеющуюся у неё информацию на экран
в более-менее понятной форме. Вы можете даже настроить это в теле программы! Файл <i>main.py</i>, переменная <i>debug</i>.<br>
Для того, чтобы вывести это на экран, используйте комбинацию клавиш <b>LEFT CTRL + D</b> <u>(Обязательно в английской раскладке на Linux.)</u><br>

<h3>Радио</h3><br>
В программе так же есть плеер, но для каноничности будем называть его радиом. Для того, чтобы добавить в пул песен свои, просто скопируйте их 
в следующую папку<br><br>
<code>road-model/Shiro/engine/sounds/</code><br><br>
Изначально там уже лежит несколько из нравящихся мне песен.<br><br>
Для управления плеером используются следующие комбинации клавиш:<br>
<b>LEFT CTRL + LEFT ARROW</b> - переключить на 1 песню назад<br>
<b>LEFT CTRL + LEFT RIGHT</b> - переключить на 1 песню вперёд<br>
<b>LEFT CTRL + LEFT DOWN</b> - поставить плеер на паузу<br>
<b>LEFT CTRL + LEFT UP</b> - снять плеер с паузы<br>

<div id="header" align="center">
  <hr align="center" width="650" size="3"/>
</div>

<h2>Заключение</h2>

В общем (и целом), я действительно постарался успеть сделать что-то хорошее за остаток недели, так что надеюсь на высокий балл.

<div id="header" align="center">
  <hr align="center" width="650" size="3"/>
</div>

<div id="header" align="center">
  <img src="https://media.tenor.com/LsTm2sO-8FkAAAAd/shiro-no-game-no-life.gif" width="400"/>
</div>

<div id="header" align="center">
  <hr align="center" width="650" size="3"/>
</div>
