import git
import tempfile
import shutil

class RepoStats(object):
    def __init__(self, repo_url, repo):
        self._repo_url = repo_url
        self._repo = repo
        self._commits = [c for c in self._repo.iter_commits()]

    @property
    def authors(self):
        return {c.author.name for c in self._commits}

    def __repr__(self):
        return 'RepoStats<{}>'.format(self._repo_url)

class RemoteRepoStats(RepoStats):
    def __init__(self, repo_url):
        self._repo_path = tempfile.mkdtemp()
        repo = git.Repo.clone_from(repo_url, self._repo_path)
        super().__init__(repo_url, repo)

    def __del__(self):
        shutil.rmtree(self._repo_path)
