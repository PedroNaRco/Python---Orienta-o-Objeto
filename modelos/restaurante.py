from modelos.avaliacao import avaliacao


class restaurante:
    restaurantes = []
    
    
    def __init__(self, nome, categoria):     
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        restaurante.restaurantes.append(self)
        
    def __srt__():
        return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.media_avaliacoes} |{restaurante.ativo}')  @property
    def ativo(self):
        return 'Verdadeiro' if self._ativo else 'Falso'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        
         
    def receber_avaliacao(self, cliente, nota):
        if 0< nota <= 5:
            avaliacao = avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
            
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
