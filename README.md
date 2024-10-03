<h1 align="center"> 🦾GymTracker </h1>

## 🌍 Visão Geral
O **GymTracker** é uma aplicação web desenvolvida em Django, projetada para ajudar usuários a gerenciar suas rotinas de exercícios e monitorar seu progresso físico de maneira eficaz. O aplicativo oferece uma interface intuitiva onde os usuários podem se cadastrar, registrar seus treinos, selecionar exercícios específicos para diferentes grupos musculares e planejar suas atividades semanais.

## Sobre o Projeto  
### Esta aplicação foi projetada para oferecer suporte a:  
  
**Iniciantes:** Orientações claras e simples para quem está começando, com treinos fáceis de seguir e dicas essenciais para evitar lesões.

**Intermediários:** Programas de treino adaptáveis, que ajudam a manter a motivação e progredir de forma constante.  

**Avançados:** Planos de treino personalizados que desafiam e ajudam a alcançar metas específicas, seja para ganho de massa muscular, perda de peso, ou melhora na performance esportiva.  

## :clipboard: Índice
- :earth_africa: Visão Geral
- :hammer_and_wrench: Funcionalidades
- 🧷 Links
- 🚚 Entrega 01
- 🚚 Entrega 02
- :computer: Tecnologias Utilizadas
- :gear: Pré-requisitos
- :hammer_and_wrench: Instalação
- :rocket: Como Usar
- :phone: Contato

## 🛠️ Funcionalidades
**Cadastro de Usuário:** Crie e gerencie seu perfil.  
**Seleção de Grupos Musculares:** Escolha quais músculos deseja focar em seus treinos.  
**Gestão de Treinos:** Cadastro e edição de treinos, permitindo acompanhamento detalhado do desempenho.  
**Sugestão de Treinos:** Receba sugestões de treinos adequados ao seu perfil e objetivos.  
**Dicas de Saúde:** Conteúdo educativo sobre nutrição e saúde para complementar o treinamento.  
**Biblioteca de Exercícios:** Acesso a um catálogo com descrições e vídeos de exercícios.   
**Monitoramento de Progresso:** Acompanhe seu progresso com gráficos e relatórios.  
**Escolha o treinador ideal para seu treino:** Escolha um dos treinadores parceiros da academia. 

## 🧷 Links
<a href="https://www.figma.com/design/ktzZ8wUvE2x2i93Ued7Yon/GymTracker-Prototipa%C3%A7%C3%A3o-Lo-fi?node-id=0-1&t=6QbpqgcsmcV8Rvh8-1">
    <img src="https://img.shields.io/badge/figma-b86e14?style=for-the-badge&logo=figma&logoColor=white" height="30px"/></a>
    
<a href="https://raulvnc.atlassian.net/jira/software/projects/GT/boards/1">
    <img src="https://img.shields.io/badge/Jira-b86e14?style=for-the-badge&logo=jira&logoColor=white" height="30px"/></a>
    
<a href="https://gymtracker-a8cdbge3d6cccqed.brazilsouth-01.azurewebsites.net/">
    <img src="https://img.shields.io/badge/SITE DO PROJETO-b86e14?style=for-the-badge&logo=google&logoColor=white" height="30px"/></a>
  
# 🚚 Entrega 01
## [Screencast Protótipo Lo-Fi](https://www.youtube.com/watch?v=edpW3PThu6E)

[![Clique para assistir o vídeo (abrirá em uma nova aba)](https://github.com/AdrianMichael5/gymtracker/blob/main/docs/screencast.png)](https://youtu.be/edpW3PThu6E)

## [Quadro&BackLog (JIRA)](https://raulvnc.atlassian.net/jira/software/projects/GT/boards/1)

[![Clique para ver o quadro do jira (abrirá em uma nova aba)](https://github.com/AdrianMichael5/gymtracker/blob/main/docs/quadro-jira.png)](https://raulvnc.atlassian.net/jira/software/projects/GT/boards/1)
[![Clique para ver o backlog do jira (abrirá em uma nova aba)](https://github.com/AdrianMichael5/gymtracker/blob/main/docs/backlog-jira.png)](https://raulvnc.atlassian.net/jira/software/projects/GT/boards/1/backlog)

# 🚚 Entrega 02

## [Screencast Primeiro Deploy](https://youtu.be/p6bjTbyv9cE)

[![Clique para assistir o vídeo (abrirá em uma nova aba)](https://github.com/AdrianMichael5/gymtracker/blob/main/docs/screencast.png)](https://youtu.be/p6bjTbyv9cE)

## [Quadro&BackLog (JIRA)](https://raulvnc.atlassian.net/jira/software/projects/GT/boards/1)
[![Clique para ver o quadro do jira (abrirá em uma nova aba)](https://github.com/user-attachments/assets/2b223cf0-0606-48c2-bf20-f07f6a72d790)](https://raulvnc.atlassian.net/jira/software/projects/GT/boards/1)
[![Clique para ver o backlog do jira (abrirá em uma nova aba)](https://github.com/user-attachments/assets/84e92b29-f0a4-4dac-ad91-db63af6fbbf9)](https://raulvnc.atlassian.net/jira/software/projects/GT/boards/1/backlog)

## 💻 Tecnologias Utilizadas
- **Backend:** Django (Python) 🐍
- **Banco de Dados:** PostgreSQL 🐘
- Frontend: HTML, CSS, JavaScript 🌐

## ⚙️ Pré-requisitos
Python 3.8+  
PostgreSQL  
Git  

## 🛠️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/AdrianMichael5/gymtracker.git
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

![Alt](https://repobeats.axiom.co/api/embed/7d9b9b486efd3bad6dc818c201a1c0354e7284d9.svg "Repobeats analytics image")

