 # Projeto 2 - Painel Censo
 
## Objetivo
Este projeto organiza e cruza dados do Censo Escolar de 2024. Isso realizado por meio de tabelas dinâmicas, gráficos dinâmicos e segmentação. A fim de exibir informações em um única tela (dashboard), facilitando a visualização dos dados.

## Como usar
1. Abra o arquivo `Final G6_Dashboard_2024_DADOS_SP.xlsx`, para ver o simulador completo, com as ferramentas interativas (segmentação, tabelas dinâmicas e graficos dinâmicos).
2. Abra a planilha `Painel_de_Indicadores' no navegador para interagir com a versão visual do simulador:
   - Observe os dados presentes no dashboard.
   - Há 4 tabelas de segmentação de dados: "SITUAÇÃO", "DEPENDENCIA", "LOCALIZAÇÃO", "TAM_ESCOLA" com diferentes categorias cada.
   - Clique em no máximo 1 categoria de cada tabela, sendo possível combinar categorias de tabelas diferentes. 
   - Analise as segmentações de dados por meio dos gráficos dinãmicos.  

## Prints dos resultados 
Imagem da página inicial ao abrir o arquivo na planilha "Painel de Indicadores":
<img width="1087" height="638" alt="image" src="https://github.com/user-attachments/assets/17dd0fd2-88b5-44f8-b9cc-80c5703bcd65" />
Imagem da página ao clicar na categoria "Ativa" da tabela "SITUAÇÃO", na categoria "Municipal" da tabela "DEPENDENCIA", na categoria "Urbana" da tabela "LOCALIZAÇÃO" e na categoria "Média" da tabela "TAM_ESCOLA"\:
<img width="1142" height="653" alt="Captura de tela 2026-09-07 145651" src="https://github.com/user-attachments/assets/7aa9fb67-d75e-4c94-90ec-14ab9c4bea91" />

- **Ferramenta utilizada:** Claude (Anthropic)
- **Para que foi usada:** gerar o artefato HTML interativo do simulador, reproduzindo fielmente a lógica e os valores da planilha `Projeto_1_-_final.xlsx`
- **Exemplo de prompt utilizado:** Você vai gerar um artefato HTML interativo (um único arquivo, autocontido) que simula o cálculo do repasse do PNAE, a partir do modelo que eu construi em Excel para o Projeto 1 do curso Análise de Dados para Pesquisas em Políticas Públicas (FGV EAESP).

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
- **O que foi ajustado manualmente:** Nada foi ajustado manualmente após o envio do prompt para a IA.

## Fonte de Dados
- **Fonte oficial:** *Instituto Nacional de Estudos e Pesquisas Educacionais Anísio teixeira*
- **Link oficial:** *download.inep.gov.br/dados_abertos/microdados_censo_escolar_2025*
- **O que os dados representam:** *Os tipos de escola presentes no município de São Paulo*
- **Estrutura:** Ferramentas:abelas dinâmicas, gráficos dinâmicos e segmentação**

## Participação do Grupo
- **O que aprendemos com este projeto:** Aprendemos como é possível reunir dados de maneira estratégica para fins analíticos, desde a aquisição dos  dados da fonte até a montagem do dashboard. No Excel, usamos as ferramentas  (segmentação, tabelas dinâmicas e graficos dinâmicos, com isso, transformamos em uma página de site para facilitar a vizualição dos impactos quando mudamos uma categoria na tabela. O projeto foi uma boa experiência para aprender a organizar dados oficiais e a disponibilizar esses documentos de forma pública para outras pessoas terem acesso (github).
- **Papel de cada integrante:**
  - Lorenna: Criou o repositório e as pastas.
  - Caroliny: Fez o upload dos arquivos e  Editou o arquivo README.
  - Bárbara: 
  - Sofia: Criou as tabelas dinâmicas
  - Caroliny: Finalizou o Excel do projeto 1 com Ana Luiza.
