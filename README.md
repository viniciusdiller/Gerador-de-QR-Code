# Gerador de QR Code para Eventos

Este projeto contém scripts em Python para gerar:

- QR Codes simples  
- Crachás completos para eventos com nome, identificação e QR integrado  

Ideal para eventos, conferências, visitas técnicas, empresas e escolas.

---

## Funcionalidades

### 1. QR Sem Formatação — `QR Sem Formatação.py`

Gera apenas a imagem PNG do QR Code contendo o texto:

CPF;Nome


---

### 2. QR Formatado — `QR Formatado para Eventos.py`

Gera crachás prontos para impressão com:

- Nome do participante  
- Identificação (Visitante, Palestrante, etc.)  
- QR Code centralizado  
- Layout limpo e profissional  

---

## Como Usar

### 1. Instalar Dependências

Certifique-se de que o Python 3 está instalado.

Depois execute:

```bash
pip install pandas qrcode pillow

2. Criar o Arquivo de Entrada

Crie um arquivo chamado NovosVisitantes.xlsx na mesma pasta dos scripts.

Este arquivo deve conter as colunas:

Nome	CPF	Identificação

Exemplo:

| João Silva | 12345678900 | Visitante |
| Maria Costa | 98765432100 | Palestrante |
3. Executar os Scripts
Gerar QR Codes simples
python "QR Sem Formatação.py"


As imagens serão salvas na pasta:

QR-Code-sem-formatação/

Gerar crachás formatados
python "QR Formatado para Eventos.py"


Os crachás serão salvos na pasta:

QR-Code-Formatado/

Dica de Uso: Leitura dos QR Codes

Para automatizar o registro de entrada, você pode usar o aplicativo Scan to Sheets:

O app lê automaticamente o QR Code

O conteúdo (CPF;Nome) é enviado para uma Planilha Google

Útil para controle de eventos e check-in

Exemplos

As pastas:

QR-Code-sem-formatação

QR-Code-Formatado

já contêm exemplos gerados pelos scripts.
