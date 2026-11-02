@echo off
chcp 65001 >nul
echo ========================================================
echo   TalypMeyilnama Django Serwerini Isletmek (Python 3.11)
echo ========================================================
echo.
echo Migrasiyalary barlap ulanmak...
py manage.py makemigrations accounts schedule tasks homework attendance bot
py manage.py migrate
echo.
echo Nusga maglumatlary we Admin hasabyny girizmek...
py manage.py seed_talyp_data
echo.
echo ========================================================
echo Serwer baslady! Brauzerde acyn:
echo   Esasy sahypa: http://127.0.0.1:8000/
echo   Admin paneli: http://127.0.0.1:8000/admin/
echo   Admin login:  admin / admin123
echo   Talyp login:  talyp / talyp123
echo   Icki tor:     http://0.0.0.0:8000/
echo ========================================================
py manage.py runserver 0.0.0.0:8000
pause
