Msgpack sniff
=============

msgpack serialisation is self describing.

Lets use plain old tcpdump for sniffing msgpack exchange.

test it
-------

    make venv

Get some datas

    sudo tcpdump -n -w test.dat -i lo "tcp port 24224"

Analyze them

    ./venv/bin/python sniff.py test.dat
