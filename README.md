Projetos Politicos SJC
================

Ranking de Políticos da cidade de SJC

O Objetivo deste projeto é unir informações das participações dos políticos da Cidade de São José dos Campos, 

Este Software é baseado em iniciativas como o http://www.votenaweb.com.br/, http://www.politicos.org.br/?p=ranking e deputadômetro (que acabou saindo do ar http://migre.me/afezP) 

A idéia básica é unir a a forma como o "Ranking Políticos" lista e realiza os critérios de avaliação, em conjunto com as funcionalidades do "Vote na Web" no qual proporciona os usuários votarem e opinarem a respeito dos projetos de lei, desta forma serão alinhado as informações entre os políticos e a população da cidade, proporcionando um feedback efetivo sobre tudo o que acontece em nossa região.


Iniciando o desenvolvimento
================

  Instale o distribute:
  
    $ sudo apt-get install curl
    $ curl -O http://python-­‐distribute.org/distribute_setup.py 
    $ sudo python distribute_setup.py
  
  Instale o PIP e o virtualenv:
  
    $ sudo easy_install pip
    $ sudo pip install virtualenv

  Clone o repositório
    
    $ git clone git@github.com:PauloLuan/ProjetosPoliticosSJC.git
    $ cd ProjetosPoliticosSJC/projetospoliticos

  Crie um novo ambiente virtual:

    $ virtualenv --distribute --no-site-packages ProjetosPoliticosSJC
    $ source ProjetosPoliticosSJC/bin/activate

  Instale o Django no Virtualenv
    
    $ pip install django
  
  Rode o aplicativo!
    
    $ python manage.py runserver
  
  Acesse 
    
    http://localhost:8000

  Contribua! Críticas, sugestões e pull requests são bem vindos.

  Ajude-nos a construir um país mais democrático!
  <img src="http://3.bp.blogspot.com/_ayB_UOMOmWM/TI4qo3YTu-I/AAAAAAAALO8/eNQtvpCCNJA/s1600/democracia_no_brasil.jpg" width="500px"/>
