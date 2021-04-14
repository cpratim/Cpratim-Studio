from github import Github
import json

github = Github()
username = 'cpratim'

def read_json(f):
    with open(f, 'r') as df:
        return json.loads(df.read())

def dump_json(f, d):
    with open(f, 'w') as df:
        json.dump(d, df, indent=4)

def get_projects():
	try:
		user = github.get_user(username)
		repos = []
		for repo in user.get_repos():
			repos.append({
				"desc": repo.description,
				"updated": str(repo.updated_at),
				"href": repo.html_url,
				"title": repo.name,
				"language": repo.language
			})
		dump_json('projects.json', repos)
		return repos
	except:
		return read_json('projects.json')