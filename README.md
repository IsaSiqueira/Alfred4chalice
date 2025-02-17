# Alfred para Chalice

![Alfred](https://upload.wikimedia.org/wikipedia/commons/8/80/Alfred_Thaddeus_Crane_Pennyworth.jpg)

Alfred Thaddeus Crane Pennyworth é um personagem fictício da DC Comics. Ele é mordomo e tutor do bilionário Bruce Wayne.

Alfred tem sua origem muitas vezes envolta em mistério e pouco se fala de suas atividades antes de ele se tornar mordomo da rica e tradicional família Wayne. Em algumas mini-series e edições avulsas das HQs fala-se de sua distante ligação com a Scotland Yard onde ele teria trabalhado como um de seus agentes mais discretos.

Sabe-se ainda de um passado como ator competente, tendo essa experiência na dramaturgia se provado útil em diversas ocasiões. Como, por exemplo, tendo ensinado ao Bruce, ainda jovem, como modificar sua voz para imitar as vozes de outras pessoas. Algo que se provou muito útil na criação da persona do Homem-Morcego.

Demonstra também muitas outras habilidades úteis, como conhecimentos médicos básicos, por exemplo. Contudo, fica-se com a impressão que nem Bruce Wayne conhece totalmente esse passado de seu mordomo. Muitas vezes, as palavras de Alfred são sugestões quase que subliminares que ajudam o "cruzado mascarado" na solução de enigmas complexos de crimes. Mesmo assim, Alfred, várias vezes, faz o papel de ingênuo.

## Rodando o projeto local

Primeiramente você deve instanciar o docker com o comando

```bash
make build
```

Após o build, é só rodar os testes

```bash
make test
```

## CACHE

Opções de gerenciadores de Cache para serem utilizados:

- [Walrus Cache](/docs/cache/walrus_cache.md): gerenciador baseado na lib Walrus

## SQLALCHEMY_UTILS

Opções de campos personalizados para serem utilizados na definição de um Model do SqlAlchemy

- [ImageType](/docs/sqlalchemy_utils/ImageType.md): para armazenar arquivos de imagem
- [PasswordSaltType](/docs/sqlalchemy_utils/PasswordSaltType.md): para armazenar password com salt randômico
- [PasswordType](/docs/sqlalchemy_utils/PasswordType.md): para armazenar password com salt fixo

## AUTH

Opções de authorizers para serem utilizados na definição de uma nova api

- [basic_auth_authorizer](/docs/auth/basic_auth_authorizer.md): para validação do tipo Basic Auth sem cache
- [basic_auth_cached_authorizer](/docs/auth/basic_auth_cached_authorizer.md): para validação do tipo Basic Auth com cache
- [jwt_authorizer](/docs/auth/jwt_authorizer.md): para validação do tipo token JWT

## SQS

Para utilizar o `sqs`, primeiro você deve adicionar o endereço de sua fila default na AWS as variáveis de ambiente do projeto:

```python
ALFRED_AWS_ACCESS_KEY_ID=id
ALFRED_AWS_SECRET_ACCESS_KEY=key

SQS_QUEUE_URL=endereço-da-sua-fila-default
```

Como utilizar

```python
@app.on_sqs_message(queue=SQS_QUEUE_URL)
def handle_sqs_message(event):
     alfred.sqs.handle_sqs_message(event, queue=SQS_QUEUE_URL)
```

Para multiplas filas

```python

from your.settings import SQS_SECOND_QUEUE_NAME, SQS_SECOND_QUEUE_URL

@app.on_sqs_message(queue=SQS_SECOND_QUEUE_NAME)
def handle_second_sqs_message(event):
     alfred.sqs.handle_sqs_message(event, queue_url=SQS_SECOND_QUEUE_URL)

# app.tasks.py
@SQSTask(bind=True, queue_url=SQS_SECOND_QUEUE_URL)
def task_very_important(self, charge_id):
     # very important script

```

## Feature Flag

Para utilizar o `Feature Flag`, você deve instanciar a classe FeatureFlag passando como parâmetro o `id` e `data`.

```python
from alfred.feature_flag.models import FeatureFlag

FeatureFlag(id=1, data={"foo": "bar"}).save()
```

Como acessar as informações:

- Passando o `id` no método `get_data`, você acessa os dados contido no campo `data`:

```python
flag = FeatureFlag.get_data(id=1)
```

Resposta:

```python
print(flag)

# >>> {"foo": "bar"}
```

- Caso o parâmetro `id` seja **Nulo** ou **id que não existe** o método irá retornar **None**.


# Tools

Verificação de e-mail:
- [EmailListVerifyOne](/docs/tools/email_verify.md)