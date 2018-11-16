import socketserver, threading, time, configparser, logging

# create logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename='light.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

config = configparser.ConfigParser()
config.read('settings.ini')
serversettings = config['server']


class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        current_thread = threading.current_thread()
        print("{}: client: {}, wrote: {}".format(current_thread.name, self.client_address, data))
        socket.sendto(data.upper(), self.client_address)


class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass


if __name__ == "__main__":

    server = ThreadedUDPServer((serversettings['host'], int(serversettings['port'])), ThreadedUDPRequestHandler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True

    try:
        server_thread.start()
        print("Server started at {} port {}".format(serversettings['host'], serversettings['port']))
        logging.info('Server listening at %s on port %s', serversettings['host'], serversettings['port'])
        while True: time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        server.shutdown()
        server.server_close()
        exit()
