## Dependências

- Python 3.10+
- yt-dlp

Instalação:

pip install -r requirements.txt

## FFmpeg

Baixe o FFmpeg em:

https://www.gyan.dev/ffmpeg/builds/

Baixe uma versão `Essentials` e extraia para o disco de sua preferência.

Certifique-se de que o caminho do FFmpeg definido no código corresponde ao local onde o FFmpeg foi instalado na sua máquina.

Exemplo:

C:\ffmpeg-8.1.2-essentials_build\bin

No código:

'ffmpeg_location': r'C:\ffmpeg-8.1.2-essentials_build\bin'

Ou, alternativamente, adicione a pasta `bin` do FFmpeg ao PATH do Windows. Nesse caso, não é necessário informar `ffmpeg_location` no código.