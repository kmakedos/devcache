from server import server
import os


def main():
    address = os.getenv("DEVCACHE_HOST", "localhost")
    port = os.getenv("DEVCACHE_PORT", 8001)
    print(f"Arguments found from env: {address} {port}")
    s = server.Server(address, int(port))
    s.start()


if __name__ == '__main__':
    main()