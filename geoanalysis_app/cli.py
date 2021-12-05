import os
import sys

import streamlit.cli as stcli


def run():
    directory_path = os.path.abspath(os.path.dirname(__file__))
    script_path = os.path.join(directory_path, "app.py")

    sys.argv = ["streamlit", "run", script_path]
    sys.exit(stcli.main())
