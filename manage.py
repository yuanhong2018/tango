#!/usr/bin/env python
import os
import sys

print(1111111111111111)

print(88888888888888888)

print(123456789)
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
