# Importação das bibliotecas
import cv2

# Função para redimensionar uma imagem
def redim(img, width):
  alt = int(img.shape[0] / img.shape[1] * width)
  img = cv2.resize(img, (width, alt), interpolation = cv2.INTER_AREA)
  return img

# Cria o detector de faces baseado no XML
cxml = 'frontalface.xml' # > Caminho do modelo
cascade = cv2.CascadeClassifier(cxml)

# Abre um vídeo gravado
video = 'clip.mp4' # Caminho do vídeo
camera = cv2.VideoCapture(video) # Caso queira usar uma camera coloque 0 no lugar do video (ou outro index de acordo com os dispositivos conectados)

while True:
  # read() Retorna 1-Se houve sucesso e 2-O próprio frame
  ret, frame = camera.read()

  if not ret: break # Final do vídeo

  # Reduz tamanho do frame para acelerar processamento
  frame = redim(frame, 320)

  # Converte para tons de cinza
  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Detecta as faces no frame
  faces = cascade.detectMultiScale(
      frame_gray,
      scaleFactor = 1.1,
      minNeighbors = 3,
      minSize = (20, 20),
      flags = cv2.CASCADE_SCALE_IMAGE
  )

  frame_temp = frame.copy()
  for (x, y, lar, alt) in faces:
    cv2.rectangle(frame_temp, (x, y), (x + lar, y + alt), (0, 255, 0), 2)

  cv2.imshow('Encontrando faces...', redim(frame_temp, 640))

  # Espera que a tecla ESC seja pressionada para sair
  key = cv2.waitKey(1)
  if key == 27:
    break

# Fecha streaming
camera.release()
cv2.destroyAllWindows()