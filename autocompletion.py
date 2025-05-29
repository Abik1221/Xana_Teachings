import jedi

def auto_complete(code, column, line):
    script = jedi.Script(code)
    return [c.name for c in script.complete(line, column)]