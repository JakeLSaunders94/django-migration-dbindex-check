# Django-migration-dbindex-checker
[![CircleCI](https://circleci.com/gh/PrimarySite/django-migration-dbindex-check/tree/master.svg?style=svg)](https://circleci.com/gh/PrimarySite/django-migration-dbindex-check/tree/master)
[![codecov](https://codecov.io/gh/PrimarySite/django-migration-dbindex-check/branch/master/graph/badge.svg?token=DBL4fCqCQq)](https://codecov.io/gh/PrimarySite/django-migration-dbindex-check)

Automatically check your Django migrations for a new db_index=True

This package checks your Django project for any migrations 
that have new database indices and lets you know where they are. 
It's designed to be implemented ad a CI check warning you before you deploy.


##Why do I need this?
The default behaviour of most SQL databases when creating a new index is to lock 
the specified table and scan each row sequentially to create the index.
On existing projects with large databases this can take some time and will cause downtime 
on your production application. This check will warn you so you can migrate out of hours, 
use Postgres' CONCURRENTLY feature or schedule downtime.


##Installation
Install from pypi - `pip install django-migration-db-index-checker`

Install from git repo - `pip install -e git+https://github.com/JakeLSaunders94/django-migration-dbindex-check.git#egg=django-migration-dbindex-check`


##Usage
The package is designed to be used from the command line: 
1. Navigate to your projects root folder.
2. python -m django-migration-db-index-checker

or 

1. python -m django-migration-db-index-checker <your_root_path>

The script will then output a list of offending migrations or stderr as per this example:

`A new db_index was added to field:<offending_field> in model:<offending_model> in 
app:<offending_app>. This was added in migration <offending_migration>.`

The script will exit with a non-zero status code if a new db_index has been found.


###Ignoring Migrations
Once you've been warned about the issue, you won't want your CI checks to fail forever.
There are two ways to ignore migrations. 

In your projects root, create a file called `migrations_check.cfg` following the example below.

```
[DJANGO_MIGRATION_DBINDEX_CHECK]
important_functionality = 4
other_service = 4
the_app = 4

exclude_paths=
    venv,
    some/other/path
```

In the top section, each variable represents an app name and the number assigned is the migration 
number ignore up to. So in this example, all migrations for the app `important_functionality`
will be ignored up to (but not including) `0004_my_migration.py`.

It's also common to want to ignore entire directories (for example your venv folder), to do this 
add your directory path to the `exclude_paths` variable. Note that this will check for each 
string anywhere in the filepath so be specific.