# Painel Interativo do Censo Escolar em Python

Este é o **Projeto 4** do repositório, que reúne quatro projetos sobre educação, repasse de verbas e organização e reagrupamento de dados. Ele é a versão em Python do painel do Censo Escolar feito em Excel no Projeto 2.

## Objetivo

Este painel mostra as escolas em atividade de 30 municípios de quatro regiões do estado de São Paulo (Região Metropolitana, Baixada Santista, Litoral Norte e Vale do Ribeira), com base no Censo Escolar 2024. Ele permite filtrar as escolas por região, por porte e por dependência administrativa e ver, ao mesmo tempo, o total de escolas, o total de matrículas, gráficos com as características e a infraestrutura das escolas (abastecimento de água e coleta de lixo), a localização de cada uma no mapa e a lista das escolas selecionadas. Pode ser usado para comparar rapidamente as condições das escolas entre regiões e identificar onde há mais carência de infraestrutura.

O pandas carrega e organiza os dados, e o Streamlit monta a página interativa, que roda no navegador a partir de um script.

## Como usar

**1. Pré-requisitos:** ter o Python 3 instalado.

**2. Baixar a pasta:** clone o repositório ou baixe a pasta `projeto-4-painel-censo-python` e mantenha os arquivos `painel.py` e `escolas_sp_regioes_2024_geo.csv` juntos, na mesma pasta.

**3. Instalar os pacotes:**

```bash
python -m pip install pandas streamlit
```

**4. Rodar o painel** (a partir da pasta do projeto):

```bash
python -m streamlit run Painel.py
```

O painel abre automaticamente no navegador. Se não abrir, acesse o endereço mostrado no terminal (normalmente `http://localhost:8501`).

**5. Usar os filtros:** escolha uma região, um porte e/ou uma dependência administrativa. Os indicadores, os gráficos, o mapa e a lista de escolas são recalculados juntos com as escolas selecionadas. Para ver o conjunto completo, deixe os filtros em "Todas".

## Prints do resultado

<img width="1279" height="826" alt="Captura de tela 2026-11-17 154315" src="https://github.com/user-attachments/assets/c3d22bdb-fdef-4abb-b317-791047f791e2" />
<img width="1279" height="774" alt="Captura de tela 2026-11-17 154336" src="https://github.com/user-attachments/assets/13b51bd7-4ff7-49bb-a520-1504990d0fb3" />
<img width="1279" height="830" alt="Captura de tela 2026-11-17 154401" src="https://github.com/user-attachments/assets/5e79ae40-574d-4927-a156-731e4624d2e0" />
<img width="1279" height="511" alt="Captura de tela 2026-11-17 154440" src="https://github.com/user-attachments/assets/9716de3d-9145-49f2-9b59-2cdebb7d8214" />


## Elementos do painel

| Tipo | Elemento | Coluna da base usada |
| --- | --- | --- |
| Indicador | Qtde de escolas | contagem de linhas da base filtrada |
| Indicador | Total de matrículas | `matriculas` |
| Filtro | Região | `regiao` |
| Filtro | Porte | `porte` (criada pela função `classifica_porte`) |
| Filtro | Dependência administrativa | `dependencia` |
| Gráfico de características | Escolas por porte | `porte` |
| Gráfico de características | Escolas por dependência | `dependencia` |
| Gráfico de infraestrutura | Escolas por abastecimento de água | `agua` |
| Gráfico de infraestrutura | Escolas por coleta de lixo | `lixo` |
| Mapa | Cada escola como um ponto | `latitude` e `longitude` |
| Lista | Escolas que atendem aos filtros | `regiao`, `municipio`, `escola`, `dependencia`, `matriculas` e `porte` |

O porte é calculado pelo número de matrículas da escola: até 200 matrículas é **Pequena**, de 201 a 400 é **Média** e acima de 400 é **Grande**.

## O que o painel mostra

[Escrevam aqui, depois de testar o painel, um parágrafo curto com uma diferença real entre regiões ou municípios que apareceu ao usar os filtros. Por exemplo: comparem a forma de abastecimento de água ou de coleta de lixo entre "todas as regiões" e o Vale do Ribeira, citando os números ou proporções que vocês viram no gráfico.]

## Organização do programa

O arquivo `painel.py` segue a ordem vista em aula: função, carregamento dos dados e, por fim, os comandos que montam o painel, com os filtros antes dos indicadores e dos gráficos.

| Parte do código | O que faz | Correspondente no painel do Projeto 2 (Excel) |
| --- | --- | --- |
| Função `classifica_porte` | Classifica cada escola como Pequena, Média ou Grande a partir do número de matrículas | Coluna calculada com fórmula na base |
| Carregamento dos dados | Lê o arquivo `escolas_sp_regioes_2024_geo.csv` com o pandas | Aba com a base de dados |
| Filtros | Seleção de região, porte e dependência, aplicada à base | Segmentação de dados |
| Indicadores | Quantidade de escolas e total de matrículas das escolas filtradas | Big numbers do dash |
| Gráficos | Contagem de escolas por porte, dependência, água e coleta de lixo | Gráficos dinâmicos |
| Mapa | Pontos com a latitude e a longitude das escolas filtradas | [elemento correspondente, se houver, ou "novo no Projeto 4"] |
| Lista de escolas | Tabela com as escolas que atendem aos filtros | Tabela com os dados filtrados |

## Uso de Inteligência Artificial

**Ferramenta utilizada:** Gemini

**Para que foi usada:** Explicar um erro de código

**Exemplo de prompt utilizado:** "O que é SyntaxError: unterminated string literal"

**O que foi ajustado manualmente:** A identificação e correção do erro

## Fonte de Dados

**Fonte oficial:** Censo Escolar 2024 (INEP)


**O que os dados representam:** A base reúne as escolas em atividade de 30 municípios de quatro regiões do estado de São Paulo, com suas características, sua infraestrutura e sua localização geográfica. Cada linha corresponde a uma escola. Os dados são do Censo Escolar 2024, a principal pesquisa estatística sobre a educação básica no Brasil, realizada pelo INEP.

**Estrutura:** arquivo `escolas_sp_regioes_2024_geo.csv`. Colunas usadas no painel:

| Coluna | O que representa |
| --- | --- |
| `regiao` | Região do estado: Região Metropolitana de SP, Baixada Santista, Litoral Norte ou Vale do Ribeira |
| `municipio` | Município da escola |
| `escola` | Nome da escola |
| `dependencia` | Municipal, Estadual, Federal ou Privada |
| `matriculas` | Número de matrículas da escola |
| `porte` | Pequena, Média ou Grande (criada no programa com a função `classifica_porte`, a partir de `matriculas`) |
| `agua` | Forma de abastecimento de água da escola |
| `lixo` | Forma de coleta de lixo da escola |
| `latitude`, `longitude` | Coordenadas geográficas da escola, usadas no mapa |

## Participação do Grupo

**O que aprendemos com este projeto:** Em geral, aprendemos como o pandas organiza e filtra os dados, como o Streamlit transforma um script em página interativa, e as diferenças entre fazer o painel em Excel e em Python.

**Papel de cada integrante**

- **Lorenna:** Revisou as informações e organizou o GitHub.
- **Ana Laura:** Revisou as informações e organizou o GitHub.
- **Bárbara:** Fez o README.
- **Sofia:** Fez o README.
- **Ana Luiza:** Completou o Projeto 4.
- **Caroliny:** Completou o Projeto 4.
