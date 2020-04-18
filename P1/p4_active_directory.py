#!/usr/bin/env python3

import unittest


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    def _user_in_group_cached(user, group, user_not_in_groups):
        group_name = group.get_name()
        if group_name in user_not_in_groups:
            return False
        if user in group.get_users():
            return True
        sub_groups = group.get_groups()
        if not len(sub_groups):
            return False
        user_not_in_groups.add(group_name)
        for sub_group in sub_groups:
            res = _user_in_group_cached(user, sub_group, user_not_in_groups)
            if res is True:
                return True
        return False

    if not isinstance(group, Group):
        return False
    user_not_in_groups = set()
    return _user_in_group_cached(user, group, user_not_in_groups)


class UnitTests(unittest.TestCase):
    def test_case1(self):
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")

        sub_child_user = "sub_child_user"
        sub_child.add_user(sub_child_user)

        child.add_group(sub_child)
        parent.add_group(child)

        self.assertTrue(is_user_in_group('sub_child_user', parent))
        self.assertFalse(is_user_in_group('child_user', parent))

    def test_case2(self):
        parent = Group("parent")
        child = Group("child")
        child2 = Group("child2")
        sub_child = Group("subchild")
        sub_child2 = Group("subchild2")

        sub_child_user = "sub_child_user"
        sub_child2.add_user(sub_child_user)

        child.add_group(sub_child)
        child2.add_group(sub_child2)
        parent.add_group(child)
        parent.add_group(child2)

        self.assertTrue(is_user_in_group('sub_child_user', parent))
        self.assertFalse(is_user_in_group('child_user', parent))

    def test_case3(self):
        parent = Group("parent")
        child = Group("child")
        child2 = Group("child2")
        sub_child = Group("subchild")
        sub_child2 = Group("subchild2")

        sub_child_user = "sub_child_user"
        sub_child2.add_user(sub_child_user)

        child.add_group(sub_child)
        child.add_group(sub_child2)
        child2.add_group(sub_child)
        child2.add_group(sub_child2)

        parent.add_group(child)
        parent.add_group(child2)

        self.assertTrue(is_user_in_group('sub_child_user', parent))
        self.assertFalse(is_user_in_group('child_user', parent))


if __name__ == '__main__':
    print('Running UT cases:')
    unittest.main()
