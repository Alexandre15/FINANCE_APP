from infra.repository.filmes_repo import Repo

repo = Repo
data = repo.select

print(data)
