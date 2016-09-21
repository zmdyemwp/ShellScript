@ adb reboot bootloader
@ timeout /t 5

@ fastboot -i 0x27f1 flash boot boot.img
@ fastboot -i 0x27f1 flash system system.img
@ fastboot -i 0x27f1 flash userdata userdata.img

@ fastboot -i 0x27f1 reboot
