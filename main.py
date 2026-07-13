import asyncio
import os
import logging
import time
import aiohttp
from aiohttp import web
from pyrogram import idle
from bot import Bot

# Calculate uptime
START_TIME = time.time()

def get_uptime():
    elapsed = time.time() - START_TIME
    days, rem = divmod(elapsed, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s"

async def web_server():
    async def handle(request):
        uptime = get_uptime()
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Auto Forward Bot</title>
        </head>
        <body>
            <h1>✅ Bot is Running</h1>
            <p>Uptime: {uptime}</p>
            <p>Status: Alive</p>
        </body>
        </html>
        """
        return web.Response(text=html_content, content_type='text/html')
    
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 10000)   # Render के लिए 10000 port
    await site.start()
    print("🌐 Web Server Started on port 10000")

async def main():
    bot = Bot()
    await bot.start()
    print("🤖 Bot Started Successfully!")
    await web_server()   # web server start
    await idle()         # bot को alive रखने के लिए

if __name__ == "__main__":
    asyncio.run(main())