from tv_controle import Televisor, ControleRemoto


tv = Televisor('SONY', 'SONY-123')
controle = ControleRemoto(tv)
controle.sintonizaCanal('SBT')
controle.trocaCanal('SBT')
print(tv.canal_atual)

# Comentários explicativos sobre o código:

# - Importação de todas as funcionalidades do arquivo funcionalidades.py.

# - Instanciação de um televisor da marca SONY com o modelo SONY-123.

# - Instanciação de um controle remoto associado ao televisor.

# - Sintoniza o canal 'SBT' no televisor usando o controle remoto.

# - Troca o canal atual do televisor para 'SBT' usando o controle remoto.

# - Imprime o canal atual do televisor.

