# good-dev-practice
Espen's effort to move from writing code on and for my local PC to production quality code deployed in the cloud (AWS).

[Writing Great Python Code](https://docs.python-guide.org/#writing-great-python-code)  

## Learnt from PRs - to be moved at some point
- Be super critical of your own doc string. Check spelling, grammar, conciseness, intuitivety and DRY with declaration/type hints.
- Use helper functions within functions to keep it readable.  
- Always use `snake_case` variable names in Python, also when referring to `CamelCaseClassNames`.  
- (Simen mener:) Move large if/else or other boilerplate sections into helper functions with intuitive
names to make the main function more readable.
- Use plenty og type annotations `stats: ClassVar[Dict[str, int]] = {}` and [PEP 526](https://www.python.org/dev/peps/pep-0526/).  
- First, do type check (`isinstance(value, type)`), så gjør de logiske operasjonene, ikke i en `if isinstance .. else ...`.  
- Line changes between groups of `import`s, first standard libraries, then 3rd party, then import from own modules.  
- DRY blir sjelden feil.
- `date_range` is a more pythonic function name than `get_date_range`.
- Class/function/variable names should be as consise and descriptive as possible.  
- Don't use the doc string to describe what should or is described in the type hint.
- Avoid double negatives. `if x is not None:` --> `if x:`
- ..

