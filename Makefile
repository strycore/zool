deps:
	apt install -y supervisor autossh wakeonlan python3-dev \
		python3-setuptools tcpdump raspberrypi-kernel-headers

setup: deps
	mkdir -p ${HOME}/mac-addresses
	mkdir -p ${HOME}/log

install:
	cp scripts/tunnel /usr/local/bin/
	cp scripts/wake /usr/local/bin/
	cp supervisor/zool.conf /etc/supervisor/conf.d/

