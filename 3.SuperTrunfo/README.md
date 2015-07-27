## Neo4J

### Instalação

#### Official site
http://neo4j.com

#### (optional) Setting up tutorial
http://www.delimited.io/blog/2014/1/15/getting-started-with-neo4j-on-ubuntu-server

## Python: neomodel

#### Criar um virtual environment com python2.7
virtualenv env -p python2.7

#### Entrar no virtual environment
source env/bin/activate

#### Instalar neomodel
pip install neomodel

#### Exporta database - Mudar USER e PASSWORD
export NEO4J_REST_URL=http://USER:PASSWORD@localhost:7474/db/data/

#### Para executar um arquivo
python nome_do_arquivo.py
