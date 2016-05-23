data = ' ' * 100 + '\x0A'
def client(th_count):
    sockets = []
    for i in range(th_count):
        sock = socket.socket()

        for cnt in range(3):
            try:
                sock.connect(host_port)
                break
            except socket.error:
                if cnt == 2:
                    raise
                    time.sleep(0.1)

            sockets.append(sock)

    for i in range(NUM_PACKETS):
        sock = random.choice(sockets)
        sock.send(data)

    for sock in sockets:
        sock.send('bye\x0A')
