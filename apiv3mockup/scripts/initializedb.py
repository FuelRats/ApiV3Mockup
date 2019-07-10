import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)
from pyramid.scripts.common import parse_vars

from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    User,
    Rat
)
from ..models.meta import Base


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        user1 = User(email='user1@example.com', status='active')
        dbsession.add(user1)
        user2 = User(email='user2@example.com', status='active')
        dbsession.add(user2)
        user3 = User(email='user3@example.com', status='active')
        dbsession.add(user3)
        rat = Rat(name="rat1", platform='pc', user=user1.id)
        dbsession.add(rat)
        rat = Rat(name="rat2", platform='xb', user=user2.id)
        dbsession.add(rat)
        rat = Rat(name="rat3", platform='ps', user=user3.id)
        dbsession.add(rat)
