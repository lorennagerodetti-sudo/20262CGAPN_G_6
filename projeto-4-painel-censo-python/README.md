# Painel Interativo do Censo Escolar em Python

## Objetivo

Este painel mostra as escolas em atividade de 30 municípios de quatro regiões do estado de São Paulo (Região Metropolitana, Baixada Santista, Litoral Norte e Vale do Ribeira), com base no Censo Escolar 2024. Ele permite filtrar as escolas por região e por dependência administrativa e ver, ao mesmo tempo, o total de escolas, o total de matrículas, as características e a infraestrutura das escolas, a localização de cada uma no mapa e a lista completa das escolas selecionadas. Pode ser usado para comparar rapidamente as condições das escolas entre regiões e identificar onde há mais carência de infraestrutura.

É a versão em Python (pandas + Streamlit) do painel construído em Excel no Projeto 2.

## Como usar

**1. Pré-requisitos:** ter o Python 3 instalado.

**2. Baixar a pasta:** clone o repositório ou baixe a pasta `projeto-4-painel-censo-python` e mantenha os arquivos `painel.py` e `escolas_sp_regioes_2024_geo.csv` juntos, na mesma pasta.

**3. Instalar os pacotes:**

```bash
python -m pip install pandas streamlit
```

**4. Rodar o painel** (a partir da pasta do projeto):

```bash
python -m streamlit run painel.py
```

O painel abre automaticamente no navegador. Se não abrir, acesse o endereço mostrado no terminal (normalmente `http://localhost:8501`).

**5. Usar os filtros:** na barra lateral, escolha uma região e/ou uma dependência administrativa. Todos os indicadores, gráficos, o mapa e a lista de escolas são recalculados juntos com as escolas selecionadas. Para ver o estado geral, deixe os filtros em "Todos".

## Prints do resultado

**Todas as regiões selecionadas**

![Painel com todas as regiões](prints/print_todas_regioes.png)

**Vale do Ribeira selecionado**

![Painel com o Vale do Ribeira](prints/print_vale_do_ribeira.png)

## Elementos do painel

| Tipo | Elemento | Coluna da base usada |
| --- | --- | --- |
| Indicador | Total de escolas | contagem de linhas da base filtrada |
| Indicador | Total de matrículas | [coluna de matrículas da base] |
| Filtro | Região | `regiao` |
| Filtro | Dependência administrativa | `dependencia` |
| Gráfico de características | Escolas por porte | `porte` (criada pela função `classificar_porte`) |
| Gráfico de características | Escolas por localização (urbana ou rural) | `localizacao` |
| Gráfico de infraestrutura | Escolas por forma de abastecimento de água | `agua` |
| Gráfico de infraestrutura | Escolas por forma de esgotamento sanitário | `esgoto` |
| Mapa | Cada escola como um ponto | `latitude` e `longitude` |
| Lista | Escolas que atendem aos filtros | [colunas exibidas, por exemplo `municipio`, `dependencia`, `localizacao`, `porte`] |

## O que o painel mostra

[Escrevam aqui, depois de testar o painel, um parágrafo curto com uma diferença real entre regiões ou municípios que apareceu ao usar os filtros. Por exemplo: comparem a forma de abastecimento de água ou de esgotamento sanitário entre "todas as regiões" e o Vale do Ribeira, citando os números ou proporções que vocês viram no gráfico.]

## Organização do programa

O arquivo `painel.py` segue a ordem vista em aula: função, carregamento dos dados e, por fim, os comandos que montam o painel, com os filtros antes dos indicadores e dos gráficos.

| Parte do código | O que faz | Correspondente no painel do Projeto 2 (Excel) |
| --- | --- | --- |
| Função `classificar_porte` | Classifica cada escola como Pequena, Média ou Grande a partir do número de matrículas | Coluna calculada com fórmula na base |
| Carregamento dos dados | Lê o arquivo `escolas_sp_regioes_2024_geo.csv` com o pandas | Aba com a base de dados |
| Filtros | Seleção de região e de dependência, aplicada à base inteira | Segmentação de dados |
| Indicadores | Total de escolas e total de matrículas das escolas filtradas | Big numbers do dash |
| Gráficos | Contagem de escolas por porte, localização, água e esgoto | Gráficos dinâmicos |
| Mapa | Pontos com a latitude e a longitude das escolas filtradas | [elemento correspondente, se houver, ou "novo no Projeto 4"] |
| Lista de escolas | Tabela com as escolas que atendem aos filtros | Tabela com os dados filtrados |

## Uso de Inteligência Artificial

**Ferramenta utilizada:** [nome da ferramenta, por exemplo Claude]

**Para que foi usada:** [descrevam, por exemplo: tirar dúvidas sobre o Streamlit, ajudar a adicionar o segundo filtro e os gráficos extras, revisar erros de código]

**Exemplo de prompt utilizado:** [colem aqui um prompt real usado pelo grupo]

**O que foi ajustado manualmente:** [descrevam os ajustes feitos depois da resposta da IA, por exemplo: conferência dos nomes das opções dos filtros com `value_counts()`, testes das combinações de filtros, textos do painel]

## Fonte de Dados

**Fonte oficial:** Censo Escolar 2024 (INEP)

**Link oficial:** [colem aqui o link da fonte]

**O que os dados representam:** A base reúne as escolas em atividade de 30 municípios de quatro regiões do estado de São Paulo, com suas características, sua infraestrutura e sua localização geográfica. Cada linha corresponde a uma escola. Os dados são do Censo Escolar 2024, a principal pesquisa estatística sobre a educação básica no Brasil, realizada pelo INEP.

**Estrutura:** arquivo `escolas_sp_regioes_2024_geo.csv`. Colunas usadas no painel:

| Coluna | O que representa |
| --- | --- |
| `regiao` | Região do estado: Região Metropolitana de SP, Baixada Santista, Litoral Norte ou Vale do Ribeira |
| `municipio` | Município da escola |
| `dependencia` | Federal, Estadual, Municipal ou Privada |
| `porte` | Pequena, Média ou Grande (criada no programa com a função `classificar_porte`) |
| `agua` | Principal forma de abastecimento de água |
| `esgoto` | Principal forma de esgotamento sanitário |
| `latitude`, `longitude` | Coordenadas geográficas da escola, usadas no mapa |
| [coluna de matrículas] | Número de matrículas da escola, usado no indicador e no porte |

## Participação do Grupo

**O que aprendemos com este projeto:** [descrevam, por exemplo: como o pandas organiza e filtra os dados, como o Streamlit transforma um script em página interativa, e as diferenças entre fazer o painel em Excel e em Python]

**Papel de cada integrante**

- **[Nome 1]:** [o que fez no projeto]
- **[Nome 2]:** [o que fez no projeto]
- **[Nome 3]:** [o que fez no projeto]
