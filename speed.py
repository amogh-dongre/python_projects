#!/usr/bin/env python3
import speedtest
server=speedtest.Speedtest()
server.get_best_server()
down=server.download()
down/=1000-000
print(f"Download speed: {down} Mb/s")
up =server.upload()
up/=1000-000
print(f"Upload speed: {up} Mb/s")
ping=server.results.ping
print(f"Ping speed: {ping}")
