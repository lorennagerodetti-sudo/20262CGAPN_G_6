 # Projeto 1 - Simulador de Repasse do PNAE
ocê vai gerar um artefato HTML interativo (um único arquivo, autocontido) que simula o cálculo do repasse do PNAE, a partir do modelo que eu construi em Excel para o Projeto 1 do curso Análise de Dados para Pesquisas em Políticas Públicas (FGV EAESP).

Anexei dois arquivos:

1.⁠ ⁠Minha planilha Excel, com as abas Parametros_PNAE e Simulador_Escola, contendo os dados e as fórmulas.

2.⁠ ⁠Um arquivo modelo.html, que é um artefato sobre um assunto totalmente diferente (cálculo do valor atual, matemática financeira). Não use nada do conteúdo desse arquivo — nenhum dado, nenhuma fórmula, nenhum texto dele. Use apenas como referência de: paleta de cores e tipografia, formato dos cards e das tabelas, e o tipo de mecânica interativa (campos editáveis no topo, um botão que avança passo a passo reconstruindo uma tabela de resultados, valores que reagem em tempo real a mudanças nos parâmetros).

O que o artefato deve reproduzir, fielmente ao que está na minha planilha:
Uma tabela de referência com os parâmetros do PNAE (modalidades e valores per capita), extraída da aba Parametros_PNAE.
Os dados da minha escola (nome, bairro, município) e a tabela de matrículas por modalidade, com campos editáveis para o número de matrículas.
O cálculo automático de: total de matrículas, porte da escola (a mesma regra de classificação por faixas que está na minha planilha), repasse anual estimado, e o resultado da regra de elegibilidade para complementação municipal (se ela existir na minha planilha).
A simulação com o parâmetro de ajuste que criei na Tabela de Dados do Excel: um campo editável para esse fator, mostrando como matrículas e repasse mudam em tempo real.
Um mecanismo com botões que percorre, passo a passo, os mesmos cenários que estão na minha Tabela de Dados do Excel, reconstruindo a tabela de resultados cenário a cenário — não apenas mostrando o resultado final de uma vez.
Regras importantes:
Use os dados reais da minha planilha (nome da escola, matrículas, valores per capita, faixas de classificação, fórmulas). Não invente números nem modalidades que não estejam na minha planilha.
Siga o mesmo estilo visual do modelo.html anexado: paleta de cores, tipografia, formato dos cards, dos botões e da mecânica de "avançar".
O artefato deve ser um único arquivo HTML, sem dependências externas (sem CDN, sem chamadas à internet, sem fontes externas), porque será usado sem acesso à web.
Reproduza as fórmulas da minha planilha com a mesma lógica (soma, PROCV, SOMARPRODUTO, SE aninhado com E/OU, e o fator de ajuste usado na Tabela de Dados) — não simplifique nem troque por uma lógica diferente da que eu construí.
Ao final, liste rapidamente quais células da minha planilha inspiraram cada parte do artefato (preciso disso para documentar o uso de IA no portfólio do GitHub, junto com este prompt).

## Objetivo
Este projeto simula o cálculo do repasse financeiro do PNAE (Programa Nacional de Alimentação Escolar) para uma escola, com base no número de matrículas por modalidade de ensino (creche, pré-escola, fundamental, médio, EJA, indígena/quilombola e AEE) e nos valores per capita definidos para cada uma. O simulador também classifica o porte da escola, verifica elegibilidade para complementação municipal e permite testar cenários de variação nas matrículas.

## Como usar
1. Abra a planilha `Projeto_1_-_final.xlsx` para ver o simulador completo, com as fórmulas (SE, PROCV, SOMARPRODUTO e a Tabela de Dados).
2. Abra o arquivo `simulador_pnae.html` no navegador para interagir com a versão visual do simulador:
   - Edite as quantidades de matrículas por modalidade na tabela principal e veja o repasse recalculado automaticamente.
   - Use o campo de "Fator de Ajuste" para simular variações nas matrículas.
   - Clique em "Avançar cenário" para percorrer os 9 cenários da Tabela de Dados (de -20% a +20%).

## Prints do resultado
<img width="539" height="493" alt="image" src="https://github.com/user-attachments/assets/f3ce4c91-1186-4557-a3a5-fa3a9de78e35" />
<img width="1060" height="1090" alt="WhatsApp Image 2026-09-02 at 13 41 00" src="https://github.com/user-attachments/assets/356cc381-d02d-4727-a9f8-95bea443900c" />
<img width="1060" height="1090" alt="WhatsApp Image 2026-09-02 at 13 41 00" src="https://github.com/user-attachments/assets/39cd775a-0032-48d0-9cb7-8dec4aa3bb8c" /> 



## Uso de Inteligência Artificial
- **Ferramenta utilizada:** Claude (Anthropic)
- **Para que foi usada:** gerar o artefato HTML interativo do simulador, reproduzindo fielmente a lógica e os valores da planilha `Projeto_1_-_final.xlsx`
- **Exemplo de prompt utilizado:** *[colar aqui o prompt real usado pelo grupo]*
- **O que foi ajustado manualmente:** *[descrever os ajustes feitos depois da resposta da IA]*

## Fonte de Dados
- **Fonte oficial:** *[confirmar a resolução/fonte usada]*
- **Link oficial:** *[colar o link da fonte]*
- **O que os dados representam:** *[descrever]*
- **Estrutura:** *[listar colunas/variáveis usadas]*

## Participação do Grupo
- **O que aprendemos com este projeto:** *[descrever]*
- **Papel de cada integrante:**
  - *[Nome 1]: [o que fez]*
  - *[Nome 2]: [o que fez]*
  - *[Nome 3]: [o que fez]*
