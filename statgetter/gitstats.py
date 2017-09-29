import git
import tempfile
import shutil
import itertools
from collections import namedtuple, defaultdict

class AuthorStats(namedtuple('AuthorStats', 'commits insertions deletions')):
    def __add__(self, other):
        return AuthorStats(
            self.commits + other.commits,
            self.insertions + other.insertions,
            self.deletions + other.deletions)


AuthorStats.add = lambda self, other: AuthorStats(
    self.added + other.added,
    self.removed + other.removed,
    self.lines + other.lines)

class RepoStats(object):
    def __init__(self, repo_url, repo):
        self._repo_url = repo_url
        self._repo = repo
        self._commits = [c for c in self._repo.iter_commits()]

    @property
    def authors(self):
        return {c.author.name for c in self._commits}

    @property
    def contributions_by_author(self):
        author_stats = [
            (c.author.name, self._file_stats_to_author_stat(c.stats.files))
            for c in self._commits]
        return self._sum_author_stats(author_stats)

    @staticmethod
    def _sum_author_stats(author_stats):
        result = defaultdict(lambda: AuthorStats(0, 0, 0))
        for name, author_stat in author_stats:
            result[name] += author_stat
        return dict(result)


    @staticmethod
    def _file_stats_to_author_stat(file_stats):
        insertions = sum([stat['insertions'] for stat in file_stats.values()])
        deletions = sum([stat['deletions'] for stat in file_stats.values()])
        return AuthorStats(1, insertions, deletions)

    def __repr__(self):
        return 'RepoStats<{}>'.format(self._repo_url)

class RemoteRepoStats(RepoStats):
    def __init__(self, repo_url):
        self._repo_path = tempfile.mkdtemp()
        repo = git.Repo.clone_from(repo_url, self._repo_path)
        super().__init__(repo_url, repo)

    def __del__(self):
        shutil.rmtree(self._repo_path)
