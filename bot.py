from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Suas credenciais do Spotify
SPOTIFY_CLIENT_ID = 'SUA_CLIENT_ID_AQUI'
SPOTIFY_CLIENT_SECRET = 'SEU_CLIENT_SECRET_AQUI'

# URL da playlist do Spotify
PLAYLIST_URL = 'https://open.spotify.com/playlist/6gcnqdxfF7t8RbK3fW6VYy?si=iBkqGl2ERVGjQyBCwC8ZoQ'

# URL do formulário do Google
FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSce_wQf6Jz58QZDD4di8FUfNcei6_aTVlghKtWj479SKr_JmQ/viewform'

# Autenticação no Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

# Obter o ID da playlist
playlist_id = PLAYLIST_URL.split("/")[-1].split("?")[0]

# Obter as faixas da playlist
tracks = sp.playlist_tracks(playlist_id)['items']

# Inicializando o WebDriver do Selenium
driver = webdriver.Chrome()

# Navegar até o formulário
driver.get(FORM_URL)

# Espera até que o formulário esteja totalmente carregado
wait = WebDriverWait(driver, 10)

# Loop para preencher o formulário com cada música da playlist
for item in tracks:
    track = item['track']
    music_name = track['name']  # Nome da música
    artist_name = track['artists'][0]['name']  # Nome do artista (pegando o primeiro artista)

    # Combina o nome da música e do artista no formato "nome da música - nome do artista"
    music_name_with_artist = f"{music_name} - {artist_name}"

    # Pausa antes de preencher o nome da música
    time.sleep(2)  # Espera 2 segundos antes de preencher o campo da música

    # Preenche o campo "Nome da Música" com o nome correto da música e o nome do artista
    input_musica = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "whsOnd")))
    input_musica.clear()  # Limpa o campo antes de preencher
    input_musica.send_keys(music_name_with_artist)  # Preenche com o nome da música e artista

    # Pausa antes de selecionar o turno
    time.sleep(1)  # Espera 1 segundo antes de selecionar o turno

    # Seleciona o turno "Noturno"
    turno = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio' and @aria-label='Noturno']")))
    turno.click()

    # Pausa antes de enviar o formulário
    time.sleep(2)  # Espera 2 segundos antes de enviar o formulário

    # Submete o formulário
    submit_button = driver.find_element(By.XPATH, "//span[text()='Enviar']")
    submit_button.click()

    # Aguarda a página de confirmação carregar
    time.sleep(5)  # Aguarda a página de confirmação carregar

    # Aguarda mais tempo para garantir que a transição foi concluída e o link está presente
    time.sleep(5)

    # Tentando encontrar o link "Submit another response" com diferentes abordagens
    try:
        submit_another_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'form_confirm')]")))
        submit_another_button.click()
    except Exception as e:
        print("Erro ao encontrar o link para enviar outra resposta:", e)

    # Aguarda o formulário ser carregado novamente
    time.sleep(3)

# Fecha o navegador após terminar o preenchimento
driver.quit()
