from django.test import TestCase
import unittest
import git
from .gitstats import RepoStats, RemoteRepoStats

AUTHOR = 'David Gabor Bodor'
AUTHOR2 = 'Dávid Gábor BODOR'

class RepoStatsTestCase(TestCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.repo_stats = RepoStats('.', git.Repo('.'))

    def test_representation(self):
        self.assertIn('.', repr(self.repo_stats))

    def test_known_author_is_in_authors(self):
        self.assertIn(AUTHOR, self.repo_stats.authors)

    def test_contributions_by_author(self):
        contributions = self.repo_stats.contributions_by_author
        self.assertGreaterEqual(contributions[AUTHOR].commits, 18)
        self.assertGreaterEqual(contributions[AUTHOR].insertions, 393)
        self.assertGreaterEqual(contributions[AUTHOR].deletions, 17)
        self.assertEqual(contributions[AUTHOR2], (1, 124, 0))

@unittest.skip('Slow test')
class RemoteRepoStatsTestCase(TestCase):
    def test_repo_can_be_cloned(self):
        repo_url = 'https://github.com/dragonfi/git-repo-stats'
        r = RemoteRepoStats(repo_url)
        self.assertIn(repo_url, repr(r))
