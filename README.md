# :seedling: AgroSchool
<p align="center">
  <img width="460" height="300" <img alt="image.png" src="https://github.com/AdrianMichael5/agroschool/blob/main/scr/image.png?raw=true" data-hpc="true" class="Box-sc-g0xbh4-0 kzRgrI">
</p>
AgroSchool é uma plataforma de cursos online focada em agricultura, desenvolvida com Django e PostgreSQL. O objetivo é fornecer conhecimento e capacitação para agricultores, especialmente aqueles envolvidos em agricultura familiar, ajudando-os a melhorar suas práticas agrícolas e aumentar a produtividade de forma sustentável.

## :clipboard: Índice
- :earth_africa: Visão Geral
- :hammer_and_wrench: Funcionalidades
- :computer: Tecnologias Utilizadas
- :gear: Pré-requisitos
- :hammer_and_wrench: Instalação
- :rocket: Como Usar
- :scroll: Licença
- :phone: Contato

## 🌍 Visão Geral
O AgroSchool oferece cursos online que abrangem diversos temas relacionados à agricultura, incluindo técnicas de plantio, manejo de pragas, uso eficiente da água, e práticas sustentáveis. A plataforma permite que os usuários acessem materiais de aprendizado em vídeo, texto, e participem de fóruns de discussão.

## 🛠️ Funcionalidades
Catálogo de Cursos: Uma ampla variedade de cursos sobre agricultura.
Módulos de Aprendizado: Divisão de cursos em módulos com videoaulas, textos e quizzes.
Sistema de Avaliação: Testes ao final de cada módulo para avaliar o aprendizado.
Certificação: Emissão de certificados para cursos concluídos com sucesso.
Fórum de Discussão: Espaço para interação entre os usuários e instrutores.
Painel do Usuário: Gerenciamento de cursos, progresso e certificados.

## 💻 Tecnologias Utilizadas
Backend: Django (Python)
Banco de Dados: PostgreSQL
Frontend: HTML, CSS, JavaScript
Autenticação: Django Allauth
Deploy: Docker, Heroku

## ⚙️ Pré-requisitos
Python 3.8+
PostgreSQL
Git
Docker (opcional para ambiente de desenvolvimento)

## 🛠️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/agroschool.git
cd agroschool
```

### 2. Crie e ative um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/MacOS
ou
venv\Scripts\activate  # Windows
```
### 3. Instale as dependências

``` bash
pip install -r requirements.txt
```
### 4. Configurar o Banco de Dados

Crie um banco de dados PostgreSQL e configure as credenciais no arquivo settings.py.

### 5. Execute as migrações

``` bash

python manage.py migrate
```
### 6. Inicie o servidor de desenvolvimento

``` bash
python manage.py runserver
``` 

## 🚀 Como Usar
- Acesso ao Painel: Navegue até http://localhost:8000 para acessar a plataforma.
- Administração: Acesse http://localhost:8000/admin para gerenciar cursos e usuários.

## 📞 Contato
### Seu Nome - seu-email@exemplo.com
### LinkedIn: SeuPerfil
### GitHub: seu-usuario
