# -*- coding: utf-8 -*-
"""Tests for the checker class."""
from unittest import TestCase

from django_migration_dbindex_check.checker import DBIndexChecker


class TestWalkFiles(TestCase):
    """Tests for the _walk_files function."""

    def test_walk_files_returns_correct_files(self):
        """Function should return the correct data from the sample files."""
        checker = DBIndexChecker()
        result = checker._walk_files("example_migrations")

        assert result == {
            "important_functionality": {
                "migration_files": [
                    [
                        "0001_initial_migrations.py",
                        "example_migrations/important_functionality/"
                        "migrations/0001_initial_migrations.py",
                    ],
                    [
                        "0002_added_some_new_field.py",
                        "example_migrations/important_functionality/migrations"
                        "/0002_added_some_new_field.py",
                    ],
                    [
                        "0003_added_new_field_db_index.py",
                        "example_migrations/important_functionality/migrations/"
                        "0003_added_new_field_db_index.py",
                    ],
                ],
            },
            "other_service": {
                "migration_files": [
                    [
                        "0001_initial_migrations.py",
                        "example_migrations/other_service/"
                        "migrations/0001_initial_migrations.py",
                    ],
                ],
            },
            "the_app": {
                "migration_files": [
                    [
                        "0001_initial_migrations.py",
                        "example_migrations/the_app/" "migrations/0001_initial_migrations.py",
                    ],
                    [
                        "0002_added_index_to_existing_field.py",
                        "example_migrations/the_app/"
                        "migrations/0002_added_index_to_existing_field.py",
                    ],
                ],
            },
        }


class TestGetAllRelevantOperations(TestCase):
    """Tests for the _get_all_relevant_operations_nodes_for_file."""

    def test_function_returns_the_correct_nodes_for_example_file(self):
        """Should return the correct nodes for the example file."""
        pass
