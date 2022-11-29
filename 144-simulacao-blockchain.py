# Simulação de sistema de dependência de uma blockchain

def executa(base_dir, no_dir, chain):
    caminhos = []
    base = base_dir
    no = no_dir
    chain = chain
    caminhos.append[0](base)
    caminhos.append[1](no)
    caminhos.append[2](chain)
    return caminhos

class Cluster:

    def __init__(self, bloco, params, configs):
        caminhos = executa()
        self.bloco = bloco
        self.params = params
        self.configs = configs
        self.nodes = ["bloco_01", "bloco_02", "bloco_03", "bloco_04"]
        self.cria_bloco = {
            node:executa(caminho = caminhos,
                          bloco = self.bloco,
                          params = self.params,
                          configs = self.configs) for node in self.nodes
        }