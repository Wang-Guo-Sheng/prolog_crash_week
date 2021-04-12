from pygments import highlight
from pygments.lexers import PrologLexer
from pygments.formatters import HtmlFormatter

import os
import datetime
import re


def get_time_string():
    d = datetime.datetime.now()
    return d.strftime('%Y_%m_%d_%H_%M_')


def print_inlcude(dir_fname):
    result = dict()
    tstring = "prolog_crash_week_" + re.sub(r"[/\.]", "_", dir_fname)
    result['div'] = '<div id = "includedContent_' + tstring + '"></div>'

    with open("template.js") as jstemp:
        js_content = ''.join(jstemp.readlines())
    base = "https://raw.githubusercontent.com/Wang-Guo-Sheng/prolog_crash_week/main/"
    url = base + dir_fname.replace('\\', '/').replace('.pro', '.html')
    result['js'] = js_content.replace('TSTRING', tstring).replace('URL', url)

    return result


def ruby2html(ruby_file):
    with open(ruby_file, encoding='utf-8') as prologf:
        code = prologf.readlines()
    html = highlight(''.join(code), PrologLexer(), HtmlFormatter())
    html_name = ''.join(ruby_file.split('.')[:-1]) + '.html'
    with open(html_name, 'w', encoding='utf-8') as hf:
        hf.writelines(html)


def convert_dir(directory, operation):
    results = []
    for filename in os.listdir(directory):
        if filename.endswith(".pro"):
            dir_fname = ''.join([directory, '/', filename])
            results.append(operation(dir_fname))
            continue
        else:
            continue
    return results


convert_dir('day1', ruby2html)
results = convert_dir('day1', print_inlcude)
print('\n'.join([res['div'] for res in results]))
print('\n'.join([res['js'] for res in results]))
