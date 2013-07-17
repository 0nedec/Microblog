#!flask/bin/python
from migrate.versioning import api
from config import SQlALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQlALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print 'Current database version: ' + str.(api.db_version(SQlALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))