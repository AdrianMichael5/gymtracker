<h1 align="center"> 🦾GymTracker </h1>

<p align="center">
  <img width="440" height="360" <img alt="image.png" src="https://github.com/AdrianMichael5/gymtracker/blob/main/src/Gymtracker.png" data-hpc="true" class="Box-sc-g0xbh4-0 kzRgrI">
</p>

> O Gymtracker é uma aplicação web desenvolvida com Django e PostgreSQL que permite a criação de treinos personalizados com base em suas informações pessoais, idade, nível de condicionamento físico e metas específicas. Com uma vasta biblioteca de exercícios e planos de treino adaptados, você terá todas as ferramentas necessárias para alcançar seus objetivos de forma eficiente.

## :clipboard: Índice
- :earth_africa: Visão Geral
- :hammer_and_wrench: Funcionalidades
- :computer: Tecnologias Utilizadas
- :gear: Pré-requisitos
- :hammer_and_wrench: Instalação
- :rocket: Como Usar
- :phone: Contato

## 🌍 Visão Geral
O **Gymtracker** é uma plataforma web inovadora desenvolvida para transformar a forma como as pessoas abordam seus treinos e condicionamento físico. A proposta é oferecer uma experiência de treino personalizada e adaptada às necessidades individuais de cada usuário, utilizando tecnologia moderna para promover saúde e bem-estar.

## 🛠️ Funcionalidades
**Cadastro de Usuário:** Crie e gerencie seu perfil, informando detalhes como idade, peso, altura e metas.  
**Seleção de Grupos Musculares:** Escolha quais músculos deseja focar em seus treinos.  
**Sugestão de Treinos:** Receba sugestões de treinos adequados ao seu perfil e objetivos.  
**Treinos Específicos para** Idades: Treinos adaptados para diferentes faixas etárias.  
**Biblioteca de Exercícios:** Acesso a um catálogo com descrições e vídeos de exercícios.  
**Monitoramento de Progresso:** Acompanhe seu progresso com gráficos e relatórios.  
**Planos de Treino Personalizados:** Crie ou siga planos de treino ajustados à sua evolução.  

## Links
#### [Figma - GymTracker](https://www.figma.com/design/ktzZ8wUvE2x2i93Ued7Yon/GymTracker-Prototipa%C3%A7%C3%A3o?node-id=0-1&node-type=CANVAS&t=PNX0I5oILUylDFD8-0)

#### [Quadro do Jira]()

#### [Site do Projeto](URL)

# Entrega 01
## [Screencast Protótipo Lo-Fi]()

[![Clique para assistir o vídeo](https://github.com/AdrianMichael5/gymtracker/blob/main/src/GymTracker.png)](https://www.youtube.com/watch?v=aNw4lxtW_YY&list=PLLT61SHdeQXuxTYMoLSTrT0kRCChHpc0W&index=5)


## 💻 Tecnologias Utilizadas
- **Backend:** Django (Python) 🐍
- **Banco de Dados:** PostgreSQL 🐘
- Frontend: HTML, CSS, JavaScript 🌐

## ⚙️ Pré-requisitos
Python 3.8+  
PostgreSQL  
Git  
Docker (opcional para ambiente de desenvolvimento)

## 🛠️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/gymtracker.git
cd gymtracker
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

## 🤝 Colaboradores
<table>
  <tr>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR65dbMui6whWaxsVpnyP_A1zY2IXODEzLVoA&s" width="100px;" alt="Foto do Adrian Michael"/><br>
        <sub>
          <b>Adrian Michael</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR65dbMui6whWaxsVpnyP_A1zY2IXODEzLVoA&s" width="100px;" alt="Foto do Marcelo Henrique"/><br>
        <sub>
          <b>Marcelo Henrique</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR65dbMui6whWaxsVpnyP_A1zY2IXODEzLVoA&s" width="100px;" alt="Foto do Raul vila nova"/><br>
        <sub>
          <b>Raul Vila Nova</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR65dbMui6whWaxsVpnyP_A1zY2IXODEzLVoA&s" width="100px;" alt="Foto do Arthur Gabriel"/><br>
        <sub>
          <b>Arthur Gabriel</b>
        </sub>
      </a>
    </td>
     <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR65dbMui6whWaxsVpnyP_A1zY2IXODEzLVoA&s" width="100px;" alt="Foto do Miguel Arcanjo"/><br>
        <sub>
          <b>Miguel Arcanjo</b>
        </sub>
      </a>
    </td>
     <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR65dbMui6whWaxsVpnyP_A1zY2IXODEzLVoA&s" width="100px;" alt="Foto do Pedro Barreto"/><br>
        <sub>
          <b>Pedro Barreto</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


## 📞 Contato
### 👨‍💻 Adrian Michael
[![Adrian Michael](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adrian-michael-77b236282/)

### 📧 Email: ama3@cesar.school
___
### 👨‍💻 Marcelo Henrique
![Marcelo Henrique](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)

### 📧 Email: mhpb@cesar.school
___
### 👨‍💻 Raul Vila Nova
![Raul Vila Nova](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)

### 📧 Email: rvnc@cesar.school
___
### 👨‍💻 Arthur Gabriel
![Arthur Gabriel](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)

### 📧 Email: agts@cesar.school
___
### 👨‍💻 Miguel Arcanjo
[![Miguel Arcanjo](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/miguel-arcanjo-205455316?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)

### 📧 Email: maha@cesar.school
___
### 👨‍💻 Pedro Barreto
[![Pedro Barreto](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pedro-barreto-6417262ba?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)

### 📧 Email: pmab@cesar.school


