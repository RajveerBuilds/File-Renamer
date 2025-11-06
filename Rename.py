import os
folder_path = input("Enter folder path: ").strip()
os.listdir(folder_path)
print(os.listdir(folder_path))
for count, filename in enumerate(os.listdir(folder_path)):
    if not filename.endswith(".txt"):
        continue
    src = os.path.join(folder_path , filename)
    name, ext = os.path.splitext(filename)
    dst = os.path.join(folder_path , f"renamed_{count}.txt")
    os.rename(src, dst)
    print(f"{filename} → renamed_{count}.txt")
