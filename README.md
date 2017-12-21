# amigo_secreto
Sistema para realizar sorteio de amigo secreto! o/

IMPORTANTE: Estamos usando Python 3.6 neste projeto

# Como instalar?

Antes, verifique se você tem esses pacotes instalados (os pacotes abaixo são do Ubuntu):

```
sudo apt-get install build-essential python3-dev python3-venv python3-pip
```

Crie um virtualenv:

```
python -m venv .venv
```

Ative o virtualenv:

```
source .venv/bin/activate
```

Instale os requisitos:

```
pip install -r requirements.txt
```

Copie o exemplo de configuração de .env:

```
cp contrib/env-sample .env
```

Gere sua SECRET_KEY:

```
python contrib/generate_secret_key.py
```

Adicione a sua SECRET_KEY gerada e mude o arquivo .env conforme suas preferências:

```
vim .env
```

Execute as migrações do projeto:

```
python manage.py migrate
```

Inicie o projeto:

```
python manage.py runserver
```

# Como usar o sistema?

Crie um superuser:

```
python manage.py createsuperuser
```

Com o sistema rodando (`python manage.py runserver`) acesse `http://127.0.0.1:8000/admin` informe seu usuário e senha criados anteriormente no login.

Clique em `Participantes` e adicione os participantes do amigo secreto.

É importante que não fiquem selecionadas as opções "Escolhido" e "Sorteou", pois isso invalidará o sorteio.

Adicionados os participantes vá a tela inicial do sistema escolha seu nome e veja quem você sorteou. Feito isso os outros participantes também deverão escolher seus nomes e sortearem.

# Possíveis problemas

## wheel

Existem sistemas onde o virtualenv não colocará o pacote wheel por padrão. Nestes casos quando for instalar os requisitos de com o pip você não conseguirá compilar algumas dependências necessárias. Caso isso aconteça instale primeiramente o pacote wheel:

```
pip install wheel
```
