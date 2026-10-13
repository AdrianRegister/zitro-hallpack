import re

def resolve_branch(branches, tag):
    tag = tag.lower()
    tag_major_version = tag.split(".")[0]
    tag_minor_version = tag.split(".")[1]
    # tag_patch_version = tag.split(".")[2]
    
    print(f'Resolviendo rama de {branches} con tag {tag}\n')
    
    with open(branches, "r") as b:
        matches = []
        
        for line in b:
            line = line.strip()
            line = line.lower()
            
            if tag in line:
                matches.append(line)
                print(f"Matches: {matches}")
            elif tag_major_version in line:
                matches.append(line)
            
        if not matches:
            print(f"Ninguna rama encontrada asociada con tag {tag}")
            return
            
        matches = [m for m in matches if "_old" not in m]  
        # print(f"Ramas encontradas: {matches}")
        
        for m in matches:
            full_pattern = rf"^releases/{tag_major_version}\.{tag_minor_version}+" 
            if re.match(full_pattern, m):
                print(m)
                return
            
            major_version_pattern = rf"^releases/{tag_major_version}\.x"
            if re.match(major_version_pattern, m):
                print(m)
                return