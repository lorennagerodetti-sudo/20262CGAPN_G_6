# Projeto 2 - Painel Censo (com Power Query)

## Objetivo
Este projeto organiza e cruza dados do Censo Escolar de 2024 em um painel (dashboard) interativo no Excel, construído com tabelas dinâmicas, gráficos dinâmicos e segmentação de dados. O objetivo é reunir, em uma única tela, informações sobre as escolas de um município escolhido pelo grupo, facilitando a visualização dos dados.

O município analisado nesta versão é **[MUNICÍPIO] - [UF]**.

## O que mudou em relação à versão anterior
- **Antes:** o painel usava um recorte já pronto da cidade de São Paulo (cerca de 8 mil linhas), colado na planilha. Dependência, Localização, Situação e Tamanho da Escola eram calculados por fórmulas do Excel (PROCV e SE) dentro da própria aba de dados.
- **Agora:** o painel usa a **base completa do Censo Escolar 2024 (todos os municípios do Brasil)**, importada via Power Query. O filtro por município é feito dentro do Power Query, de modo que as tabelas dinâmicas trabalham só com os dados do município escolhido, mesmo a base completa tendo centenas de milhares de linhas.
- O tratamento dos dados, que antes era feito por fórmulas, passou a ser feito em etapas no Power Query:
  1. Importação da base completa e das quatro tabelas auxiliares (Dependência, Localização, Localização Diferenciada e Situação).
  2. Criação de uma aba com duas células nomeadas, **UF** e **Município**, transformadas em uma consulta ("De Tabela/Intervalo").
  3. Filtro por município: o Power Query lê as células **UF** e **Município** e filtra a base completa para o município escolhido. O Merge com Inner Join previsto no roteiro não funcionou no nosso arquivo, como explicado em "Mudança durante o desenvolvimento".
  4. **Merges com Junção Esquerda Externa (Left Join)** para trazer Dependência, Localização, Localização Diferenciada e Situação.
  5. **Colunas condicionais** para Tamanho da Escola (pelas faixas de matrícula) e para os indicadores de infraestrutura: Água, Energia, Esgoto e Lixo (prioridade para a primeira coluna binária marcada com 1).
- A opção "Habilitar atualização em segundo plano" foi desmarcada na consulta principal, para que o **Atualizar Tudo** espere a consulta terminar antes de atualizar as tabelas dinâmicas.
- **Resultado:** para analisar outro município, basta trocar UF e Município nas células nomeadas e clicar em Atualizar Tudo. Todo o painel muda com um clique.

## Mudança durante o desenvolvimento
O roteiro previa filtrar a base pelo município com um **Merge de Junção Interna (Inner Join)** entre a base e a tabela de filtro. Não conseguimos fazer esse Merge funcionar da forma prevista. Por isso, o filtro foi aplicado de outro jeito.

O Power Query continua lendo as células de **UF** e **Município** e filtrando a base completa para o município escolhido. Para facilitar o uso, o arquivo tem **duas abas**:

- **Aba de filtro:** o usuário escreve o **estado (UF)** e o **município** que deseja analisar. Há instruções escritas na própria aba.
- **Aba do dashboard:** depois de preencher o filtro e clicar em **Dados > Atualizar Tudo**, o painel mostra os dados do município escolhido.

## Como usar
1. Abra o arquivo `Projeto_2_atualizado.xlsx` no Excel (a atualização via Power Query exige o Excel instalado; ela não roda no navegador).
2. Na aba `Filtro Município`, escreva o estado (UF) e o município que deseja analisar, exatamente como aparecem na base do Censo.
3. Clique em **Dados > Atualizar Tudo** e aguarde a atualização.
4. Na aba `Painel de Indicadores`, observe os dados do dashboard. Há 4 segmentações de dados: "SITUAÇÃO", "DEPENDENCIA", "LOCALIZAÇÃO" e "TAM_ESCOLAa", cada uma com diferentes categorias.
   - Clique em no máximo 1 categoria de cada segmentação. É possível combinar categorias de segmentações diferentes.
   - Analise os resultados por meio dos gráficos dinâmicos.

## Prints dos resultados
Painel com o município **Catunda**:

<img width="791" height="368" alt="image" src="https://github.com/user-attachments/assets/25071bca-a490-40fb-bfb2-9ea32a500576" /> 


Painel após trocar para o município **São Paulo** e clicar em 'Atualizar Tudo' e com segmentações aplicadas (**Tamanho da escola (baseado em critérios não oficiais), situação (ativa ou inativa), dependência (estadual, federal, municipal ou privada), localização (rural ou urbana) e localização diferenciada (não, comunidades tradicionais, terra indígena, assentamento ou comunidade quilombola)**:

<img width="778" height="359" alt="image" src="https://github.com/user-attachments/assets/450146e0-fb18-41c6-b4bf-ab78f9131fa8" />


Etapas do Power Query (painel "Etapas aplicadas" e os Merges):

<img width="680" height="346" alt="image" src="https://github.com/user-attachments/assets/af783750-80f5-47de-819f-5453fc862708" />
<img width="683" height="347" alt="image" src="https://github.com/user-attachments/assets/501e2def-f07e-4ee0-9e0d-13511df79590" />

<img width="751" height="383" alt="image" src="https://github.com/user-attachments/assets/dd4b41bd-457c-49a4-9591-b38b8cbdb36e" />
<img width="682" height="347" alt="image" src="https://github.com/user-attachments/assets/6f9983f8-bc51-4c12-a2b7-004a3f40c349" />
<img width="679" height="347" alt="image" src="https://github.com/user-attachments/assets/0d3ddff1-44e6-4295-b725-29aea6562955" />



## Uso de Inteligência Artificial
- **Ferramenta utilizada:** Claude
- **Para que foi usada:** a IA nos ajudou a organizar algumas informações e corrigir algum passo errado que estivesse travando o avanço dos processos, então algum erro de fórmula que não estávamos conseguindo corrigir sozinhas.
- **O que foi ajustado manualmente:** de forma manual conferimos a coerência dos dados, por exemplo, se o número de escolas do painel bate com o filtro, se a troca de município atualiza tudo.
## Fonte de Dados
- **Fonte oficial:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).
- **Link oficial:** `download.inep.gov.br/dados_abertos/microdados_censo_escolar_2024`
- **O que os dados representam:** as escolas de educação básica do município escolhido, com informações de dependência administrativa, localização, situação de funcionamento, infraestrutura (água, energia, esgoto e lixo) e matrículas.
- **Estrutura:** a base completa do Censo Escolar 2024 (todos os municípios) e quatro tabelas auxiliares (Dependência, Localização, Localização Diferenciada e Situação).

## Participação do Grupo
- **O que aprendemos com este projeto:** aprendemos a diferença na dinamicidade entre tratar dados com fórumlas e com o Power Query. Além disso, vimos como o Inner Join reduz uma base grande ao município escolhido e como o painel inteiro pode se atualizar com poucos cliques
- **Papel de cada integrante nesta etapa:**
  - Lorenna: elaboração do readme
  - Anna Laura: elaboração do readme
  - Bárbara: atualização do projeto
  - Sofia: atualização do projeto
  - Ana Luiza: atualização do projeto
  - Caroliny: criação da nova pasta no github, subiu os arquivos e revisou os dados
- **Como o grupo testou a atualização:** testamos com o município de São Paulo e Catunda, a Sofia, Bárbara e Ana Luiza ficaram na responsabilidade de testar o painel.
