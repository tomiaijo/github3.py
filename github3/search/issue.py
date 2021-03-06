# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from github3.models import GitHubCore
from github3.issues import Issue


class IssueSearchResult(GitHubCore):
    def __init__(self, data, session=None):
        super(IssueSearchResult, self).__init__(data, session)
        result = data.copy()
        #: Score of the result
        self.score = result.pop('score')
        #: Text matches
        self.text_matches = result.pop('text_matches', [])
        #: Issue object
        self.issue = Issue(result, self)

    def _repr(self):
        return '<IssueSearchResult [{0}]>'.format(self.issue)
