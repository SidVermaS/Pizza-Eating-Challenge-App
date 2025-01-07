from .cmds import intialize_cmds


def setup(app, db):
    intialize_cmds(app, db)
