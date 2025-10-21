import discord
from discord.ext import commands
import os

# 🔐 디스코드 봇 토큰은 코드에 직접 넣지 않습니다.
# Render.com 환경변수(Settings → Environment Variables)에서 TOKEN으로 설정하세요.
TOKEN = os.getenv("TOKEN")

# 🔧 디스코드 봇 권한 설정
intents = discord.Intents.default()
intents.message_content = True  # 메시지 내용 접근 허용

# 🤖 봇 초기화
bot = commands.Bot(command_prefix="/", intents=intents)

# ✅ 봇이 켜졌을 때 콘솔에 표시
@bot.event
async def on_ready():
    print(f"리본봇 로그인 완료 ✅: {bot.user}")

# 🌱 리본 7일 프로젝트 시작 명령
@bot.command()
async def start(ctx):
    await ctx.send("🌱 리본 7일 프로젝트를 시작합니다! 오늘의 주스를 인증해주세요 💚")

# 💬 팀원 칭찬 명령
@bot.command()
async def cheer(ctx, *, member: discord.Member = None):
    if member:
        await ctx.send(f"{member.mention} 오늘 너무 멋져요! 🌟 리본 성공률이 올라가고 있어요!")
    else:
        await ctx.send("칭찬할 사람을 @멘션해주세요 🧡")

# 🩵 간단한 테스트용 상태 확인 명령
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 리본봇이 잘 작동 중이에요!")

# 🚀 봇 실행
bot.run(TOKEN)
