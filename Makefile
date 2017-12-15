deps:
	apt install -y supervisor autossh wakeonlan

setup: deps
	mkdir -p /home/pi/mac-addresses
	mkdir -p /home/pi/log

install:
	cp scripts/tunnel /usr/local/bin/
	cp scripts/wake /usr/local/bin/
	cp supervisor/zuul.conf /etc/supervisor/conf.d/

