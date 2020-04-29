import unittest
from flask_script import Manager

from app import app


manager = Manager(app)


@manager.command
def run():
    app.run()


@manager.command
def test():
    tests = unittest.TestLoader().discover('app/test', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        return 0

    return 1


if __name__ == '__main__':
    manager.run()

