import bibtexparser
import json
import yaml
import textwrap
from collections import OrderedDict

def write_frontmatter(fp):
    text = '''---\npermalink: /test/\n---\n'''
    fp.write(text)

def write_navigation(fp):
    text = '<span style="color:blue;font-weight:700;font-size:25px">\n' \
           '[People](#people) &ensp; &ensp; ' \
           '[Goals](#goals) &ensp; &ensp; ' \
           '[Results](#results)' \
           '\n</span>\n'
    fp.write(text)

def write_people(fp, ppl):
    text = '# Team Members <a name="people"></a>\n' \
           '### Principal Investigators\n'
    for cnt, pi in enumerate(ppl['pi']):
        text += '[%s](%s) '%(pi['name'], pi['homepage']) if 'homepage' in pi.keys() else '%s '%pi['name']
        text += '(%s) '%pi['role']
        text += '&ensp; | &ensp; ' if (cnt+1)<len(ppl['pi']) else '\n'

    text += '### Research Fellows\n'
    for cnt, fe in enumerate(ppl['fellows']):
        text += '[%s](%s) '%(fe['name'], fe['homepage']) if 'homepage' in fe.keys() else '%s '%fe['name']
        text += '&ensp; | &ensp; ' if (cnt+1)<len(ppl['fellows']) else '\n'

    text += '### Students\n'
    for cnt, st in enumerate(ppl['student']):
        text += '[%s](%s) '%(st['name'], st['homepage']) if 'homepage' in st.keys() else '%s '%st['name']
        text += '&ensp; | &ensp; ' if (cnt+1)<len(ppl['student']) else '\n'

    fp_w.write(text)

def write_goal(fp):
    text = '# Major Goals <a name="goals"></a>\n' \
           'The objective of the project is to develop deep-learning based multimodal retinal image registration methods ' \
           'to help the ophthalmologist to quickly detect and diagnose retinal diseases.  Four major goals: ' \
           '(1). Collect and prepare a wide range of retina images/data to support algorithm development and testing; ' \
           '(2). Develop algorithm to align ultra-widefield, color fundus and multicolor images to help with early ' \
           'diagnosis of cardiovascular diseases, ' \
           '(3).  Develop segmentation algorithm for OCT volumes with the help of motion correction, and ' \
           '(4).  Evaluate and assess the ability of goals 2 and 3 in diagnosis evaluation using human experts ' \
           '(clinical specialist). \n'
    fp.write(text)

def process_publications(fp_w, bib, orders):
    # order_c = orders[0]
    order = orders[0]
    ko, vo, output = order['key'], order['order'], order['output']
    if type(vo) is not list:
        allvalues = list(set([bib[_k][ko] for _k in bib.keys()]))
        if vo=='ascend':
            allvalues = sorted(allvalues)
        elif vo=='descend':
            allvalues = sorted(allvalues)[::-1]
        vo = allvalues
    bibnew = OrderedDict({_k:OrderedDict() for _k in vo})
    for kb in bib.keys():
        # if bib[kb][ko] not in values
        bibnew[bib[kb][ko]][kb]= bib[kb]
    for kn in bibnew.keys():
        if output=='title':
            text = '### %s\n'%kn
            fp_w.write(text)
            print(text)
        if len(orders) > 1:
            process_publications(fp_w, bibnew[kn], orders[1:])
        else:
            for kb in bibnew[kn].keys():
                bib_c = bibnew[kn][kb]
                text = '**%s** \n' % bib_c['title']
                text += '%s \n' % bib_c['author']
                text += '*%s*, ' % bib_c['journal'] if 'journal' in bib_c.keys() else '*%s*, ' % bib_c['booktitle']
                text += '%s \n' % bib_c['year']
                text += '**\[[Paper \(link\)](%s)\]**' % ('https://doi.org/'+bib_c['doi']) if 'doi' in bib_c.keys() else ''
                text += ' &ensp; **\[[Supplementary](%s)\]**' % bib_c['supplementary'] if 'supplementary' in bib_c.keys() else ''
                text += ' &ensp; **\[[Code](%s)\]**' % bib_c['code'] if 'code' in bib_c.keys() else ''
                text += '\n'

                text += '<details> ' \
                        '<summary>Abstract</summary> ' \
                        '%s ' \
                        '</details>\n' % bib_c['abstract'] if 'abstract' in bib_c.keys() else ''

                text += '<p align="center"> ' \
                        '<img src="{{site.baseurl}}%s" > ' \
                        '</p>\n' % bib_c['image_bar'] if 'image_bar' in bib_c.keys() else ''
                fp_w.write(text)
                print(text)





def write_publication(fp, bib, att):
    text = '# Results (Publications) <a name="results"></a>\n'

if __name__=='__main__':
    bibtex_dict = OrderedDict(bibtexparser.load(open("_data/reference.bib")).entries_dict)
    reference_json = json.load(open('_data/reference.json'))
    for k1 in reference_json.keys():
        for k2 in reference_json[k1].keys():
            bibtex_dict[k1][k2] = reference_json[k1][k2]
    people_yaml = yaml.load(open('_data/people.yml'))
    print(' ')

    fp_w = open('test.md', 'w')
    write_frontmatter(fp_w)
    write_navigation(fp_w)
    write_people(fp_w, people_yaml)
    # fp_w.write('<h2 id="test-page">Test page</h2>\n')

    # 'order': None (just group), 'ascend', 'descend', [list]
    orders = [{'key': 'year', 'order': 'descend', 'output': 'title'},
              {'key': 'ENTRYTYPE', 'order': ['article', 'inproceedings'], 'output': 'tag'},
              {'key': 'type', 'order': ['engineering', 'clinical'], 'output': 'tag'}]

    process_publications(fp_w, bibtex_dict, orders)
