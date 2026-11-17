# Simulador PNAE – Projeto 3

## Etapa 2 – Escola escolhida (Censo Escolar 2024)

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
É pública (municipal), está em atividade e, entre as escolas públicas ativas da
planilha, é a única com matrículas nas três etapas. Por isso **nenhuma etapa
precisou ser preenchida com zero**.

### Variáveis usadas (planilha `microdados_ed_basica_2024`)
- `NO_ENTIDADE`: nome da escola
- `NO_MUNICIPIO`: município
- `DEPENDENCIA` (e `TP_DEPENDENCIA`): dependência administrativa
- `SITUAÇÃO` (e `TP_SITUACAO_FUNCIONAMENTO`): situação de funcionamento
- `QT_MAT_INF`: matrículas da educação infantil
- `QT_MAT_BAS_0_3` e `QT_MAT_BAS_4_5`: matrículas por faixa etária
- `QT_MAT_FUND`: matrículas do ensino fundamental

### Observações e limitações
1. **Código INEP:** a planilha não tem a coluna do código INEP. O valor
   35079042 foi encontrado em fontes externas que o associam a esta escola:
   escol.as (<https://www.escol.as/195683-emebs-lucie-bray-me>) e QEdu
   (<https://qedu.org.br/escola/35079042-emebs-lucie-bray-me>), que também
   indicam escola pública municipal em São Paulo/SP, em atividade. Nome,
   município, dependência e situação conferem com a planilha. Nenhuma dessas
   fontes é o próprio INEP; a verificação no Catálogo de Escolas do INEP
   (<https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/inep-data/catalogo-de-escolas>)
   fica como pendência.
2. **UF:** a planilha não tem coluna de UF. SP foi deduzida pelo nome do arquivo
   (`DADOS_SP`), pelo município (São Paulo) e pelo próprio código INEP: os dois
   primeiros dígitos (35) correspondem ao código IBGE do estado de São Paulo.
3. **Creche e pré-escola:** a planilha só traz `QT_MAT_INF` (5 matrículas) e as
   faixas etárias. Creche = `QT_MAT_BAS_0_3` (3) e pré-escola = `QT_MAT_BAS_4_5`
   (2). A soma (3 + 2) é igual ao total da educação infantil, então a
   aproximação é consistente para esta escola.
4. **Tipo de escola:** é uma Escola Municipal de Educação Bilíngue para Surdos
   (EMEBS), pequena (porte "Pequena" no simulador). A planilha contém apenas o
   município de São Paulo.
5. **Etapas com zero:** nenhuma.

## Parâmetros do simulador

- **Valores per capita do PNAE (R$ por aluno por dia letivo):** creche 1,57;
  pré-escola 0,82; fundamental 0,57. Fonte: Resolução CD/FNDE nº 1, de
  18/02/2026 (DOU de 19/02/2026).
- **`CUSTO_ALIMENTOS_REFEICAO` = R$ 1,44** (só alimentos, por refeição).
  - Fonte: Brandão, I. F. *Modelo conceitual de sistema de gestão de custos da
    alimentação escolar no setor público*. XXVII Congresso Brasileiro de
    Custos, 2020.
    <https://anaiscbc.emnuvens.com.br/anais/article/download/4758/4779/4896>
  - Dado: custo padrão de gêneros alimentícios por refeição, campus Baturité
    do IFCE, maio/2018.
  - Justificativa: não existe valor oficial nacional (o FNDE informou em 2025
    que ainda não tem esse dado). Este é o único valor encontrado que mede só
    alimentos.
  - Limitações: é de um campus federal, não de escola municipal de SP, e é de
    2018.

## Resultado da simulação (200 dias letivos)

```
Total de matrículas:       54
Porte da escola:           Pequena
Repasse anual do PNAE:     R$ 6.856,00
Custo anual estimado:      R$ 15.552,00
Cobertura do repasse:      44,1%
Diferença a cobrir:        R$ 8.696,00
```

Print do terminal: `<img width="1280" height="862" alt="print proejto 3" src="https://github.com/user-attachments/assets/26fefae2-6a44-4faf-9116-c868d5e67592" />
`<img width="1280" height="801" alt="print 3 2" src="https://github.com/user-attachments/assets/56e14df9-ff8d-4cad-9bb0-5edfc1955e08" />
).
