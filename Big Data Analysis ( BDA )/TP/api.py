from hdfs import InsecureClient

HDFS_URL='http://localhost:9870'

client = InsecureClient(HDFS_URL, user='romain')

hdfs_path = '/user/romain/arbre.csv'

def create_empty_arbre() :
    with client.write(hdfs_path, overwrite=True) as writer:
        writer.write('')
    print(f'Arbre vide créé a : {hdfs_path}')

def upload_local_arbre(local_path) :
    client.upload(hdfs_path, local_path, overwrite=True)
    print(f"Arbre chargé depuis {local_path} vers {hdfs_path}")

def read_file(path) :
    with client.read(path) as reader:
        content = reader.read().decode('utf-8')
        print(f"Contenue du fichier {path} : \n")
        print(content)

def list_dir(dir_path) :
    files = client.list(dir_path)
    print(f"Contenue du repertoire {dir_path} : {files}")

def read_file_line_by_line(path) :
    with client.read(path) as reader:
        print(f"Contenue du fichier {path} line by line : \n")
        for line in reader:
            print(line)

def delet_file(path) :
    client.delete(path, recursive=True)
    print(f"Fichier {path} supprimé")


create_empty_arbre()
upload_local_arbre('arbres.csv')
# read_file(hdfs_path)
list_dir('/user/romain')
# read_file_line_by_line(hdfs_path)
delet_file(hdfs_path)