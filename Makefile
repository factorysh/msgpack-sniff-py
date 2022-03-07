dump:
	sudo tcpdump -n -w test.dat -i lo0 "tcp port 24224"

venv:
	python3 -m venv venv
	./venv/bin/pip install -U pip wheel
	./venv/bin/pip install -r requirements.txt
