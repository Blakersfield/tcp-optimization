import shutil
import os
import tarfile

def mktar(seed_file_path="../static/harambe.jpg", target_file_path="../static/arch.tar", target_size=1):
    target_bytes = target_size * (1024 ** 3)
    seed_bytes = os.path.getsize(seed_file_path)
    iterations = int(target_bytes/seed_bytes)
    file_list = []

    if not os.path.exists("working/"):
        os.mkdir("working/")

    for i in range(1,iterations):
        iterfile = "working/h"+str(i)+".jpg"
        shutil.copyfile(seed_file_path,iterfile)
        file_list.append(iterfile)

    tar = tarfile.open(target_file_path,"w")
    for name in file_list:
        tar.add(name)
    tar.close()

    for i in file_list:
        os.remove(i)

    os.rmdir("working/")
    print("done!")
