CPU Affinity
===========

Python TCP server, client example.

To be honest, I don't know is it correct...

----
How to run on Ubuntu:

    python mt_test.py client 4 & time python mt_test.py server 4 

----
How to run on Ubuntu with one cpu:

    python mt_test.py client 4 & time taskset 0x00000001 python mt_test.py server 4
