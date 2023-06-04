from tools.parser import get_try_catchs


class StateCatch:
    PROCESSED = 'PROCESSED'
    FAILED = 'FAILED'


class Catch:
    def __init__(self, obj_exc: Exception):
        self.obj_exc = obj_exc

    def handler_error(self, handlers: list) -> tuple:
        exc_name = str(self.obj_exc.__class__.__name__)

        if exc_name not in handlers:
            raise self.obj_exc

        exceptions = get_try_catchs()
        next_line = 1

        for exc_key in exceptions:
            for idx, exc in enumerate(exceptions[exc_key]['catchs']):
                if exc_name in exc.values():
                    start = exc['num_line'] + next_line

                    if idx+1 < len(exceptions[exc_key]['catchs']):
                        end = exceptions[exc_key]['catchs'][idx+1]['num_line'] + next_line
                    else:
                        end = exceptions[exc_key]['end'] + next_line

                    jump = exceptions[exc_key]['end'] + next_line

                    return start, end, jump

        return None, None, None

    @staticmethod
    def get_handlers(tree_exc: dict) -> list:
        res = []

        for exc_key in tree_exc:
            for exc in tree_exc[exc_key]['catchs']:
                res.append(exc['obj_exc'])

        return res
