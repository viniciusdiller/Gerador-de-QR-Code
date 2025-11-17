import pandas as pd
import qrcode
import os

df = pd.read_excel("NovosVisitantes.xlsx")  # ajuste o nome do seu arquivo

os.makedirs("QR-Code-sem-formatação", exist_ok=True)

for index, row in df.iterrows():
    nome = row['Nome']
    cpf = str(row['CPF']).replace('.', '').replace('-', '')
    
    conteudo = f"{cpf};{nome}"  # simples e direto

    qr = qrcode.make(conteudo)
    qr.save(f"QR-Code-sem-formatação/{cpf.replace(' ', '_')}.png")

print("QR Codes atualizados com conteúdo compatível.")
