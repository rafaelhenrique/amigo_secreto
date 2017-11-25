# amigo_secreto
Sistema para realizar sorteio de amigo secreto! o/

# Como instalar?

Crie um virtualenv:

```
python3.6 -m venv .venv
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
python3.6 contrib/generate_secret_key.py
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

