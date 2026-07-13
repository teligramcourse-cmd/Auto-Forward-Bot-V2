import asyncio
import time
from aiohttp import web
from pyrogram import idle

# Import Bot class carefully
try:
    from bot import Bot
    print("✅ Bot class imported successfully")
except Exception as e:
    print(f"❌ Import Error: {e}")
    exit(1)

START_TIME = time.time()

def get_uptime():
    elapsed = time.time() - START_TIME
    days, rem = divmod(int(elapsed), 86400)
    hours, rem = divmod(rem, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{days}d {hours}h {minutes}m {seconds}s"

async def web_server():
    async def handle(request):
        uptime = get_uptime()
        html = f"<h1>✅ Auto Forward Bot Running</h1><p>Uptime: {uptime}</p>"
        return web.Response(text=html, content_type="text/html")
    
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 10000)
    await site.start()
    print("🌐 Web Server Started on port 10000")

async def main():
    bot = Bot()
    await bot.start()
    print("🤖 Bot Started Successfully!")
    await web_server()
    await idle()

if __name__ == "__main__":
    asyncio.run(main())