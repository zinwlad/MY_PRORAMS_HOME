
# Чтобы рассчитать скорость вашего интернет-соединения с помощью Python, вам необходимо
# установить библиотеку Python, известную как  speedtest . Если вы никогда не использовали его раньше,
# вы можете легко установить его в своей системе с помощью команды pip:
# pip install speedtest-cli

import speedtest
wifi  = speedtest.Speedtest()
print("Wifi Download Speed is ", wifi.download())
print("Wifi Upload Speed is ", wifi.upload())