import pandas as pd
import qrcode
import os
from PIL import Image, ImageDraw, ImageFont

# === Configurações ===
df = pd.read_excel("NovosVisitantes.xlsx")
os.makedirs("QR-Code-Formatado", exist_ok=True)

largura_cracha = 945
altura_cracha = 590

# Margens / espaçamentos
side_margin = 20
gap_after_name = 20
gap_after_qr = 20
max_name_block_height = 240   # altura máxima reservada para o nome

# Fontes
def load_font(name, size):
    try:
        return ImageFont.truetype(name, size)
    except Exception:
        return ImageFont.load_default()

font_name_family = "arialbd.ttf"  
font_id_family = "arialbd.ttf"   

# Função que quebra palavras longas
def break_long_word(word, font, max_width, draw):
    parts = []
    start = 0
    while start < len(word):
        end = start + 1
        while end <= len(word):
            bbox = draw.textbbox((0,0), word[start:end], font=font)
            w = bbox[2] - bbox[0]
            if w <= max_width:
                end += 1
            else:
                break
        if end == start + 1:
            parts.append(word[start:end])
            start = end
        else:
            parts.append(word[start:end-1])
            start = end - 1
    return parts

# Função que quebra texto em linhas respeitando max_width
def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        bbox_word = draw.textbbox((0,0), word, font=font)
        if (bbox_word[2] - bbox_word[0]) > max_width:
            parts = break_long_word(word, font, max_width, draw)
        else:
            parts = [word]

        for part in parts:
            test = (current + " " + part).strip() if current else part
            bbox_test = draw.textbbox((0,0), test, font=font)
            if (bbox_test[2] - bbox_test[0]) <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = part
    if current:
        lines.append(current)
    return [ln for ln in lines if ln != ""]

# Percorre cada participante
for index, row in df.iterrows():
    nome_original = str(row.get('Nome', '')).strip()
    partes = nome_original.split()

    if len(partes) >= 2:
        # Primeiro + último, iniciais maiúsculas
        nome = f"{partes[0]} {partes[-1]}".upper()
    else:
        nome = nome_original.upper()

    identificacao = str(row.get('Identificação', '')).strip()
    cpf = str(row.get('CPF', '')).replace('.', '').replace('-', '')

    conteudo = f"{cpf};{nome}"

    cracha = Image.new("RGB", (largura_cracha, altura_cracha), "white")
    draw = ImageDraw.Draw(cracha)

    # === Nome ===
    font_size = 56
    while True:
        font_nome = load_font(font_name_family, font_size)
        max_text_width = largura_cracha - side_margin * 2
        nome_linhas = wrap_text(nome, font_nome, max_text_width, draw)

        linha_alturas = []
        for ln in nome_linhas:
            bbox = draw.textbbox((0,0), ln, font=font_nome)
            linha_alturas.append(bbox[3] - bbox[1])
        total_name_height = sum(linha_alturas) + (len(linha_alturas)-1)*6 if linha_alturas else 0

        if total_name_height <= max_name_block_height or font_size <= 12:
            break
        font_size -= 2

    # Fonte identificação
    font_id = load_font(font_id_family, 40)
    bbox_id = draw.textbbox((0, 0), identificacao, font=font_id)
    id_height = bbox_id[3] - bbox_id[1]

    # QR Code
    qr_img = qrcode.make(conteudo).convert("RGB")
    avail_height_for_qr = altura_cracha - (total_name_height + gap_after_name + gap_after_qr + id_height + 40)
    max_qr_width = largura_cracha - side_margin*2
    qr_size = min(250, max_qr_width, int(avail_height_for_qr))
    if qr_size < 50:
        qr_size = min(max_qr_width, 250)
    qr_img = qr_img.resize((qr_size, qr_size))

    # === Centralização ===
    total_content_height = total_name_height + gap_after_name + qr_size + gap_after_qr + id_height
    y_start = (altura_cracha - total_content_height) // 2

    # Nome
    y_text = y_start
    for ln in nome_linhas:
        bbox = draw.textbbox((0, 0), ln, font=font_nome)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        draw.text(((largura_cracha - w) / 2, y_text), ln, font=font_nome, fill="black")
        y_text += h + 6

    # Identificação (vem logo depois do nome)
        bbox_id = draw.textbbox((0, 0), identificacao, font=font_id)
        w_id = bbox_id[2] - bbox_id[0]
        h_id = bbox_id[3] - bbox_id[1]
        y_id = y_text + gap_after_name
        draw.text(((largura_cracha - w_id) / 2, y_id), identificacao, font=font_id, fill="black")
        
        
        x_qr = (largura_cracha - qr_size) // 2
        y_qr = y_id + h_id + gap_after_qr
        cracha.paste(qr_img, (x_qr, y_qr))


    # Salva
    arquivo_nome = cpf
    cracha.save(f"QR-Code-Formatado/{arquivo_nome}.png", dpi=(300, 300))