import json
import locale


def _read_json(
    self,
    encoding=None,
    errors=None,
    cls=None,
    object_hook=None,
    parse_float=None,
    parse_int=None,
    parse_constant=None,
    object_pairs_hook=None,
    **json_load_kw
):
    encoding = encoding if encoding is not None else locale.getpreferredencoding()
    with self.open(mode="r", encoding=encoding, errors=errors) as f:
        return json.load(
            f,
            cls=cls,
            object_hook=object_hook,
            parse_float=parse_float,
            parse_int=parse_int,
            parse_constant=parse_constant,
            object_pairs_hook=object_pairs_hook,
            **json_load_kw
        )


def _write_json(
    self,
    obj,
    encoding=None,
    errors=None,
    newline=None,
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    cls=None,
    indent=None,
    separators=None,
    default=None,
    sort_keys=False,
    **json_dump_kw
):
    encoding = encoding if encoding is not None else locale.getpreferredencoding()
    with self.open(mode="w", encoding=encoding, errors=errors, newline=newline) as f:
        return json.dump(
            obj,
            f,
            skipkeys=skipkeys,
            ensure_ascii=ensure_ascii,
            check_circular=check_circular,
            allow_nan=allow_nan,
            cls=cls,
            indent=indent,
            separators=separators,
            default=default,
            sort_keys=sort_keys,
            **json_dump_kw
        )
