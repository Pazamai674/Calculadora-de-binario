import re

def processar_slot_unico(slot_entrada):
    # Regex para identificar o documento (numeros, pontos, tracos e barras) no final da string
    match = re.search(r"^(.*?)\s*([\d\.\/-]+)$", slot_entrada.strip())
    
    if match:
        nome = match.group(1).strip()
        documento = match.group(2).strip()
        return {"nome": nome, "documento": documento}
    else:
        # Caso nao encontre padrao de documento, assume que tudo e o nome
        return {"nome": slot_entrada.strip(), "documento": "Nao encontrado"}


slot_entrada = "Joao da Silva 123.456.789-00"

resultado = processar_slot_unico(slot_entrada)

print(f"Nome extraido: {resultado['nome']}")
print(f"Documento extraido: {resultado['documento']}")