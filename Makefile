deps:
	apt install -y supervisor autossh

install:
	cp tunnel /usr/local/bin/
	cp supervisor/zuul.conf /etc/supervisor/conf.d/

