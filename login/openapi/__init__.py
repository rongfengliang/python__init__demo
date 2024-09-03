from importlib.util import find_spec
if not find_spec('httpx'):
    raise ImportError("httpx not found  run `pip install httpx`")