# Olá meu amigos,

## Este pequeno projeto faz parte da atividade ETL_Pipeline_SDW2023.

Observação: antes de tudo quero avisá-los que substitui a utilização do chatGpt na geração de mensagens personalizadas por uma mensagem padronizada, e substitui o banco de dados da API do santander por um arquivo local em json.

Tem o objetivo de consolidar os conceitos de ETL

**Extract (Extração):**

Nesta etapa, os dados são coletados e extraídos de várias fontes de dados, como bancos de dados, arquivos, APIs, ou qualquer outra fonte de dados relevante. O objetivo é reunir os dados brutos de várias fontes e prepará-los para processamento adicional.

**Transform (Transformação):**

Depois que os dados são extraídos, eles passam por um processo de transformação. Isso inclui limpeza, filtragem, agregação e qualquer manipulação necessária para tornar os dados adequados para análise ou armazenamento. A transformação pode envolver a conversão de formatos de dados, a eliminação de dados duplicados ou a criação de novos campos calculados.

**Load (Carregamento):**
 
Após a transformação, os dados processados e preparados são carregados em um destino, geralmente um repositório de dados, como um banco de dados relacional, um data warehouse, ou um sistema de armazenamento de dados apropriado. Os dados são organizados de uma maneira que seja fácil acessá-los e utilizá-los para análises ou relatórios.


No meu caso realizei assim:

Extract: extrai do arquivo local SDW2023.csv uma lista de Ids.
De acordo com esta lista, consigo acessar e buscar os clientes no meu banco de dados, que exemplifiquei em um arquivo local usuarios.json, gerando uma lista de usuários.

Transform: Com esta lista em mãos, insiro uma mensagem de feliz Aniversário padronizada para cada participante nesta lista.

Load: Depois, insiro esta lista com o novo conteúdo em nosso  banco de dados, o arquivo usuarios.json.
Disponibilizando esses dados atualizados para novas pesquisas e usos.

Qualquer dúvida ou sugestões, pode me mandar msg.

Bons estudos.


Para rodar este projeto, será necessário a instalação do pacote Pandas,

Se estiver utilizando o Visual Studio Code, rode o arquivo motor.py, a cada vez que você rodar este arquivo, será adicionado um news em cada usuário no arquivo usuarios.json

