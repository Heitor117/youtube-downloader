# Este programa baixa músicas do YouTube utilizando yt-dlp e FFmpeg.

# pip install yt-dlp OU python -m pip install yt-dlp
# Link do FFmpeg: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
#(baixe e extraia o .zip)

from yt_dlp import YoutubeDL

DOWNLOAD_PATH = r"D:\\"  # Escolha o caminho de destino para salvar os arquivos baixados


print("Cole as URLs dos videos ou playlists (uma por linha)")
print("Quando terminar, pressione Enter em uma linha vazia!.\n")

urls = []

while True:
    url = input()

    if url == "":
        break

    urls.append(url)

opcoes = {
    'format': 'bestaudio/best',
<<<<<<< Updated upstream
    'outtmpl': DOWNLOAD_PATH + r'\%(title)s.%(ext)s',               # Escolha o caminho de destino para salvar os arquivos baixados
    'ffmpeg_location': r'C:\ffmpeg-2026-08-09-git-6bbc22dc09-essentials_build',     # Escolha o caminho onde o FFmpeg está instalado
=======
    'ignoreerrors': True,
    'outtmpl': r'D:\%(title)s.%(ext)s',                             # Escolha o caminho de destino para salvar os arquivos baixados
    'ffmpeg_location': r'C:\ffmpeg-8.1.2-essentials_build\bin',     # Escolha o caminho onde o FFmpeg está instalado
>>>>>>> Stashed changes
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

with YoutubeDL(opcoes) as ydl:
    ydl.download(urls)

print("\nDownload concluído com exito!\n")