import jinja2
import os

def templatedirs():
    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    basedirs = os.listdir(basedir)
    possibledirs = [basedir + "/" + m + "/templates/html" for m in basedirs]
    possibledirs += [basedir + "/" + m + "/templates/xml" for m in basedirs]
    possibledirs += [basedir + "/" + m + "/templates/txt" for m in basedirs]
    dirs = [dir for dir in possibledirs if os.path.exists(dir)]
    return dirs
  
_jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(templatedirs()),
    trim_blocks=True)

def render(template_name, values={}):
    template = _jinja_environment.get_template(template_name)
    return template.render(values)
