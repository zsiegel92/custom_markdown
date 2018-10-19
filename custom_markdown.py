import argparse
import sys
import subprocess
from jinja2 import Template,Environment, FileSystemLoader, select_autoescape

from markdown import markdown, markdownFromFile

import pymdownx


env = Environment(
	loader = FileSystemLoader('.', followlinks=True),
	autoescape=select_autoescape([])
)
template = env.get_template('layout.html')

# TY: https://gist.github.com/jiffyclub/5015986
# template = """<!DOCTYPE html>
# <html>
# <head>
# 	<link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.0/css/bootstrap-combined.min.css" rel="stylesheet">
# 	<style>
# 		body {
# 			font-family: sans-serif;
# 		}
# 		code, pre {
# 			font-family: monospace;
# 		}
# 		h1 code,
# 		h2 code,
# 		h3 code,
# 		h4 code,
# 		h5 code,
# 		h6 code {
# 			font-size: inherit;
# 		}
# 	</style>
# </head>
# <body>
# <div class="container">
# {{content}}
# </div>
# {% for script in js %}
# 	<script src="{{script}}"></script>
# {% endfor %}
# </body>
# </html>
# """

# def parse_args(args=None):
# 	d = 'Make a complete, styled HTML document from a Markdown file.'
# 	parser = argparse.ArgumentParser(description=d)
# 	parser.add_argument('mdfile', type=argparse.FileType('r'), nargs='?',
# 						default=sys.stdin,
# 						help='File to convert. Defaults to stdin.')
# 	parser.add_argument('-o', '--out', type=argparse.FileType('w'),
# 						default=sys.stdout,
# 						help='Output file name. Defaults to stdout.')
# 	return parser.parse_args(args)

# def main(args=None):
# 	args = parse_args(args)
# 	md = args.mdfile.read()
# 	extensions = ['extra', 'smarty']
# 	html = markdown.markdown(md, extensions=extensions, output_format='html5')
# 	doc = jinja2.Template(TEMPLATE).render(content=html)
# 	args.out.write(doc)



filename = "Python12.md"
outfile = "{}.html".format(filename.rsplit(".",1)[0])




extensions = [
	'markdown.extensions.tables',
	# 'pymdownx.magiclink',
	'pymdownx.betterem',
	# 'pymdownx.tilde',
	# 'pymdownx.emoji',
	# 'pymdownx.tasklist',
	'pymdownx.superfences',
	'markdown.extensions.toc',
	'markdown.extensions.codehilite',
	"markdown.extensions.smart_strong",
	"markdown.extensions.footnotes",
	# "markdown.extensions.attr_list",
	# "markdown.extensions.def_list",
	# "markdown.extensions.abbr",
	# "pymdownx.extrarawhtml",
	"markdown.extensions.meta",
	"markdown.extensions.sane_lists",
	"markdown.extensions.smarty",
	# "markdown.extensions.wikilinks",
	# "markdown.extensions.admonition",
	"pymdownx.arithmatex"
]
extension_config = {
	'markdown.extensions.codehilite': {
		# 'noclasses ':True,
		'use_pygments':True,
		'pygments_style':'github'
	},
	# "pymdownx.magiclink": {
	# 	"repo_url_shortener": True,
	# 	"repo_url_shorthand": True,
	# 	"provider": "github",
	# 	"user": "facelessuser",
	# 	"repo": "pymdown-extensions"
	# },
	# "pymdownx.tilde": {
	# 	"subscript": False
	# },
	# "markdown.extensions.toc": {
	# 			"permalink": "\ue157"
	# 		}
}
js = [
	"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML",
]
localjs =[ "math_config.js" ]
localscripts=[]
for script in localjs:
	with open(script) as f:
		content = f.read()
	localscripts.append(content)
localjs = localscripts

with open("Python12.md") as f:
	md = f.read()

# for link in js:
# 	link= link.replace(" ","\\ ")
# 	md += '\n<script src="{}"> \n</script>\n\n'.format(link)


html=markdown(md,extension_configs=extension_config,extensions=extensions)
# doc = Template(template).render(content=html,js=js)
doc = template.render(content=html,js=js,localjs=localjs)
with open(outfile,"r+") as f:
	f.write(doc)
# html = markdownFromFile(input=filename,output=outfile,extension_configs=extension_config,extensions=extensions)


subprocess.call("source ~/.bashrc && chromelocal {}".format(outfile),shell=True)
