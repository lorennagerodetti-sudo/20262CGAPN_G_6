# Projeto 1 (atualizado) – Simulador de Repasse do PNAE com Automação em VBA
## O que mudou em relação à versão anterior
A versão anterior do Simulador calculava o repasse anual estimado do PNAE para
uma escola fictícia (EMEB Vila Quitaúna, Osasco/SP) e simulava cenários com um
Fator de Ajuste. Nesta versão foi incorporada uma automação em VBA que **registra
cada simulação em um banco de dados dentro da própria planilha**.

## Objetivo
Guardar o histórico das simulações, incluindo o raciocínio de quem simulou. Assim,
a escola ou qualquer pessoa que reabra a planilha vê não só o resultado numérico,
mas também por que aquele Fator de Ajuste parecia razoável naquele momento.

Exemplo: uma funcionária da secretaria simula 5% a menos de matrículas e justifica
que, pelo Censo, o número de nascidos está diminuindo. A simulação fica gravada
na aba `Banco_de_Dados` para consulta futura.

## Como usar
1. Abra a [planilha_de_Simulador_Repasse_Pnae](ativ.erica.xlsm) e clique em **Habilitar Conteúdo/Macros**.
2. Na aba `Simulador_Escola`, informe seu nome no campo roxo **USUÁRIO** (F2).
3. Escolha o **Fator de Ajuste** (C26) e explique o motivo no campo **Racional da Taxa** (C25).
4. Clique no botão que executa a macro `RegistrarSimulacao`.
5. A macro valida os campos. Se estiver tudo preenchido, grava uma linha na aba
   `Banco_de_Dados` (ID, Data/Hora, Fator de Ajuste, Racional da Taxa, Total de
   Matrículas Ajustadas, Repasse Ajustado e Usuário) e limpa os campos para a
   próxima simulação.
6. Se algum campo estiver vazio (incluindo o Usuário), aparece uma mensagem de
   erro e **nada é gravado**.

> Atenção: o código VBA lê endereços fixos (C25, C26, F2). Não insira linhas ou
> colunas no meio do layout da aba `Simulador_Escola`.

## Prints do resultado
<img width="1341" height="725" alt="566310e1-d350-4255-92c5-56870fead1b3" src="https://github.com/user-attachments/assets/b35b8fdf-fc1b-4faf-b70c-c58245f1540b" />
<img width="1341" height="723" alt="14c74da0-893d-418d-9a34-eafaa8543851" src="https://github.com/user-attachments/assets/23690427-cd68-44c3-be0a-06bc3c5fca94" />
<img width="1341" height="725" alt="d54a98de-621f-41fc-b9e2-81217a7721f1" src="https://github.com/user-attachments/assets/c7cdaa90-dca3-43ef-8b13-36830448b36b" />
<img width="1341" height="725" alt="3eea1ee4-9efd-4d72-a87b-18b9da062c32" src="https://github.com/user-attachments/assets/ae1cb692-258d-48c3-a924-bc6dfa3fe1d8" />


## Automação em VBA – o que foi implementado (campo Usuário)
Seguindo a lógica de quatro passos da Aula 11 (cadastro de beneficiário):
1. **Criar o campo:** campo Usuário na tela do Simulador (célula F2, destacada em roxo).
2. **Ler o campo:** em `RegistrarSimulacao`, variável `usuario` lida da célula F2.
3. **Validar:** em `ValidarSimulacao`, se `usuario` estiver em branco, exibe erro e impede o registro.
4. **Gravar e limpar:** o usuário é gravado na coluna G do Banco de Dados e o campo é limpo em `LimparCampos`.

## Estrutura da pasta
-  – planilha habilitada para macro
- `README.md` – este arquivo
  
### Inteligência Artificial
A Inteligênicia Artificial foi utilizada foi o Claude para saber em qual linha colocar o msgErro, após subir o arquivo do excel.
Prompt: Em qual linha coloco o msgErro

### Dados
Escola, bairro e matrículas são **fictícios**, criados para fins didáticos. Valores
per capita, dias letivos e a regra de cálculo do repasse seguem a Resolução
CD/FNDE nº 1/2026 (que altera a Res. CD/FNDE nº 6/2020). A regra de elegibilidade
para complementação municipal é fictícia, apenas de exercício. Os dados da aba
`Banco_de_Dados` são simulações de teste.

### Participação
   - Bárbara: criou o campo de usuário; atualizou o projeto 1 com a implementação do campo de usuário
   - Ana Luiza: atualizou o projeto 1; tirou os prints do simulador
   - Caroliny: elaboração do README; subiu o aquivo do simulador; criou a pasta do simulador atualiazado
   - Sofia: atualizou o projeto 1
   - Lorenna: atualização e revisão do Github
   - Ana Laura: atualização e revisão do Github
