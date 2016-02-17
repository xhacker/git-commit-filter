#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The main entry point. Invoke as `git-commit-filter' or `python -m `git-commit-filter'.
"""
import sys
from argparse import ArgumentParser
import subprocess

from pygit2 import init_repository
from pygit2 import GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE


def short_hash(commit):
    return str(commit.id)[:7]


def main():
    parser = ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    repo = init_repository('.')
    commits = list(repo.walk(repo.head.target, GIT_SORT_TOPOLOGICAL | GIT_SORT_REVERSE))

    total_commits = 0

    for commit in commits:
        # Skip merge commits
        if len(commit.parents) > 1:
            continue

        if len(commit.parents) == 1:
            diff = repo.diff(commit.parents[0], commit)
        else:
            diff = commit.tree.diff_to_tree(swap=True)

        if diff.stats.insertions + diff.stats.deletions > 5:
            continue

        short_message = commit.message.split('\n')[0]
        print '\033[1m\033[94m[' + short_hash(commit) + ']\033[0m', short_message

        if len(commit.parents) == 1:
            subprocess.call(['git', '--no-pager', 'diff', str(commit.id), str(commit.parents[0].id)])
            print ''
        else:
            print diff.patch

        total_commits += 1

    print str(total_commits) + ' commit(s)'


if __name__ == '__main__':
    sys.exit(main())
