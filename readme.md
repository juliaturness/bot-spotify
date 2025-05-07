# Bot de Envio de Respostas para Formulários Google a Partir do Spotify

Este projeto consiste em um **bot automatizado** que preenche um formulário do Google com informações de músicas de uma playlist do Spotify, incluindo o nome da música, nome do artista e o turno (Noturno). O bot envia uma nova resposta para o formulário e repete o processo até que todas as músicas da playlist sejam enviadas.

## Pré-requisitos

Para rodar este bot, você precisará de:

- **Python 3.x** instalado em sua máquina.
- **Spotify API credentials** (Client ID e Client Secret) para acessar os dados da sua playlist do Spotify.
- **Google Form** para o qual o bot enviará as respostas.

## Instalação

Siga as instruções abaixo para configurar o ambiente e executar o bot:

1. **Instalar as dependências do projeto**:

    Abra o terminal/linha de comando e execute os seguintes comandos para instalar as bibliotecas necessárias:

    ```bash
    pip install spotipy selenium
    ```

    **Selenium** é a biblioteca usada para automatizar o navegador e interagir com o formulário do Google.

2. **Instalar o WebDriver** (para o Selenium):

    Para que o Selenium funcione corretamente, você precisará de um WebDriver para o navegador. Utilize o seguinte comando para instalar o `webdriver-manager`:

    ```bash
    pip install selenium webdriver-manager
    ```

    O `webdriver-manager` gerencia o download do driver para o Chrome, por exemplo, e mantém a versão correta compatível com o navegador.

3. **Atualizar o pip (se necessário)**:

    Para garantir que o pip esteja na versão mais recente, execute:

    ```bash
    python.exe -m pip install --upgrade pip
    ```

## Configuração do Projeto

1. **Obtenha suas credenciais do Spotify**:

    Para acessar a API do Spotify e obter as faixas de uma playlist, você precisará de uma chave de cliente (Client ID) e uma chave secreta (Client Secret) da Spotify API.

    - Acesse [Spotify for Developers](https://developer.spotify.com/dashboard/applications) e crie um aplicativo para obter essas credenciais.

2. **Configurar as credenciais no código**:

    - Abra o arquivo `bot.py`.
    - Substitua os valores das variáveis `SPOTIFY_CLIENT_ID` e `SPOTIFY_CLIENT_SECRET` pelas credenciais que você obteve no passo anterior.

    ```python
    SPOTIFY_CLIENT_ID = 'SUA_CLIENT_ID_AQUI'
    SPOTIFY_CLIENT_SECRET = 'SEU_CLIENT_SECRET_AQUI'
    ```

3. **Defina a URL da playlist do Spotify**:

    - No código, substitua a variável `PLAYLIST_URL` com a URL da playlist do Spotify da qual você quer pegar as músicas:

    ```python
    PLAYLIST_URL = 'https://open.spotify.com/playlist/5LanSitIRsd1ZGwq2XB9gT?si=jkPlf7QVRLSLwBGDFJ9cVg'
    ```

4. **Formulário do Google**:

    - Substitua a variável `FORM_URL` com a URL do formulário do Google no qual você deseja enviar as respostas. O bot vai preencher o formulário com os dados das músicas.

    ```python
    FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSce_wQf6Jz58QZDD4di8FUfNcei6_aTVlghKtWj479SKr_JmQ/viewform'
    ```

## Como Usar

1. Após configurar o código, basta rodar o script `bot.py`:

    ```bash
    python bot.py
    ```

2. O bot começará a preencher o formulário automaticamente com o nome da música e o artista, além de selecionar o turno "Noturno". Ele repetirá esse processo para cada música da playlist até que todas as faixas sejam enviadas.

3. Após cada envio, o bot clica no link "Submit another response" para enviar outra resposta até que todas as músicas da playlist sejam processadas.

4. O bot termina quando todas as músicas da playlist foram enviadas para o formulário.

## Observações

- **Certifique-se de que a playlist do Spotify não seja muito grande**, pois o bot fará um loop por cada música da playlist, o que pode demorar dependendo da quantidade de faixas.
- O formulário do Google deve ter os campos adequados para o bot preencher (Nome da Música, Artista, Turno, etc.).
- Caso o formulário do Google seja atualizado, você pode precisar ajustar os seletores do Selenium.



