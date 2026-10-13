import re

def resolve_branch(branches, tag):
    tag = tag.lower()
    tag_root = tag.split(".")[0]
    print(f"TAG ROOT: {tag_root}\n")
    
    print(f'Resolving branch from {branches} with tag {tag}\n')
    
    with open(branches, "r") as b:
        matches = []
        
        for line in b:
            line = line.strip()
            line = line.lower()
            
            if tag in line:
                return line
            elif tag_root in line:
                matches.append(line)
            else:
                pass
            
        print(f"Matches: {matches}")