from infra.repository.filmes_repo import Repo

repo = Repo

repo.insertar("Alita2", "Ação", 2026)
repo.deletar("Batman")
data = repo.select

print(data)
