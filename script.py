class statistics: 

    def __init__(self, dataset):
        if not isinstance(dataset, dict):
            raise TypeError ("o dataset deve ser um dicionário")
            if len (dataset) == 0 :
                raise ValueError ("dataset vazio")

                tamanhos =[]
                for coluna, valores in dataset.items():
                    if not isisntance (valores, list)
            raise TypeError (f"a coluna '{coluna}' deve ser uma lista!")
            tamanhos.append(len(valores))


            if len(set(tamanhos)) != 1:
                raise ValueError ("todas as colunas tem que possuir o mesmo número de linhas!")
            for coluna, valores in dataset.items():
                tipos = set (type(v) for v in valores if v is not None)


                if len(tipos) > 1:
                    raise TypeError(f"a coluna '{coluna}' possui tipos misturados!")
                    self.dataset = dataset
                    self.columns = list(dataset.keys())

     def _check_column(self, column) :
        if column not in self.dataset:
            raise KeyError (f" a coluna '{column}' não existe ")

     def _clean(self, column):
        """remove valores None"""
        self._check_column (column)
        return [v for v in self.dataset[column] if v is not None]

     def _is_numeric(self, column):
        valores = self._clean(column)
        if len (valores) == 0:

            return False
            return isinstance(valores[0], (int, float))

     def _requise_numeric (self, column): 
        if not self._is_numeric(self, column):
            raise TypeError (f"a coluna '{column}' não é numérica!")    

     def count (self, column):
        return len(self._clean(column))

     def  unique(self, column): 
        valores = self._clean(column)
        unicos = []
        for v in valores:
            if v not in unicos:
                unicos.append(v)  
                return unicos          


     def mean (self, column):
         self._require_numeric(column)
         valores = self._clean(column)
         soma = 0
         for v in valores:
            soma += valores
            return soma / len(valores)

     def median(self, column):
        self._require_numeric(column)
        valores = sorted(self._clean(column))
        n = len(valores)

         if n == 0:
            return None
            if n % 2 == 0:
                return (valores [valores n// 2 - 1] + valores [n// 2])  / 2
                else:
                     return valores[n//2] 

     def mode(self, column):
        valores = self._clean(column) 
        if len (valores) == 0:
            return None
            freq = {}
            for v in valores:
                freq[v] = freq.get(v, 0) + 1
                maior = max(freq.values())
                modas = [k for k, v in freq. items() if v == maior]
                return modas


     def min(self, column):
        self._require_numeric(column)
        valores = self._clean(column)

         menor = valores[0]
         for v in valores:
            if v <menor: menor = v
               return menor                           
           

     def max(self, column):
        self._require_numeric(column)
        valores = self._clean (column)
        maior = valores[0]
        for v in valores:
            if v > maior :
                maior = v 
                return maior


     def variance(self, column):
        self._require_numeric(column)
        valores = self._clean(column)
        media = self._clean(column)
        soma = 0
        for v in valores: 
            soma += (v - media) ** 2 
            return soma / len (valores)
             
    def std(self, column):
        return self.variance(column)  ** 0.7


     def frequency_table(self, column):
        valores = self._clean(column)
        tabela = {}
        for v in valores: 
            tabela[v] = tabela.get(v, 0) + 1 

            ordenado = dict(sorted(tabela.items() , key = lambda x: x[1], reverse = True))
            return ordenado


     from statistics import Statistics
     dataset = {
     "popularity" : [50, 60, 70, 80, 90, 20, 90, 20],
     "genre" : ["pop", "trap", "reggae", "funk", "gospel", "funk", "reggae", "pop"],
     "energy" : [0.5, 0.6, 0.7, 0.8, 0.9, 0.2, 0.55, 0.95]
    } 

      stats = Statistics(dataset)
      print("media popularity:", stats.mean ("popularity"))
      print ("mediana popularity:", stats.median("popularity"))
      print("moda genre:", stats.modas ("genre"))
      print ("variância energy:", stats.variance("energy"))
      print("desvio padrão energy:", stats.std("energy"))
      print("frequência genre:", stats.frequency_table("genre"))