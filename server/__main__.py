from .server import server


def main():
    server.start_tcp('localhost', 2087)


if __name__ == '__main__':
    main()
