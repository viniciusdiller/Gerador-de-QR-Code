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
```

### 2. Criar o Arquivo de Entrada

Crie um arquivo chamado `NovosVisitantes.xlsx` na mesma pasta dos scripts.

Este arquivo deve conter as colunas:
`Nome` `CPF` `Identificação`

**Exemplo:**

| Nome | CPF | Identificação |
| :--- | :--- | :--- |
| João Silva | 12345678900 | Visitante |
| Maria Costa | 98765432100 | Palestrante |


### 3. Executar os Scripts

**Gerar QR Codes simples**
```bash
python "QR Sem Formatação.py"
```

As imagens serão salvas na pasta:
`QR-Code-sem-formatação/`

**Gerar crachás formatados**
```bash
python "QR Formatado para Eventos.py"
```

Os crachás serão salvos na pasta:
`QR-Code-Formatado/`

---

## Dica de Uso: Leitura dos QR Codes

Para automatizar o registro de entrada, você pode usar o aplicativo **Scan to Sheets**:

1.  Faça o login no app com uma conta Google.
2.  Configure-o para apontar para uma Planilha Google (Google Sheet) específica.
3.  Ao ler o QR Code, o app envia o conteúdo (`CPF;Nome`) automaticamente para a planilha.
4.  É uma forma excelente e rápida de fazer o check-in e controle de presença.

---

## Exemplos

As pastas:

-   `QR-Code-sem-formatação`
-   `QR-Code-Formatado`

já contêm exemplos gerados pelos scripts.
