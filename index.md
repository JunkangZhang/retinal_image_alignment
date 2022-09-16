<!-- ---
title: Multimodal Retina Image Alignment and Applications
--- -->

<!-- <table>
   <tr>
     <td><a href=".#people">People</a></td>
     <td><a href=".#goals">Goals</a></td>
     <td><a href=".#results">Results</a></td>
   </tr>
 </table>
 <hr> -->

<span style="color:blue;font-weight:700;font-size:25px">
  [People](#people) &ensp; &ensp; [Goals](#goals) &ensp; &ensp; [Results](#results)
</span>

# Team Members <a name="people"></a>
### Principal Investigators
{% for pi in site.data.people.pi %} {% if pi.homepage %} [{{pi.name}}]({{pi.homepage}}) ({{pi.role}}) {% else %} {{pi.name}} ({{pi.role}}) {% endif %} &ensp; | &ensp; {% endfor %}

### Research Fellows
<!-- {% assign fellows_list = site.data.people.fellows | map: "name" %}
{% assign fellows_str = fellows_list | join: "&ensp; | &ensp; " %}
{{fellows_str}} -->
{% for fellow in site.data.people.fellows %} {{fellow.name}} &ensp; | &ensp; {% endfor %}

### Students
{% for student in site.data.people.student %} [{{student.name}}]({{student.homepage}}) &ensp; | &ensp; {% endfor %}

# Major Goals <a name="goals"></a>
The objective of the project is to develop deep-learning based multimodal retinal image registration methods to help the ophthalmologist to quickly detect and diagnose retinal diseases.  Four major goals: (1). Collect and prepare a wide range of retina images/data to support algorithm development and testing; (2). Develop algorithm to align ultra-widefield, color fundus and multicolor images to help with early diagnosis of cardiovascular diseases, (3).  Develop segmentation algorithm for OCT volumes with the help of motion correction, and (4).  Evaluate and assess the ability of goals 2 and 3 in diagnosis evaluation using human experts (clinical specialist). <br>

# Results (Publications) <a name="results"></a>
{% assign papers_by_year=site.data.papers.papers | group_by: "year" | sort:"name" | reverse %}
<!-- {% assign papers=site.data.papers.papers | sort:"year", "last" | group_by: "year" %} -->
{% for paper_this_year in papers_by_year %}
### {{paper_this_year.name}}
{% for paper in paper_this_year.items %}
**{{paper.title}}** <br>
{{paper.authors}} <br>
{% if paper.journal %} *{{paper.journal}}*, {{paper.year}}. {% elsif paper.conference %} *{{paper.conference}}*, {{paper.year}}. {% endif %} <br>
{% if paper.doi %} **\[[Paper \(doi\)]({{paper.doi}})\]** &ensp; {% endif %}
{% if paper.supplementary %} **\[[Supplementary]({{paper.supplementary}})\]** &ensp; {% endif %}
{% if paper.code %} **\[[Code]({{paper.code}})\]** &ensp; {% endif %}
{% if paper.image_bar %}
<details>
	<summary>Abstract</summary>
  {{paper.abstract}}
</details>
<p align="center">
  <img src="{{site.baseurl}}{{paper.image_bar}}" >
</p>    
{% endif %}

{% endfor %}
{% endfor %}
