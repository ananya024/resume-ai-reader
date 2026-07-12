# normalizer.py

ALIASES = {

    "postgres":"postgresql",
    "postgresql database":"postgresql",

    "dbms":"database management systems",

    "oop":"object oriented programming",

    "os":"operating systems",

    "computer network":"computer networks",

    "rest apis":"rest api",

    "js":"javascript",

    "node":"node.js",

    "reactjs":"react",

}

def normalize(skill):

    skill = skill.lower().strip()

    return ALIASES.get(skill, skill)