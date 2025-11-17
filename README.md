📇 Gerador de QR Code para Eventos








Este projeto contém scripts em Python para gerar:

✅ QR Codes simples
✅ Crachás completos para eventos com nome, identificação e QR integrado

Ideal para eventos, conferências, visitas técnicas, empresas e escolas.

✨ Funcionalidades
🔹 1. QR Sem Formatação — QR Sem Formatação.py

Gera apenas a imagem PNG do QR Code, contendo:

CPF;Nome

🔹 2. QR Formatado — QR Formatado para Eventos.py

Gera crachás prontos para impressão, com:

Nome do participante

Identificação (Visitante, Palestrante, etc.)

QR Code centralizado

Layout limpo e profissional

🛠️ Como Usar
1. Instalar Dependências

Certifique-se de ter Python 3 instalado.
Depois execute:

pip install pandas qrcode pillow

2. Criar o Arquivo de Entrada

Coloque na mesma pasta um arquivo chamado NovosVisitantes.xlsx contendo:

Nome	CPF	Identificação

Exemplo:
| João Silva | 12345678900 | Visitante |
| Maria Costa | 98765432100 | Palestrante |

3. Executar os Scripts
▶️ Gerar QR codes simples
python "QR Sem Formatação.py"


Saída será salva em:

QR-Code-sem-formatação/

▶️ Gerar crachás formatados
python "QR Formatado para Eventos.py"


Saída será salva em:

QR-Code-Formatado/

💡 Dica Útil: Leitura dos QR Codes

Para automatizar presença e registro de entrada, recomendo o app:

📱 Scan to Sheets

Lê QR Codes automaticamente

Envia CPF e Nome para uma Planilha Google

Ideal para controle de eventos, check-in e contagem de público

Basta configurar o app com sua conta Google.

🖼️ Exemplos

As pastas:

QR-Code-sem-formatação

QR-Code-Formatado

já incluem arquivos de exemplo para visualização.
