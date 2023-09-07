# reconhecimento_facial
Projecto Para Detecção &amp; Reconhecimento facial Usando Python...

Detector de Rostos e Comparador de Rostos
Este é um projeto Python que utiliza as bibliotecas face_recognition e OpenCV para detectar rostos em tempo real a partir da câmera e compará-los com uma imagem de referência.

Pré-requisitos
Antes de usar este projeto, certifique-se de ter instalado as seguintes dependências:

Python 3.x: Python Downloads
OpenCV: Você pode instalar o OpenCV usando pip install opencv-python
face_recognition: Você pode instalar o face_recognition usando pip install face_recognition
Como Usar
Clone ou faça o download deste repositório para o seu sistema.

Certifique-se de ter todas as dependências instaladas conforme mencionado acima.

Coloque a imagem de referência que você deseja comparar na mesma pasta do código fonte ou especifique o caminho completo para a imagem no código.

Abra um terminal na pasta raiz do projeto e execute o seguinte comando:

bash
Copy code
python detect_and_compare_faces.py
O programa começará a capturar vídeo da câmera em tempo real e detectará rostos. Ele comparará cada rosto detectado com a imagem de referência e desenhará um quadrado ao redor do rosto com base na correspondência.

Se um rosto na câmera coincidir com a imagem de referência, o quadrado ao redor do rosto ficará verde e exibirá a mensagem "Rosto Coincide". Caso contrário, o quadrado ficará vermelho e exibirá a mensagem "Rosto Não Coincide".

Pressione a tecla 'ESC' para encerrar o programa.

Estrutura do Projeto
detect_and_compare_faces.py: O arquivo principal que contém o código para a detecção de rostos e a comparação com a imagem de referência.
caminho_para_sua_imagem.jpg: A imagem de referência que você deseja comparar (coloque na mesma pasta ou especifique o caminho no código).
README.md: Este arquivo de documentação.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar solicitações de pull para melhorias ou correções.

Licença
Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.
