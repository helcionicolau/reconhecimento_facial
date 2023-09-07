import cv2
import face_recognition

# Carregue a imagem de referência do rosto que você deseja comparar
imagem_referencia = face_recognition.load_image_file('AntonioBaptista.jpeg')
encoding_referencia = face_recognition.face_encodings(imagem_referencia)[0]

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

        # Compare o rosto da câmera com a imagem de referência
        resultado_comparacao = face_recognition.compare_faces([encoding_referencia], encoding_camera)

        # Determinar a cor do quadrado com base no resultado da comparação
        cor_quadrado = (0, 255, 0) if resultado_comparacao[0] else (0, 0, 255)

        # Desenhe um quadrado colorido ao redor do rosto detectado
        cv2.rectangle(frame, (left, top), (right, bottom), cor_quadrado, 2)

        # Exiba a mensagem de resultado na parte inferior do quadrado
        texto_resultado = "Rosto Coincide" if resultado_comparacao[0] else "Rosto Não Coincide"
        cor_texto = (0, 255, 0) if resultado_comparacao[0] else (0, 0, 255)
        cv2.putText(frame, texto_resultado, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, cor_texto, 2)

    # Exiba o frame da câmera
    cv2.imshow("Helium Detect Face", frame)

    # Quando pressionar ESC, encerre o loop
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()