Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  TalypMeyilnama Django Serwerini Isletmek (Python 3.11) " -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""
$pyCmd = if (Get-Command py -ErrorAction SilentlyContinue) { "py" } else { "python" }
Write-Host "1. Migrasiyalary ulanmak..." -ForegroundColor Yellow
& $pyCmd manage.py makemigrations accounts schedule tasks homework attendance bot
& $pyCmd manage.py migrate
Write-Host ""
Write-Host "2. Nusga maglumatlary we Admin hasabyny girizmek..." -ForegroundColor Yellow
& $pyCmd manage.py seed_talyp_data
Write-Host ""
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "Serwer baslady! Brauzerde acyn:" -ForegroundColor Green
Write-Host "  Esasy sahypa: http://127.0.0.1:8000/" -ForegroundColor White
Write-Host "  Admin paneli: http://127.0.0.1:8000/admin/" -ForegroundColor Yellow
Write-Host "  Admin login:  admin / admin123" -ForegroundColor Green
Write-Host "  Talyp login:  talyp / talyp123" -ForegroundColor Green
Write-Host "  Icki tor:     http://0.0.0.0:8000/" -ForegroundColor White
Write-Host "========================================================" -ForegroundColor Cyan
& $pyCmd manage.py runserver 0.0.0.0:8000
