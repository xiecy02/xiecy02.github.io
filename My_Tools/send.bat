@echo off
:: 这行代码是关键：强制让黑窗口识别 UTF-8 编码，消除乱码
chcp 65001 >nul

cd /d D:\My_GitHub\xiecy02.github.io

git add .
git commit -m "Update via automated script"
git push origin main

echo.
echo --------------------------------------------------
echo    🚀 已经同步到 GitHub，请等待 1 分钟左右查看网站
echo --------------------------------------------------
echo.
pause