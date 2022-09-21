## Repository for Retinal Image Analysis project webpage

## Option 1
Directly edit the webpage in markdown `index.md`. <br>
The result is shown in https://junkangzhang.github.io/retinal_image_alignment/. 

Edit `_data/peoples.yml` to add more names. <br>
Edit `_data/papers.yml` by adding more papers. 

## Option 2
Edit `generate_md.py` to adjust the webpage `test.md`. 
Then, run `generate_md.py` locally to generate `test.md` before committing & pushing the updates. <br>
The result is shown in https://junkangzhang.github.io/retinal_image_alignment/test/. 

- Dependency<br>
`pip install bibtexparser`

Edit `_data/peoples.yml` to add more names. <br>
Edit `_data/reference.bib` to add more papers (copy \& paste bibtex available on most publishers' websites), 
and edit `_data/reference.json` accordingly. 
