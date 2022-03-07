Msgpack sniff
=============

msgpack serialisation is self describing.

Lets use plain old tcpdump for sniffing msgpack exchange.

Test it
-------

    make venv

Get some datas

    sudo tcpdump -n -w test.dat -i lo "tcp port 24224"

Analyze them

    ./venv/bin/python sniff.py test.dat

Example
-------

Some fluentd ping pong.

```
127.0.0.1:24224 -> 127.0.0.1:49752
	 [b'HELO', {b'nonce': b'\\\xf4\x8c\x1c[\x9d\xc9\xfdM\xb1\xf3t/\xc7\xa5\x8b', b'auth': b'<\xce\x92A\xdbJ\x83\x82|\xbd\x95@\xfe\xce\x9b+', b'keepalive': True}]
127.0.0.1:49752 -> 127.0.0.1:24224
	 [b'PING', b'flb.local', b'L{$J1\xde\xc6\x8f\xf1FfaQ\xa8z\xed', b'745d487046747b7b2fcfa7626e525cb6f3fb8cc6ad9a4fa16891709b3ee4e57a89600901e28cc65f0663c145d4e293fc061e9ca6606a77879e52211dba41b55a', b'', b'63ddf5eb7bd0dac84698e3b9163ef5f8c9558e5daf842d2a8fe9d3f2f7e59a6d7bafe4bd8907258d48e1644afb519dc25049701ab741130454febca569d573d6']
127.0.0.1:24224 -> 127.0.0.1:49752
	 [b'PONG', True, b'', b'server.example.com', b'54309e623c705b44d55e1c7d19f9a29b46f421ab30f87ed236baacdecc61e004595578f0bd522c5a245c9ebe435c3b83119591d755078c9f30bd2e639a957d33']
127.0.0.1:49752 -> 127.0.0.1:24224
	 [b'aussi', [[1646686719, {b'rand_value': 7424620111837556107}], [1646686720, {b'rand_value': 421356355860644223}], [1646686721, {b'rand_value': 10263606291564770928}], [1646686722, {b'rand_value': 7721786514441681076}]], {b'chunk': b'3b306f59cd2367ee3f18b57a1185d227', b'size': 4}]
127.0.0.1:24224 -> 127.0.0.1:49752
	 {b'ack': b'3b306f59cd2367ee3f18b57a1185d227'}
127.0.0.1:24224 -> 127.0.0.1:49754
	 [b'HELO', {b'nonce': b'\x0eo3\xa9\xa3@Wi\xe1\x85\x90\xcb\xb0$tq', b'auth': b'\x92,kD\xa9Fzi\xc9\x88\x8bUh\x90<N', b'keepalive': True}]
127.0.0.1:49754 -> 127.0.0.1:24224
	 [b'PING', b'flb.local', b'L{$J1\xde\xc6\x8f\xf1FfaQ\xa8z\xed', b'7336e17ef1de99631bd3e101cca8d3d9b451fb7675de2cac62d210cc27d408842a8715304e8075af40337acc764a7bf7366effe4420937948af8e8b859d4168f', b'', b'3c35c65781b0d14b56b640682f912a11f4bd1c18be285c58bab4968f4803cd0b9dfdf3a69771a1f6ad209d408055b3139ba05f63fd3c412f2544be1b66821b73']
127.0.0.1:24224 -> 127.0.0.1:49754
	 [b'PONG', True, b'', b'server.example.com', b'c9beebc73026aaf609905499563cf778a98cddc61fe99d0a3b196d9c202aa35783bcb3ca8dfd04b3c63504cd453bf60c33a8791ef62520edb672b14009592b19']
127.0.0.1:49754 -> 127.0.0.1:24224
	 [b'aussi', [[1646686723, {b'rand_value': 7884160172759579118}], [1646686724, {b'rand_value': 5417808024786510511}], [1646686725, {b'rand_value': 11457246807587721347}], [1646686726, {b'rand_value': 1257448592848753448}]], {b'chunk': b'279f5d22659ad7f665e225ac4ff188e2', b'size': 4}]
127.0.0.1:24224 -> 127.0.0.1:49754
	 {b'ack': b'279f5d22659ad7f665e225ac4ff188e2'}
```


