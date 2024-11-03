from modelos.restaurante import restaurante

restaurante_praca = restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('pedro', 10)
restaurante_praca.receber_avaliacao('lais', 8)
restaurante_praca.receber_avaliacao('emy', 5)


def main():
    restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()