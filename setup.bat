@echo off
mkdir "E:Users\Public\ERRENG"
xcopy /E "ERRENG" "E:Users\Public\ERRENG" 
copy "startup.vbs" "E:ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
