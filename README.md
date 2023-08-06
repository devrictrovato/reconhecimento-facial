# Reconhecimento Facial

Este repositório contém um projeto de reconhecimento facial utilizando a técnica Haar-like em visão computacional. O projeto visa detectar e reconhecer rostos em imagens ou vídeos.

## Funcionalidades

- Detecção de rostos em imagens estáticas.
- Detecção de rostos em vídeos em tempo real.
- Reconhecimento de rostos por meio de características Haar-like.
- Utilização do classificador Adaboost para otimização da detecção.

## Como Usar

1. Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/devrictrovato/Reconhecimento-Facial.git
cd Reconhecimento-Facial
```

2. Instale as dependências necessárias. Recomendamos o uso de um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. O **Detect_IMG.ipynb** foi executado pelo [Google Colab](https://colab.research.google.com), caso queira executar no seu sistema operacional, altere o **cv2_imshow** pelo **cv2.imshow**.

4. Ao terminar, desative o ambiente virtual:

```bash
deactivate
```

Lembre-se de substituir os placeholders (`clip.mp4`, `frontalface.xml`, e outros caminhos associado a arquivos.) pelas informações reais do seu repositório. Certifique-se de adicionar informações relevantes sobre o seu projeto, como uma descrição mais detalhada, exemplos de uso e outros detalhes pertinentes.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [Licença](https://github.com/devrictrovato/Reconhecimento-Facial/blob/main/LICENSE) para obter mais detalhes.
```