import os
from random import choice, shuffle

code_files = [
	'app.py',
	'cinematics.py',
	'projects.py',
	'static/css/index.css',
	'static/css/projects.css',
	'templates/index.html',
	'templates/projects.html',
	'cinematics.py',
	'templates/about.html',
	'static/js/index.js',
	'static/css/about.css',
]


def clean(t):
	for c in special_chars:
		t = t.replace(c, "\\" + c)
	return t

def load_cines(n=5):

	f = []
	while len(f) != n:
		c = choice(code_files)
		if c not in f:
			f.append(c)

	return [(i, f[i]) for i in range(len(f))]

def load_file(f):
	with open(f, 'r') as handle:
		h = ''.join([l for l in handle.readlines()])
	return [h,]

def one_block():
	code = ''
	shuffle(code_files)
	for f in code_files:
		with open(f, 'r') as handle:
			code += ''.join([l for l in handle.readlines()])
	return [code,]

if __name__ == '__main__':
	print(load_cines())