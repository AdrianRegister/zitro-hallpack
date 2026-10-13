import argparse
from .resolve_branch.resolve_branch import resolve_branch

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("resolve-branch", help="Encuentra una rama de release basado en el TAG")
    parser.add_argument("-b", "--branches", help="La ruta del archivo de ramas remotas")
    
    args = parser.parse_args()
    
    if getattr(args, "resolve-branch"):
        resolve_branch(args.branches)
    
    
if __name__ == "__main__":
    main()