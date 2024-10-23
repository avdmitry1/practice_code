import requests
import sqlite3
import time
import aiohttp
import asyncio
from typing import Any

def create_database(db_name: str) -> sqlite3.Connection:
    connect = sqlite3.connect(db_name)
    cursor = connect.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS logs
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   time TEXT,
                   message TEXT)"""
    )
    connect.commit()
    return connect


def logs_event(connect: sqlite3.Connection, message: str):
    cursor = connect.cursor()
    cursor.execute(
        "INSERT INTO logs (time, message) VALUES (?, ?)",
        (time.strftime("%Y-%m-%d %H:%M:%S"), message),
    )
    connect.commit()


def get_content(urls: str):
    start_time = time.time()
    connect = create_database("logs_requests.db")
    for url in urls:
        logs_event(connect, f"Старт запиту до {url}")
        response = requests.get(url)
        if response.status_code == 200:
            logs_event(
                connect,
                f"Відповідь для адреси {url} отримано зі статусом {response.status_code}",
            )
        else:
            logs_event(
                connect,
                f"Відповідь для адреси {url} зі статусом {response.status_code}",
            )
    connect.close()
    print(f"Синхронно виконано за {time.time() - start_time} секунд")


"---------------------------------------------------------------------------"


def log_event(connect: sqlite3.Connection, message: str):
    cursor = connect.cursor()
    cursor.execute(
        "INSERT INTO logs (time, message) VALUES (?, ?)",
        (time.strftime("%Y-%m-%d %H:%M:%S"), message),
    )
    connect.commit()


async def get_content_aiohttp(url: str, connect: sqlite3.Connection):
    async with aiohttp.ClientSession() as session:
        log_event(connect, f"Початок запиту до адреси {url}")
        async with session.get(url) as response:
            if response.status == 200:
                log_event(
                    connect,
                    f"Відповідь для адреси {url} отримано зі статусом {response.status}",
                )
            else:
                log_event(
                    connect, f"Відповідь для адреси {url} зі статусом {response.status}"
                )


async def main(urls: str):
    start_time = time.time()
    connect = create_database("logs_aiohttp.db")
    tasks = [get_content_aiohttp(url, connect) for url in urls]
    await asyncio.gather(*tasks)
    connect.close()
    print(f"Асинхронно виконано за {time.time() - start_time} секунд")


urls = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/todos/1",
]

get_content(urls) #синхронний  request
asyncio.run(main(urls)) #асинхронний request
