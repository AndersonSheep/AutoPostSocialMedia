import cv2

# Caminho para o arquivo de vídeo
caminho_do_video = 'videos/001.mp4'

# Abre o vídeo
cap = cv2.VideoCapture(caminho_do_video)

# Verifica se o vídeo foi aberto com sucesso
if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# Loop para ler cada quadro do vídeo
while True:
    # Lê o próximo quadro
    ret, frame = cap.read()

    # Verifica se o quadro foi lido corretamente
    if not ret:
        print("Fim do vídeo.")
        break

    # Aqui você pode realizar operações no quadro, se desejar

    # Exibe o quadro
    cv2.imshow('Video', frame)

    # Verifica se o usuário pressionou a tecla 'q' para sair
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Libera os recursos
cap.release()
cv2.destroyAllWindows()
