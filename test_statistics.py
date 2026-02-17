from statistics import Statistics

def run_tests():

    dataset = {
        "idade": [20, 25, 30, 25, 40],
        "nome": ["Ana", "João", "Ana", "Maria", "João"],
        "altura": [1.70, 1.80, 1.65, 1.70, 1.90]
    }

    stats = Statistics(dataset)

    print("count:", stats.count("idade"))
    print("unique:", stats.unique("nome"))
    print("frequency:", stats.frequency("nome"))

    print("min:", stats.min("idade"))
    print("max:", stats.max("idade"))
    print("mean:", stats.mean("idade"))
    print("median:", stats.median("idade"))
    print("mode:", stats.mode("idade"))
    print("variance:", stats.variance("idade"))
    print("std:", stats.std("idade"))

    try:
        stats.mean("nome")
    except TypeError:
        print("Erro corretamente tratado para coluna categórica")

if _name_ == "_main_":
    run_tests()