# build-parser
Для запуска скрипта должен быть устанвлен python версии 3 и выше<br/>
Для запуска скрипта нужно установить все зваисимости командой pip install -r requirements.txt<br/>
Далее python3 main.py<br/>
<br/>
-Программа считывает логи о сборке(Build) двух мобильных iOS приложений. Первое мобильное приложение реализованно с помощью архитектуры проектирования MVVM, а второе с помощью VIPER.<br/>
-Логи сборок хранятся в файлах buildMVVM.json и buildVIPER.json соответсенно.<br/>
-После парсинга программа визуализирует в бразуере в виде диаграмм все этапы для каждого мобильного приложения по времени.<br/>
