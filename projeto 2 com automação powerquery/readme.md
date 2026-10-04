Projeto 2 - Painel Censo (com Power Query)
Objetivo

Este projeto organiza e cruza dados do Censo Escolar de 2024 em um painel (dashboard) interativo no Excel, construído com tabelas dinâmicas, gráficos dinâmicos e segmentação de dados. O objetivo é reunir, em uma única tela, informações sobre as escolas de um município escolhido pelo grupo, facilitando a visualização dos dados.

O município analisado nesta versão é [MUNICÍPIO] - [UF].

O que mudou em relação à versão anterior
Antes: o painel usava um recorte já pronto da cidade de São Paulo (cerca de 8 mil linhas), colado na planilha. Dependência, Localização, Situação e Tamanho da Escola eram calculados por fórmulas do Excel (PROCV e SE) dentro da própria aba de dados.
Agora: o painel usa a base completa do Censo Escolar 2024 (todos os municípios do Brasil), importada via Power Query. O filtro por município é feito dentro do Power Query, de modo que as tabelas dinâmicas trabalham só com os dados do município escolhido, mesmo a base completa tendo centenas de milhares de linhas.
O tratamento dos dados, que antes era feito por fórmulas, passou a ser feito em etapas no Power Query:
Importação da base completa e das quatro tabelas auxiliares (Dependência, Localização, Localização Diferenciada e Situação).
Criação de uma aba com duas células nomeadas, UF e Município, transformadas em uma consulta ("De Tabela/Intervalo").
Merge com Junção Interna (Inner Join) entre a base e essa tabela de filtro, pelos campos UF e Município ao mesmo tempo. É este passo que reduz a base ao município do grupo.
Merges com Junção Esquerda Externa (Left Join) para trazer Dependência, Localização, Localização Diferenciada e Situação.
Colunas condicionais para Tamanho da Escola (pelas faixas de matrícula) e para os indicadores de infraestrutura: Água, Energia, Esgoto e Lixo (prioridade para a primeira coluna binária marcada com 1).
A opção "Habilitar atualização em segundo plano" foi desmarcada na consulta principal, para que o Atualizar Tudo espere a consulta terminar antes de atualizar as tabelas dinâmicas.
Resultado: para analisar outro município, basta trocar UF e Município nas células nomeadas e clicar em Atualizar Tudo. Todo o painel muda com um clique.
Como usar
Abra o arquivo [NOME DO ARQUIVO].xlsx no Excel (a atualização via Power Query exige o Excel instalado; ela não roda no navegador).
Na aba [NOME DA ABA DO FILTRO], estão as células nomeadas UF e Município, com o município escolhido.
Para trocar de município:
Altere as duas células (UF e Município), escrevendo o nome exatamente como aparece na base do Censo.
Clique em Dados > Atualizar Tudo e aguarde a atualização.
Na aba Painel de Indicadores, observe os dados do dashboard. Há 4 segmentações de dados: "SITUAÇÃO", "DEPENDENCIA", "LOCALIZAÇÃO" e "TAM_ESCOLA", cada uma com diferentes categorias.
Clique em no máximo 1 categoria de cada segmentação. É possível combinar categorias de segmentações diferentes.
Analise os resultados por meio dos gráficos dinâmicos.
Prints dos resultados

Painel com o município [MUNICÍPIO A]:

[INSERIR PRINT]

Painel após trocar para o município [MUNICÍPIO B] e clicar em Atualizar Tudo:

[INSERIR PRINT]

Painel com segmentações aplicadas ([CATEGORIAS ESCOLHIDAS]):

[INSERIR PRINT]

Etapas do Power Query (painel "Etapas aplicadas" e os Merges):

[INSERIR PRINT]

Uso de Inteligência Artificial
Ferramenta utilizada: Claude
Para que foi usada: a IA nos ajudou a organizar algumas informações e corrigir algum passo errado que estivesse travando o avanço dos processos, então algum erro de fórmula que não estávamos conseguindo corrigir sozinhas.
O que foi ajustado manualmente: [DESCREVER O QUE O GRUPO CONFERIU E CORRIGIU, por exemplo se o número de escolas do painel bate com o filtro, se a troca de município atualiza tudo]
Fonte de Dados
Fonte oficial: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).
Link oficial: download.inep.gov.br/dados_abertos/microdados_censo_escolar_2024
O que os dados representam: as escolas de educação básica do município escolhido, com informações de dependência administrativa, localização, situação de funcionamento, infraestrutura (água, energia, esgoto e lixo) e matrículas.
Estrutura: a base completa do Censo Escolar 2024 (todos os municípios) e quatro tabelas auxiliares (Dependência, Localização, Localização Diferenciada e Situação). As principais colunas usadas foram: [LISTAR AS PRINCIPAIS COLUNAS].
Participação do Grupo
O que aprendemos com este projeto: aprendemos a diferença na dinamicidade entre tratar dados com fórumlas e com o Power Query. Além disso, vimos como o Inner Join reduz uma base grande ao município escolhido e como o painel inteiro pode se atualizar com poucos cliques.
Papel de cada integrante nesta etapa:
Lorenna: elaboração do readme
Anna Laura: elaboração do readme
Bárbara: [PAPEL]
Sofia: [PAPEL]
Ana Luiza: [PAPEL]
Caroliny: [PAPEL]
Como o grupo testou a atualização: [DESCREVER: quais municípios foram testados, quem testou e o que foi conferido]
