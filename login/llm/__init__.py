from importlib.util import find_spec
if not find_spec('ollama'):
    raise ImportError("ollama not found run `pip install ollama` ")