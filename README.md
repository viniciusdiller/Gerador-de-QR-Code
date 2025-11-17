Gerador de QR Code para Eventos

Este projeto contém scripts em Python para gerar QR Codes a partir de uma lista de participantes, permitindo criar:

QR Codes simples (apenas a imagem do código)

Crachás completos formatados para uso em eventos

🚀 Funcionalidades
🔹 1. QR Sem Formatação (QR Sem Formatação.py)

Gera imagens PNG apenas com o QR Code.
Cada QR contém:

CPF;Nome

🔹 2. QR Formatado para Eventos (QR Formatado para Eventos.py)

Gera crachás completos com:

Nome do participante

Identificação (ex.: Visitante, Palestrante, etc.)

QR Code centralizado

Fundo branco, pronto para impressão

🛠️ Passo a Passo para Utilização
1. Preparar o Ambiente

Certifique-se de que o Python 3 está instalado.
Depois, instale as dependências:

pip install pandas qrcode pillow

2. Criar o Ficheiro de Entrada

Os scripts procuram um arquivo chamado NovosVisitantes.xlsx na mesma pasta.
Ele deve conter as colunas:

Nome	CPF	Identificação
3. Executar o Script

Você pode executar cada script conforme sua necessidade:

▶️ Gerar QR Codes simples
python "QR Sem Formatação.py"


As imagens serão salvas na pasta:

QR-Code-sem-formatação/


Cada arquivo será nomeado pelo CPF do participante.

▶️ Gerar crachás formatados
python "QR Formatado para Eventos.py"


Os crachás serão salvos na pasta:

QR-Code-Formatado/


Também com nomes baseados no CPF.

💡 Dica de Uso: Leitura dos QR Codes

Para registrar presença ou controlar acessos, os QR Codes podem ser lidos por qualquer app de scanner.

Uma opção prática é o app Scan to Sheets, que:

Lê automaticamente o QR Code

Envia o conteúdo (CPF;Nome) diretamente para uma Google Sheet

Funciona como sistema de controle de entrada em tempo real

📁 Exemplos

As pastas:

QR-Code-sem-formatação

QR-Code-Formatado

já incluem exemplos para visualizar o resultado dos scripts.
