Claro, aqui está o README.md atualizado com a adição da dica sobre o "Scan to Sheets":

Gerador de QR Code para Eventos
Este projeto contém scripts Python para gerar QR codes a partir de uma lista de participantes, criando imagens simples de QR code ou crachás formatados para eventos.

Funcionalidades
Existem dois scripts principais:

QR Sem Formatação.py: Gera imagens PNG de QR codes simples. O conteúdo de cada QR code é o CPF;Nome do participante.

QR Formatado para EventOS.py: Gera imagens PNG formatadas como crachás. Cada crachá inclui o nome do participante, a sua identificação (ex: "Visitante") e um QR code (com o conteúdo CPF;Nome), tudo centralizado num fundo branco.

Passo a Passo para Utilização
1. Preparar o Ambiente
Certifique-se de que tem o Python instalado. Em seguida, instale as bibliotecas necessárias:

Bash

pip install pandas qrcode pillow
2. Criar o Ficheiro de Entrada
Os scripts procuram um ficheiro Excel chamado NovosVisitantes.xlsx na mesma pasta. Este ficheiro deve conter as seguintes colunas:

Nome

CPF

Identificação

3. Executar o Script
Pode escolher qual script executar, dependendo da sua necessidade:

Para gerar QR codes simples:

Bash

python "QR Sem Formatação.py"
Isto criará uma pasta chamada QR-Code-sem-formatação e guardará as imagens PNG lá dentro, nomeadas pelo CPF do participante.

Para gerar crachás formatados:

Bash

python "QR Formatado para Eventos.py"
Isto criará uma pasta chamada QR-Code-Formatado e guardará os crachás PNG lá dentro, também nomeados pelo CPF.

💡 Dica de Uso: Leitura dos QR Codes
Para facilitar o controle de presença ou registo, os QR codes gerados (que contêm CPF;Nome) podem ser lidos por aplicações de scanner.

Uma opção prática é usar a aplicação "Scan to Sheets". Pode configurar esta aplicação para se conectar à sua conta Google e, ao ler um QR code, ela envia os dados lidos (o CPF e o Nome) diretamente para uma Planilha Google (Google Sheet) que pode designar, automatizando o registo de entrada.

Exemplos
As pastas QR-Code-sem-formatação e QR-Code-Formatado já contêm ficheiros de exemplo para que possa ver o resultado final de cada script.
