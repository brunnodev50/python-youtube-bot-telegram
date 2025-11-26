# 🤖 YouTube Media Downloader Bot for Telegram

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![yt-dlp](https://img.shields.io/badge/yt--dlp-Media-red?style=for-the-badge&logo=youtube&logoColor=white)

<h3>
  <a href="README.md">🇺🇸 Read in English</a>
</h3>

</div>

---

## 📖 Sobre
Bot de Telegram de alto desempenho para baixar e gerenciar conteúdo do YouTube. Desenvolvido com **Python**, **yt-dlp** e focado em princípios de **Arquitetura Limpa** (Clean Architecture), garantindo facilidade de manutenção e escalabilidade.

### ✨ Funcionalidades
* Baixe vídeos do YouTube diretamente pelo chat do Telegram.
* Opção de escolha de qualidade do vídeo antes do download.
* Processamento rápido e eficiente de mídia.

---

### 🚀 Instalação e Configuração

#### 1. Obter o Token do Bot
Para o bot funcionar, é necessário criá-lo no Telegram através do **BotFather**:
1.  Acesse o [BotFather](https://telegram.me/BotFather).
2.  Envie o comando `/newbot`.
3.  Siga as instruções para obter o seu **HTTP API Token**.

#### 2. Configurar o Código
> **Nota:** Para projetos em produção, utilize variáveis de ambiente. Para testes rápidos neste repositório:

1.  Abra o arquivo `bot.py` no seu editor.
2.  Localize a **linha 6**.
3.  Substitua a variável `TOKEN = ''` pelo token que você copiou do BotFather:
    ```python
    TOKEN = 'SEU_TOKEN_AQUI_123456'
    ```

#### 3. Executar o Bot
Com o Python instalado, execute o comando no terminal dentro da pasta do projeto:
```bash
python bot.py
