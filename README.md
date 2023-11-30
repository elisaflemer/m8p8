# Ponderada 8, módulo 8

Este projeto tem como objetivo gravar áudio, transcrevê-lo e traduzi-lo usando a API do OpenAI. Além disso, ele gera uma resposta de fala com base na tradução. Na lógica principal, o script verifica se o caminho do arquivo de áudio é fornecido como argumento. Se sim, ele realiza a transcrição e tradução diretamente; caso contrário, ele grava um novo arquivo de áudio, realiza a transcrição e tradução. Os resultados, incluindo a tradução, são exibidos no console, e a resposta é reproduzida como áudio.

## Como rodar

1. Clone este repositório.
   
```
git clone https://github.com/elisaflemer/m8p8
```

2. Instale as dependências

```
pip install openai wave sounddevice playsound numpy
```

3. Defina as variáveis de ambiente em um arquivo .env com a chave do OpenAI como OPENAI_API_KEY
    
4. Execute o sistema.
   
```
python translator.py
```
## Demo

[video.webm](https://github.com/elisaflemer/m8p7/assets/99259251/15ac050f-cb79-418b-9cdb-eaae77feaa41)

