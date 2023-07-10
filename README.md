# Pr3
___
## О проекте 
### Проект выполняет роль осведомления о сервере по Minecraft

##  папка app ПРИЛОЖЕНИЕ
##  папка config ОСНОВА

# как запустить проект у себя 

## 1. зайдите в свой файл (в котором вы хотите разместить проект )
## 2. скопировать 
```
git clone https://github.com/TYTOY46/Pr3.git
``` 
## 3. в консоли `cmd` написать команду  `venv\Scripts\activate`
```
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

C:\Users\svitl\TY\V1>c:/Users/svitl/TY/V1/venv/Scripts/activate.bat

C:\Users\svitl\TY\V1>venv\Scripts\activate

(venv) C:\Users\svitl\TY\V1>
```
## 4. `pip install -r .\reguirements.txt` загрузка версий 
```
(venv) C:\Users\svitl\TY\V1>pip install -r .\reguirements.txt
Requirement already satisfied: asgiref==3.7.2 in c:\users\svitl\ty\v1\venv\lib\site-packages (from -r .\reguirements.txt (line 1)) (3.7.2)
Requirement already satisfied: Django==4.2.2 in c:\users\svitl\ty\v1\venv\lib\site-packages (from -r .\reguirements.txt (line 2)) (4.2.2)
Requirement already satisfied: django-classy-tags==4.0.0 in c:\users\svitl\ty\v1\venv\lib\site-packages (from -r .\reguirements.txt (line 3)) (4.0.0)
Requirement already satisfied: django-meta==2.2.0 in c:\users\svitl\ty\v1\venv\lib\site-packages (from -r .\reguirements.txt (line 4)) (2.2.0)
Requirement already satisfied: django-meta-mixin==0.3.0 in c:\users\svitl\ty\v1\venv\lib\site-packages (from -r .\reguirements.txt (line 5)) (0.3.0)
Requirement already satisfied: django-sekizai==4.1.0 in c:\users\svitl\ty\v1\venv\lib\site-packages (from -r .\reguirements.txt (line 6)) (4.1.0)
Requirement already satisfied: Pillow==9.5.0 in c:\users\svitl\ty\v1\venv\lib\site-packages (from -r .\reguirements.txt (line 7)) (9.5.0)
Requirement already satisfied: sqlparse==0.4.4 in c:\users\svitl\ty\v1\venv\lib\site-packages (from -r .\reguirements.txt (line 8)) (0.4.4)
Requirement already satisfied: tzdata==2023.3 in c:\users\svitl\ty\v1\venv\lib\site-packages (from -r .\reguirements.txt (line 9)) (2023.3)

[notice] A new release of pip available: 22.3.1 -> 23.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip

(venv) C:\Users\svitl\TY\V1>
```

## 4. потом написать в консоль `python manage.py runserver`
```
(venv) C:\Users\svitl\TY\V1>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 09, 2023 - 22:16:12
Django version 4.2.2, using settings 'P2.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
## 5. переходим по сылке `http://127.0.0.1:8000/` и воаля
```
System check identified no issues (0 silenced).
July 09, 2023 - 22:16:12
Django version 4.2.2, using settings 'P2.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
___