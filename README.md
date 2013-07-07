indicate-brightness
===================

Brightness Indicator for Ubuntu 13.04 in case the inbuilt settings doesn't work

How To Use
------------------
1. Make sure that the brightness can be adjusted using intel_backlight by using the following method
	* `echo 1000 | sudo tee /sys/class/backlight/intel_backlight/brightness` and enter password
	* If your brightness changes, continue to step 2.
2. Change permissions for the /sys/class/backlight/intel_backlight/brightness file by
	* Open the /etc/rc.local file `sudo gedit /etc/rc.local`
	* Add the chmod command above `exit 0` : `chmod 777 /sys/class/backlight/intel_backlight/brightness`
3. Move the indicate-brightness.py to /usr/bin `mv indicate-brightness.py /usr/bin/`
4. Make the file executable. `sudo chmod +x /usr/bin/indicate-brightness.py`
5. Add the command `indicate-brightness.py` to Startup Applications

References
---------------
http://developer.ubuntu.com/resources/technologies/application-indicators/



