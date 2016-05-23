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


def server(th_count):
    def process_client(sock):
        num = 0
        while True:
            msg = ""
            while not msg.endswith('\n'):
                msg += sock.recv(1)

                if msg == 'bye\n':
                    break

                for i in range(serv_tout):
                    pass

                num += 1

    s = socket.socket()
    s.bind(host_port)
    s.listen(5)
    with ThreadPoolExecutor(max_workers=th_count) as pool:
        fts = []

        for i in range(th_count):
            sock,_ = s.accept()
            fts.append(pool.submit(process_client, sock))

            for ft in fts:
                ft.result()
