"""gcs_upload/__init__.py"""
import argparse


def cmd_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'upload_dirs',
        default='build',
        nargs='+',
        help='The directories that should be uploaded',
    )


def main() -> None:
    pass


if __name__=='__main__':
    main()
