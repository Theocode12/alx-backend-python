#!/usr/bin/python3
import aiosqlite
import asyncio

async def fetch_users():
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute("SELECT * FROM users")
        print(await cursor.fetchall())

async def fetch_older_users():
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        print(await cursor.fetchall())

async def fetch_concurrently():
    await asyncio.gather(fetch_users(), fetch_older_users())

if __name__ == "__main__":
     asyncio.run(fetch_concurrently())