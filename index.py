import discord, datetime
token = "NzgwNDIxNzAxODc5NDYzOTQ2.X7u2WQ.q4Bhefsg2D-XutRtH_KF_RFg7wo"
client = discord.Client()

@client.event
async def on_ready():
    print("봇 준비 완료!")
    print(client.user)
    print("============================")

@client.event
async def on_message(message):
    if message.content == "/서버주소":
        await message.channel.send("서버주소는 bobdodukserver.kro.kr입니다")
    if message.content == "홀리":
        await message.channel.send("몰리")
    if message.content == "안녕하세요":
        await message.channel.send("안녕하세요 방장봇입니다 서버주소를 알고싶다면 /서버주소,버전을 알고싶다면 /버전을 사용해주세요")
    if message.content == "/버전":
        await message.channel.send("버전은 마인크래프트 자바에디션 1.15.2입니다")

    if message.content == '내정보':
        user = message.author
        date =datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 아이디 / 닉네임 : {user.name} / {user.id} / {user.display_name}")
        await message.channel.send(message.author.avatar_url)

client.run(token)