# Gerador de QR Code para Eventos

Este projeto contém scripts em Python para gerar:

-   QR Codes simples
-   Crachás completos para eventos com nome, identificação e QR integrado

Ideal para eventos, conferências, visitas técnicas, empresas e escolas.

---

## Funcionalidades

### 1. QR Sem Formatação — `QR Sem Formatação.py`

Gera apenas a imagem PNG do QR Code contendo o texto:
`CPF;Nome`

---

### 2. QR Formatado — `QR Formatado para Eventos.py`

Gera crachás prontos para impressão com:

-   Nome do participante
-   Identificação (Visitante, Palestrante, etc.)
-   QR Code centralizado
-   Layout limpo e profissional

---

## Como Usar

### 1. Instalar Dependências

Certifique-se de que o Python 3 está instalado.

Depois execute:

```bash
pip install pandas qrcode pillow
