@echo off
echo Downloading Files:
cd python.exe
python ../mods/setup/mod_updater.py
cd ..

echo Starting GitCraft152
java -Xmx8g -Xms8g -jar server.jar nogui
