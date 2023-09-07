import cv2
import os
import face_recognition

# Carregue as imagens de referência de uma pasta
pasta_referencia = 'imgs/'
imagens_referencia = []

for arquivo in os.listdir(pasta_referencia):
    if arquivo.endswith('.jpg') or arquivo.endswith('.png'):
        imagem_referencia = face_recognition.load_image_file(os.path.join(pasta_referencia, arquivo))
        encoding_referencia = face_recognition.face_encodings(imagem_referencia)[0]
        imagens_referencia.append((encoding_referencia, arquivo))

# Inicialize a câmera
webcam = cv2.VideoCapture(0)

while True:
    # Capture um frame da câmera
    verificador, frame = webcam.read()
    if not verificador:
        break

    # Detecte rostos na imagem da câmera
    rostos_camera = face_recognition.face_locations(frame)
    
    for (top, right, bottom, left) in rostos_camera:
        # Extraia os recursos do rosto da câmera
        encoding_camera = face_recognition.face_encodings(frame, [(top, right, bottom, left)])[0]

        # Compare o rosto da câmera com todas as imagens de referência
        for encoding_referencia, nome_arquivo in imagens_referencia:
            resultado_comparacao = face_recognition.compare_faces([encoding_referencia], encoding_camera)

            # Se houver correspondência com uma das imagens de referência, exiba a mensagem
            if resultado_comparacao[0]:
                mensagem = f"Rosto coincide com {nome_arquivo}"
                cv2.putText(frame, mensagem, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                break  # Pare de verificar outras imagens de referência

        # Desenhe um quadrado ao redor do rosto detectado
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Exiba o frame da câmera
    cv2.imshow("Helium Detect Face", frame)

    # Quando pressionar ESC, encerre o loop
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()