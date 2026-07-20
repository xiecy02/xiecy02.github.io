@echo off
:: 设置UTF-8编码，解决中文乱码
chcp 65001 > nul
cls

:: ====================== 配置区（只改这里）======================
set BLOG_PATH=D:\code\xiecy02.github.io
set PROXY_PORT=7890
:: ==========================================================

echo.
echo 【1/3】校验仓库目录...
if not exist "%BLOG_PATH%\.git" (
    echo ❌ 错误：目录 %BLOG_PATH% 不是Git仓库！路径配置错误！
    pause
    exit /b 1
)

echo 【2/3】进入博客根目录
cd /d "%BLOG_PATH%" || (
    echo ❌ 切换目录失败，请检查 BLOG_PATH 路径！
    pause
    exit /b 1
)

echo.
echo 【3/3】同步GitHub远程仓库
echo -------------------------------------------------------
:: 清空旧代理
git config --global --unset http.proxy 2>nul
git config --global --unset https.proxy 2>nul

:: 自动配置代理
if defined PROXY_PORT (
    echo 检测到代理端口%PROXY_PORT%，配置Git代理...
    git config --global http.proxy http://127.0.0.1:%PROXY_PORT%
    git config --global https.proxy http://127.0.0.1:%PROXY_PORT%
)

git pull origin main
set PULL_RESULT=%errorlevel%

echo -------------------------------------------------------
echo.

if %PULL_RESULT% equ 0 (
    echo ✅ 同步完成！本地仓库与远程完全一致
  
) else (
    echo ❌ 同步失败！网络/仓库权限出错
    echo 提示：1. 开启代理软件  2. 检查SSH密钥  3. 切换网络重试
)

echo.
pause