# good-dev-practice
Espen's effort to move from writing code on and for my local PC to production quality code deployed in the cloud (AWS).

[Writing Great Python Code](https://docs.python-guide.org/#writing-great-python-code)  

## Learnt from PRs - to be moved at some point
- Be super critical of your own doc string. Check spelling, grammar, conciseness, intuitivety and don't use the doc string to describe what should or is described in the type hint (DRY).
- Simplify logic in all possible cases. 
    - `if x == "" or x is None:` --> `if not x:`
    - Avoid double negatives: `if x is not None:` --> `if x:`. 
    - Also use TKL-diagrams if needed - which cases can occur and not.
- Precise naming!
    - Class/function/variable names should be as consise and descriptive as possible.
    - Always use `snake_case` variable names in Python, also when referring to `CamelCaseClassNames`.  
    - Use pythonic naming. E.g. for functions, `date_range` > `get_date_range`.
    
- Use plenty og type annotations `stats: ClassVar[Dict[str, int]] = {}` and [PEP 526](https://www.python.org/dev/peps/pep-0526/).  

- Use helper functions within functions to keep it readable. Move large if/else or other boilerplate sections into helper functions with intuitive
names to make the main function more readable.
- First, do type check (`isinstance(value, type)`), så gjør de logiske operasjonene, ikke i en `if isinstance .. else ...`.  
- Line changes between groups of `import`s, first standard libraries, then 3rd party, then import from own modules.  

- DRY blir sjelden feil.





# Legg til på et tidspunt
https://www.terraform.io/downloads.html  
[Getting started with Terraform and AWS](https://learn.hashicorp.com/collections/terraform/aws-get-started)  
CI/CD og ML pipelines: https://medium.com/@karthik.vaithyanathan/using-continuous-machine-learning-to-run-your-ml-pipeline-eeeeacad69a3

SOLID: https://link.medium.com/HgjlmchRddb  
Mer bash (mangler et par av disse) https://link.medium.com/58GLROIVcdb  


