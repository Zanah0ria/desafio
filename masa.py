def gramos_a_kilogramos(gramos):
    return gramos/ 1000

def toneladas_a_kilogramos(toneladas):
    return toneladas *1000

if __name__=="__main__":
    gramos= 2.5
    kilogramos= gramos_a_kilogramos(gramos)
    print(f"{gramos} gr son equivalentes a {kilogramos}kg")