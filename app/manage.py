import os
import sys
from dotenv import load_dotenv


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
