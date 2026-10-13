import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("resolve-branch", help="Encuentra una rama de release basado en el TAG")
    parser.add_argument("-b", "--branches", help="La ruta del archivo de ramas remotas")
    
    args = parser.parse_args()
    
    print(args)
    
    
if __name__ == "__main__":
    main()