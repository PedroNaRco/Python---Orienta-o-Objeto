class restaurante:
    def __init__(this, nome, categoria):     
        this.nome = nome
        this.categoria = categoria
        this.ativo = False
        
    def __srt__():
        return f'{this.nome} | {this.categoria}'
        
restaurante_praca = restaurante('Praça', 'Gourmet')
restaurante_pizza = restaurante('Pizza', 'Italiano')

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)
print(restaurante_pizza)
