from string import ascii_letters

def parse(filename: str = None):
    """Parses and converts your Markdown into HTML.

    Returns your converted HTML as a string."""
    with open(filename, 'r') as input:
        content = input.read()
    output = ""
    for element in content.split('\n'):
        if element == '':
            output += "\n"
            continue
        elif element[0] == "#" and element[1] == ' ':
            element = list(element)
            del element[1]
            element = ''.join(element)
            output += f"<h1>{element.strip('#')}</h1>\n"
            continue
        elif element[0] == "#" and element[1] == "#" and element[2] == " ":
            element = list(element)
            del element[2]
            element = ''.join(element)
            output += f"<h2>{element.strip('#')}</h2>\n"
            continue
        elif element[1] == "#" and element[2] == "#":
            element = list(element)
            del element[3]
            element = ''.join(element)
            output += f"<h3>{element.strip('#')}</h3>\n"
            continue
        elif element[0] == "-":
            element = list(element)
            del element[1]
            element = ''.join(element)
            if "***" in element:
                while True:
                    element = element.replace("***", "<em><strong>", 1)
                    element = element.replace("***", "</strong></em>", 1)
                    if not "***" in element:
                        break
            elif "**" in element:
                while True:
                    element = element.replace("**", "<strong>", 1)
                    element = element.replace("**", "</strong>", 1)
                    if not "**" in element:
                        break
            if "*" in element:
                while True:
                    element = element.replace("*", "<em>", 1)
                    element = element.replace("*", "</em>", 1)
                    if not "*" in element:
                        break
            element = ''.join(element)
            output += f"<li>{element.strip('-')}</li>\n"
            continue
        else:
            if "***" in element:
                while True:
                    element = element.replace("***", "<em><strong>", 1)
                    element = element.replace("***", "</strong></em>", 1)
                    if not "***" in element:
                        break
            elif "**" in element:
                while True:
                    element = element.replace("**", "<strong>", 1)
                    element = element.replace("**", "</strong>", 1)
                    if not "**" in element:
                        break
            if "*" in element:
                while True:
                    element = element.replace("*", "<em>", 1)
                    element = element.replace("*", "</em>", 1)
                    if not "*" in element:
                        break
            output += f"<p>{element}</p>\n"
            continue
    return output