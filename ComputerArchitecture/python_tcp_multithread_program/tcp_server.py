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
