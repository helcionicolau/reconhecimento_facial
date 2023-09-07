# reconhecimento_facial
Projecto Para Detecção &amp; Reconhecimento facial Usando Python...

Detector de Rostos com Comparação de Imagens
Este é um projeto Python que utiliza a biblioteca face_recognition para detectar rostos em tempo real a partir da câmera e compará-los com imagens de referência em uma pasta.

Pré-requisitos
Antes de usar este projeto, certifique-se de ter instalado as seguintes dependências:

Python 3.x: Python Downloads
OpenCV: Você pode instalar o OpenCV usando pip install opencv-python
face_recognition: Você pode instalar o face_recognition usando pip install face_recognition
Como Usar
Clone ou faça o download deste repositório para o seu sistema.

Certifique-se de ter todas as dependências instaladas conforme mencionado acima.

Coloque as imagens de referência na pasta imagens_referencia. Certifique-se de que as imagens estejam no formato .jpg ou .png.

Abra um terminal na pasta raiz do projeto e execute o seguinte comando:

bash
Copy code
python detect_face.py
O programa começará a capturar vídeo da câmera em tempo real e detectará rostos. Se um rosto na câmera coincidir com qualquer uma das imagens de referência na pasta imagens_referencia, ele exibirá uma mensagem na parte inferior do quadrado ao redor do rosto.

Pressione a tecla 'ESC' para encerrar o programa.

Estrutura do Projeto
detect_face.py: O arquivo principal que contém o código para a detecção de rostos e comparação com as imagens de referência.
imagens_referencia/: Pasta onde você deve colocar as imagens de referência.
README.md: Este arquivo de documentação.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar solicitações de pull para melhorias ou correções.

Licença
Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.
