from pathlib import Path
import pathlibext  # pylint: disable=unused-import


if __name__ == '__main__':

    tmp = Path.tmpdir()  # from pathlibext
    print(f"Create temp directory {tmp}")

    for f in [
        tmp / "dir1" / "a.txt",
        tmp / "dir1" / "b.txt",
        tmp / "dir2" / "a.txt",
        tmp / "dir2" / "b.txt",
    ]:
        f.parent.mkdir(exist_ok=True)
        f.touch()
        print(f"Create file {f}")
    

    for d in tmp.find(type_="d", name="dir2"): # from pathlibext
        d.rmtree() # from pathlibext
        print(f"Remove non-empty directory {d}")

    print("Existing directories after rmtree()")
    for d in tmp.find(type_="d"): # from pathlibext
        print(f"{d}")

    tmp.rmtree() # from pathlibext
    print(f"Remove non-empty temp dir {tmp}")