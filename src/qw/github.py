"""Github concrete service."""

import re
from collections.abc import Iterator

import github3
import keyring

import qw.service


class Issue(qw.service.Issue):
    """An issue on github."""

    ISSUE_LINK_RE = re.compile(r"#(\d+)")

    def __init__(self, issue, service) -> None:
        """
        Initialize the issue.

        Use service.get_issue(number) instead.
        """
        self.issue = issue
        self.service = service

    def number(self) -> int:
        """Get the number (human readable ID)."""
        return self.issue.number

    def title(self) -> str:
        """Get the title."""
        return self.issue.title

    def body(self) -> str:
        """Get the body text."""
        return self.issue.body

    def linked_issues(self) -> Iterator["Issue"]:
        """
        Get all the linked issues.

        This is just all the #<nnn>s from the body text.
        """
        for issue in self.ISSUE_LINK_RE.finditer(self.body()):
            yield self.service.get_issue(issue.group(1))


class Service(qw.service.GitService):
    """The github service."""

    def __init__(self, conf):
        """Log in with the gh auth token."""
        super().__init__(conf)
        token = keyring.get_password("gh:github.com", "")
        self.gh = github3.login(token=token)

    def get_issue(self, number: int):
        """Get the issue with the specified number."""
        issue = self.gh.issue(self.username, self.reponame, number)
        return Issue(issue, self)
