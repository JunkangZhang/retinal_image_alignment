import bibtexparser
import json
import yaml
import textwrap

def write_frontmatter(fp):
    text = '''---\npermalink: /test/\n---\n'''
    fp.write(textwrap.dedent(text))


if __name__=='__main__':
    bibtex_dict = bibtexparser.load(open("_data/reference.bib")).entries_dict
    reference_json = json.load(open('_data/reference.json'))
    people_yaml = yaml.load(open('_data/people.yml'))
    print(' ')

    fp_w = open('test.html', 'w')
    write_frontmatter(fp_w)
    fp_w.write('<h2 id="test-page">Test page</h2>\n')
