# Ubuntu/Pi Recipe
## Steps
1. flash Ubuntu onto the Raspberry Pi (`sudo apt install rpi-imager`, flash onto an SD card)
2. with Ubuntu up and running, clone this repository (install github with `sudo apt install gh` to push changes)
3. make a python virtual environment (`python -m venv <new directory>`)
4. install gpiozero with `pip` (might already be downloaded)
5. wire it up (details omitted):
![image](https://github.com/user-attachments/assets/76ceeb83-6689-4fa1-95b3-ca36498acbe4)

6. Run it with `GPIOZERO_PIN_FACTORY=lgpio python3 basics.py`
