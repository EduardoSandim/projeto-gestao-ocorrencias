# ==========================================
# PROJETO: Sistema de Gestão de Ocorrências Urbanas
# CONCEITOS: POO, Listas e Estruturas de Controle
# ==========================================

class Ocorrencia:
    def __init__(self, id_ocorrencia, titulo, descricao, categoria):
        self.id = id_ocorrencia
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.status = "Pendente"

    def alterar_status(self, novo_status):
        self.status = novo_status

    def exibir_detalhes(self):
        print(f"[{self.id}] {self.titulo.upper()} | Categoria: {self.categoria}")
        print(f"    Status: {self.status}")
        print(f"    Descrição: {self.descricao}")
        print("-" * 40)

class GerenciadorOcorrencias:

    def __init__(self):
        self.lista_ocorrencias = []
        self.proximo_id = 1

    def cadastrar_ocorrencia(self, titulo, descricao, categoria):
        nova = Ocorrencia(self.proximo_id, titulo, descricao, categoria)
        self.lista_ocorrencias.append(nova)
        self.proximo_id += 1
        print(f"Ocorrência #{nova.id} registrada com sucesso!")

    def listar_todas(self):
        if not self.lista_ocorrencias:
            print("Nenhuma ocorrência cadastrada até o momento.")
            return
        
        print("=== RELATÓRIO DE OCORRÊNCIAS URBANAS ===")

        for oc in self.lista_ocorrencias:
            oc.exibir_detalhes()

    def atualizar_status_ocorrencia(self, id_ocorrencia, novo_status):
        for oc in self.lista_ocorrencias:
            if oc.id == id_ocorrencia:
                oc.alterar_status(novo_status)
                print(f"Status da ocorrência #{id_ocorrencia} alterado para '{novo_status}'.")
                return
        print("Ocorrência não encontrada.")

def main():
    sistema = GerenciadorOcorrencias()

    while True:
        print("--- GESTÃO DE OCORRÊNCIAS ---")
        print("1. Cadastrar Ocorrência")
        print("2. Listar Ocorrências")
        print("3. Atualizar Status de Ocorrência")
        print("4. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Título da ocorrência (ex: Buraco na via): ")
            descricao = input("Descrição detalhada: ")
            categoria = input("Categoria (Iluminação, Asfalto, Saneamento): ")
            sistema.cadastrar_ocorrencia(titulo, descricao, categoria)
        elif opcao == "2":
            sistema.listar_todas()
        elif opcao == "3":
            try:
                id_oc = int(input("Informe o ID da ocorrência: "))
                print("Status disponíveis: Pendente | Em Atendimento | Resolvido")
                novo_st = input("Novo status: ")
                sistema.atualizar_status_ocorrencia(id_oc, novo_st)
            except ValueError:
                print("Erro: Informe um número de ID válido.")
        elif opcao == "4":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()