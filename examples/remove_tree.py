from pathlib import Path

import pathlibext  # pylint: disable=unused-import


if __name__ == "__main__":
    tmp = Path.tmpdir()  # from pathlibext
    files = [
        tmp / "1" / "a.txt",
        tmp / "1" / "b.txt",
        tmp / "2" / "a.txt",
        tmp / "2" / "b.txt",
    ]
    for f in files:
        f.parent.mkdir(exist_ok=True)
        f.touch()
    for d in tmp.find(type_="d", name="2"):  # from pathlibext
        print(f"removing {d}...")
        d.rmtree()  # from pathlibext
    tmp.rmtree()
