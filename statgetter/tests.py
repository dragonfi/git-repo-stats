from django.test import TestCase
import git
from .gitstats import RepoStats, RemoteRepoStats

AUTHOR = 'Dávid Gábor Bodor <david.gabor.bodor@gmail.com>'

class RepoStatsTestCase(TestCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.repo_stats = RepoStats('.', git.Repo('.'))

    def test_representation(self):
        self.assertIn('.', repr(self.repo_stats))


class RemoteRepoStatsTestCase(TestCase):
    def test_repo_can_be_cloned(self):
        repo_url = 'https://github.com/dragonfi/git-repo-stats'
        r = RemoteRepoStats(repo_url)
        self.assertIn(repo_url, repr(r))
