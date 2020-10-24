import github
import json

config = {
    "max-concurrent-indexers" : 4,
    "dbpath" : "/database",
    "title" : "Hound for Gardener",
    "health-check-uri" : "/healthz",
    "vcs-config" : {
        "git": {
            "detect-ref" : True
        }
    },
    "repos" : {
    }
}

gh = github.Github()
 
for repository in gh.get_organization("gardener").get_repos():
    config["repos"][repository.full_name] = {}
    config["repos"][repository.full_name]["url"] = repository.clone_url
    config["repos"][repository.full_name]["ms-between-poll"] = 3600000

with open("config.json", "w") as fp:
    json.dump(config, fp, indent=4)
