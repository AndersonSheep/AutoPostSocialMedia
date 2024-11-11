import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
from PIL import Image, ImageDraw, ImageFont

# Função para criar uma imagem com texto e emoji
def create_text_image(text, heart, font_size=30, font_path=None):
    # Criar uma imagem vazia
    image = Image.new('RGBA', (800, 100), (255, 255, 255, 0))  # Tamanho e fundo transparente
    draw = ImageDraw.Draw(image)

    # Usar a fonte especificada, ou uma fonte padrão se não for fornecida
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()

    # Calcular a largura e altura do texto
    text_bbox = draw.textbbox((0, 0), text, font=font)  # Usar textbbox para obter as dimensões
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calcular a posição central
    text_x = (image.width - text_width) // 2
    text_y = (image.height - text_height) // 2

    # Desenhar o texto na imagem
    draw.text((text_x, text_y), text, fill='yellow', font=font)

    # Desenhar o coração
    heart_x = text_x + text_width + 5  # 5 pixels de espaço entre o texto e o coração
    draw.text((heart_x, text_y), heart, fill='red', font=font)  # Desenhar o coração em vermelho

    return image

# Nome do arquivo de saída
output_filename = "videos/video_editado.mp4"

# Checar se o arquivo de saída já existe e deletá-lo se necessário
if os.path.exists(output_filename):
    os.remove(output_filename)

# Carregar o vídeo
video = VideoFileClip("videos/video1.mp4")

# Definir o tempo de início do texto (últimos 10 segundos do vídeo)
inicio_texto = max(0, video.duration - 10)

# Criar a imagem com o texto e o emoji
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # Caminho para uma fonte alternativa
text_image = create_text_image("LINK NA BIO ", "❤️", font_size=70, font_path=font_path)

# Salvar a imagem temporariamente
text_image_path = "text_image.png"
text_image.save(text_image_path)

# Criar um clip de imagem a partir da imagem
text_clip = ImageClip(text_image_path).set_duration(10).set_start(inicio_texto).set_position("center")

# Combinar o texto com o vídeo
video_final = CompositeVideoClip([video, text_clip])

# Salvar o vídeo final
video_final.write_videofile(output_filename, codec="libx264")

# Remover a imagem temporária
os.remove(text_image_path)
