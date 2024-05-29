@echo off
mkdir "C:\Users\Public\ERRENG"
xcopy /E "ERRENG" "C:\Users\Public\ERRENG" 
copy "startup.vbs" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp" 
C:\Windows\System32\setx.exe PATH "%PATH%;C:\Users\Public\ERRENG\wpy\python-3.12.3.amd64\Scripts"
