
"""Phonenum - an abstraction to represent mobile phone numbers."""

"This type is meant to be used only in the classroom!"

__all__ = ["Phonenum", "phonenum_work", "phonenum_home", "phonenum_same"]

_phonenum_types_ = ["work", "home"]

def Phonenum(numstr, type):
    """constructs an instance of a phone-number."""
    num = numstr.strip()
    if len(num) is not 10:
        return None
    return (num, type.strip().lower())

def phonenum_work(tn):
    num, type = tn
    return type == "work"

def phonenum_home(tn):
    num, type = tn
    return type == "home"

def phonenum_same(this, that):
    return _phonenum_valid_(this) and _phonenum_valid_(that) and this[0] == that[0]

def _phonenum_valid_(tn):
    return isinstance(tn, tuple) and len(tn) == 2 and \
            isinstance(tn[0], str) and len(tn[0]) == 10
