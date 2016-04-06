cmd /C taskkill /F /IM python.exe
cd C:\Python27\Edmodo
cmd /C python manage.py makemigrations
cmd /C python manage.py migrate
pause