 def convert_value(valor):
     try:
        if "." in valor:
            return float(valor)
        else:
            return int(valor)
     except:
        return valor

 def load_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        linhas = f.read().splitlines()

     cabecalho = linhas[0].split(",")
     dados = {col: [] for col in cabecalho}

     for linha in linhas[1:]:
        valores = linha.split(",")

        if len(valores) != len(cabecalho):
            continue

        for i in range(len(cabecalho)):
            dados[cabecalho[i]].append(convert_value(valores[i]))

     return dados