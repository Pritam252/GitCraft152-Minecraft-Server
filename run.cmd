@echo off
echo Downloading Files:
cd python.exe
python mods/mod_updater.py

echo Starting GitCraft152
java -Xmx8g -Xms8g -jar server.jar nogui
