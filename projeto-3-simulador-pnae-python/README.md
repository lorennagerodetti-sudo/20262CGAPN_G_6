# Simulador PNAE – Projeto 3

## Objetivo

Este simulador, escrito em Python, calcula quanto a União repassa por ano a uma escola pública pelo Programa Nacional de Alimentação Escolar (PNAE), a partir do número de matrículas em creche, pré-escola e ensino fundamental. Ele também estima o custo anual dos **alimentos** da refeição escolar e mostra qual parcela desse custo o repasse federal consegue cobrir.

Pode ser usado para entender, com números de uma escola real, se o valor federal basta para a compra de alimentos ou se estados e municípios precisam complementar o recurso.

## Como usar

**O que é preciso ter:** Python 3 instalado. O programa não usa nenhuma biblioteca externa.

**Como rodar no terminal:**

```
python simulador_pnae.py
```

Também é possível abrir o `Projeto3.ipynb` no Jupyter e executar a célula.

**O que o programa pergunta** (todas as respostas numéricas são números inteiros, só dígitos, sem sinal, ponto ou vírgula; se digitar errado, o programa pede de novo):

| Pergunta | O que digitar |
|---|---|
| Digite seu nome | Texto livre |
| Digite o nome da escola | Texto livre |
| Dias letivos no ano | Número inteiro (ex.: `200`) |
| Matrículas na creche | Número inteiro (use `0` se não houver) |
| Matrículas na pré-escola | Número inteiro (use `0` se não houver) |
| Matrículas no ensino fundamental | Número inteiro (use `0` se não houver) |

**O que o programa mostra:** total de matrículas, porte da escola, repasse anual do PNAE, custo anual estimado dos alimentos, cobertura do repasse (%) e a diferença a ser coberta por outras fontes.

**Validação:** com 200 dias letivos, 60 alunos de creche, 80 de pré-escola e 50 de ensino fundamental, o programa devolve repasse anual de R$ 37.660,00 e porte "Pequena", o mesmo resultado do Projeto 1 (EMEB Vila Quitaúna).

## Prints do resultado

Simulador rodando com os dados da escola escolhida (200 dias letivos, 3 matrículas na creche, 2 na pré-escola e 49 no ensino fundamental):

<img src="imagens/print_3_2.jpeg" alt="Saída do simulador no terminal com o resultado da simulação" width="700">

Código do simulador (parâmetros no topo, funções em seguida e programa principal no final):

<img src="imagens/print_proejto_3.jpeg" alt="Código do simulador no Jupyter" width="700">

## Escola simulada

| Campo | Valor |
|---|---|
| Nome | EMEBS LUCIE BRAY ME |
| Código INEP | 35079042 |
| Município / UF | São Paulo / SP |
| Dependência administrativa | Municipal |
| Situação de funcionamento | Ativa |
| Matrículas na creche | 3 |
| Matrículas na pré-escola | 2 |
| Matrículas no ensino fundamental | 49 |
| Total | 54 |
| Dias letivos simulados | 200 |

### Por que essa escola

É pública (municipal), está em atividade e, entre as escolas públicas ativas da planilha, é a única com matrículas nas três etapas. Por isso **nenhuma etapa precisou ser preenchida com zero**.

### Como os dados foram encontrados

Os dados vêm da planilha do Censo Escolar 2024 (`microdados_ed_basica_2024`, arquivo `DADOS_SP`). Filtramos as escolas públicas municipais em atividade e procuramos entre elas as que tinham matrículas nas três etapas. As variáveis usadas foram:

- `NO_ENTIDADE`: nome da escola
- `NO_MUNICIPIO`: município
- `DEPENDENCIA` (e `TP_DEPENDENCIA`): dependência administrativa
- `SITUAÇÃO` (e `TP_SITUACAO_FUNCIONAMENTO`): situação de funcionamento
- `QT_MAT_INF`: matrículas da educação infantil
- `QT_MAT_BAS_0_3` e `QT_MAT_BAS_4_5`: matrículas por faixa etária
- `QT_MAT_FUND`: matrículas do ensino fundamental

### Observações e limitações

1. **Código INEP:** a planilha não tem a coluna do código INEP. O valor 35079042 foi encontrado em fontes externas que o associam a esta escola: [escol.as](https://www.escol.as/195683-emebs-lucie-bray-me) e [QEdu](https://qedu.org.br/escola/35079042-emebs-lucie-bray-me), que também indicam escola pública municipal em São Paulo/SP, em atividade. Nome, município, dependência e situação conferem com a planilha. Nenhuma dessas fontes é o próprio INEP; a verificação no [Catálogo de Escolas do INEP](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/inep-data/catalogo-de-escolas) fica como pendência.
2. **UF:** a planilha não tem coluna de UF. SP foi deduzida pelo nome do arquivo (`DADOS_SP`), pelo município (São Paulo) e pelo próprio código INEP: os dois primeiros dígitos (35) correspondem ao código IBGE do estado de São Paulo.
3. **Creche e pré-escola:** a planilha só traz `QT_MAT_INF` (5 matrículas) e as faixas etárias. Creche = `QT_MAT_BAS_0_3` (3) e pré-escola = `QT_MAT_BAS_4_5` (2). A soma (3 + 2) é igual ao total da educação infantil, então a aproximação é consistente para esta escola.
4. **Tipo de escola:** é uma Escola Municipal de Educação Bilíngue para Surdos (EMEBS), pequena (porte "Pequena" no simulador). A planilha contém apenas o município de São Paulo.
5. **Etapas com zero:** nenhuma.

## Custo dos alimentos

| Item | Informação |
|---|---|
| Valor adotado | **R$ 1,44 por refeição** (só gêneros alimentícios) |
| Fonte | Brandão, I. F. *Modelo conceitual de sistema de gestão de custos da alimentação escolar no setor público*. XXVII Congresso Brasileiro de Custos, 2020. |
| Link | <https://anaiscbc.emnuvens.com.br/anais/article/download/4758/4779/4896> |
| Data da informação | Maio de 2018 (custo padrão de gêneros alimentícios do campus Baturité do IFCE), publicado em 2020 |

**Por que esse valor.** A comparação com o repasse federal deve usar o custo dos alimentos, e não o custo total da refeição, porque a Lei nº 11.947/2009 só permite usar o recurso do PNAE na compra de gêneros alimentícios. Não existe valor oficial nacional para esse custo (o FNDE informou em 2025 que ainda não tem esse dado), e este foi o único valor encontrado que mede apenas os alimentos, sem merendeiras, gás e estrutura de cozinha.

**Ressalvas sobre a comparabilidade:**

- **Outro tipo de instituição e outro lugar:** o dado é de um campus federal no Ceará, não de uma escola municipal de São Paulo. Os preços de alimentos e o cardápio podem ser bem diferentes.
- **Outro ano:** o dado é de 2018. Com a inflação dos alimentos desde então, o custo atual tende a ser maior, o que aumentaria o custo anual estimado e reduziria a cobertura do repasse.
- **Outra etapa de ensino:** o valor não distingue creche, pré-escola e fundamental. Na prática, o custo por refeição varia com a faixa etária e com o número de refeições servidas por aluno (creches em período integral, por exemplo, servem mais de uma).

Por isso, o resultado deve ser lido como uma **ordem de grandeza**, e não como o custo exato da escola.

## Resultados e reflexão

### Resultado da simulação (200 dias letivos)

```
Total de matrículas:       54
Porte da escola:           Pequena
Repasse anual do PNAE:     R$ 6.856,00
Custo anual estimado:      R$ 15.552,00
Cobertura do repasse:      44,1%
Diferença a cobrir:        R$ 8.696,00
```

Como o cálculo foi feito:

- **Repasse:** (3 × 1,57 + 2 × 0,82 + 49 × 0,57) × 200 = R$ 6.856,00
- **Custo dos alimentos:** 54 alunos × 200 dias × R$ 1,44 = R$ 15.552,00
- **Cobertura:** 6.856 ÷ 15.552 × 100 = 44,1%
- **Diferença:** 15.552 − 6.856 = R$ 8.696,00

Em termos por aluno, o repasse equivale a cerca de R$ 0,63 por aluno por dia letivo, contra R$ 1,44 de custo estimado dos alimentos. Isso acontece em grande parte porque 49 dos 54 alunos estão no ensino fundamental, etapa de menor valor per capita (R$ 0,57).

### Reflexão

Segundo a simulação, o repasse federal cobre menos da metade (44,1%) do custo estimado dos alimentos, e mais da metade (R$ 8.696,00 por ano) precisa vir de outras fontes. A legislação prevê que o PNAE é uma complementação: estados e municípios devem completar o recurso com orçamento próprio. No caso de uma escola da capital paulista, isso depende de a prefeitura ter capacidade e disposição para fazer esse aporte.

As leituras de apoio indicam por que esse ponto é sensível. O debate sobre o financiamento da alimentação escolar mostra que os valores per capita ficaram anos sem reajuste e perderam poder de compra com a inflação dos alimentos, o que empurra uma parte maior da conta para os entes subnacionais. O Observatório da Alimentação Escolar também alerta que nem todos os municípios conseguem complementar o repasse, especialmente em regiões com menos arrecadação, o que cria desigualdade entre redes. Outro ponto levantado é que os reajustes dependem de decisão política a cada ano, e não de uma regra automática, o que dá pouca previsibilidade para quem planeja o cardápio.

Quando a diferença não é coberta pelo município ou estado, as consequências recaem sobre os alunos: cardápios com menos variedade, menos alimentos frescos e in natura, menor quantidade nas porções ou substituição por produtos mais baratos e menos nutritivos. Para muitas crianças, a refeição escolar é a principal refeição do dia, então a falta de recursos pode afetar a nutrição, a frequência e o desempenho escolar. O efeito tende a ser maior em creches e em escolas de tempo integral, que servem mais refeições por aluno.


### Simplificações do simulador

- **Anos diferentes:** as matrículas são do Censo Escolar de 2024 e os valores per capita são de 2026 (Resolução CD/FNDE nº 1/2026).
- **Três etapas apenas:** o cálculo considera só creche, pré-escola e ensino fundamental. Ensino médio, EJA, ensino integral e outras modalidades têm valores per capita próprios e não entram.
- **Uma refeição por aluno por dia:** a estimativa de custo supõe uma única refeição por aluno por dia letivo, o que subestima o custo em escolas que servem mais refeições.
- **Custo de referência externo:** o custo dos alimentos vem de outro tipo de instituição, de outro lugar e de 2018 (ver seção "Custo dos alimentos").
- **Dias letivos fixos:** todos os alunos são considerados presentes em todos os dias letivos, sem descontar faltas.

## Organização do programa

O código segue a estrutura vista em aula: parâmetros no topo, funções em seguida e programa principal no final.

| Parte | O que faz | Correspondência no Projeto 1 (Excel) |
|---|---|---|
| Parâmetros (`VALOR_CRECHE`, `VALOR_PRE_ESCOLA`, `VALOR_FUNDAMENTAL`) | Valores per capita do PNAE por aluno por dia letivo (Resolução CD/FNDE nº 1/2026) | Tabela de valores per capita |
| Parâmetro `FAIXAS_PORTE` | Faixas de matrículas para classificar o porte (Pequena, Média, Grande) | Tabela de faixas de porte usada no PROCV |
| Parâmetro `CUSTO_ALIMENTOS_REFEICAO` | Custo dos alimentos por refeição (R$ 1,44), com fonte indicada em comentário | Não existe (novo no Projeto 3) |
| `ler_numero(mensagem)` | Pede um número inteiro ≥ 0 e repete a pergunta até a pessoa digitar certo | Validação dos campos de entrada (células de dados) |
| `calcular_repasse(creche, pre_escola, fundamental, dias_letivos)` | Soma matrículas × valor per capita de cada etapa e multiplica pelos dias letivos | Fórmula do repasse anual total |
| `classificar_porte(total_matriculas)` | Devolve o porte conforme as faixas, com busca aproximada | PROCV com correspondência aproximada |
| `calcular_custo_anual(total_alunos, dias_letivos, custo_refeicao)` | Custo anual = alunos × dias letivos × custo por refeição | Não existe (novo no Projeto 3) |
| `calcular_cobertura(repasse, custo)` | Devolve a cobertura em %, a diferença a cobrir e se o repasse cobre o custo (usa `if`) | Não existe (novo no Projeto 3) |
| `formatar_reais(valor)` | Formata o número no padrão brasileiro (ex.: `R$ 1.234,50`) | Formatação de moeda das células |
| `main()` | Conversa com a pessoa, chama as funções e exibe o resultado | Painel de entrada e de resultados |

## Uso de Inteligência Artificial

**Ferramenta utilizada:** Claude (Anthropic).

**Para que foi usada:** ajuda com o uso do GitHub (criar e apagar pastas, inserir imagens no README), revisão do README e da consistência entre código e documentação, e redação do texto do README a partir das informações e dos prints do grupo.

**Exemplo de prompt utilizado:** "com base nessas infos e nos prints, faça o readme" (enviando o enunciado do Projeto 3, o texto anterior do README, o notebook e os prints do terminal).

**O que foi ajustado manualmente:** *[o grupo deve descrever aqui o que revisou e alterou depois da resposta da IA, por exemplo: conferência dos números, revisão da reflexão com as leituras, ajustes de texto.]*

## Fonte de Dados

**Fontes oficiais:** Censo Escolar 2024 (INEP) e Resolução CD/FNDE nº 1, de 18/02/2026 (DOU de 19/02/2026).

**Links oficiais:**

- Censo Escolar / Catálogo de Escolas (INEP): <https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/inep-data/catalogo-de-escolas>
- Resolução CD/FNDE nº 1/2026: *[colar aqui o link da resolução usado no Projeto 1]*

**O que os dados representam:** o Censo Escolar é a principal pesquisa estatística da educação básica no Brasil, feita anualmente pelo INEP, e traz informações sobre escolas, matrículas e infraestrutura. A resolução do FNDE define os valores per capita que o governo federal repassa por aluno, por dia letivo, para a alimentação escolar.

**Estrutura:** variáveis do Censo usadas: `NO_ENTIDADE` (nome da escola), `NO_MUNICIPIO` (município), `DEPENDENCIA` / `TP_DEPENDENCIA` (dependência administrativa), `SITUAÇÃO` / `TP_SITUACAO_FUNCIONAMENTO` (situação de funcionamento), `QT_MAT_INF` (matrículas na educação infantil), `QT_MAT_BAS_0_3` (matrículas de 0 a 3 anos, usadas como creche), `QT_MAT_BAS_4_5` (matrículas de 4 a 5 anos, usadas como pré-escola) e `QT_MAT_FUND` (matrículas no ensino fundamental).

**Custo dos alimentos:** Brandão, I. F. (2020), XXVII Congresso Brasileiro de Custos, <https://anaiscbc.emnuvens.com.br/anais/article/download/4758/4779/4896>. Dado de maio de 2018.

## Participação do Grupo

**O que aprendemos com este projeto:** *[descrever: por exemplo, como transformar uma planilha de Excel em um programa em Python com funções, como localizar dados no Censo Escolar, e como o repasse federal se compara ao custo real dos alimentos.]*

**Papel de cada integrante:**

Lorenna: Revisou as informações e organizou o github.
Anna Laura: Revisou as informações e organizou o github.
Bárbara: Fez o readme
Sofia: Fez o readme
Ana Luiza: Completou o projeto 3
Caroliny: Completou o projeto 3
