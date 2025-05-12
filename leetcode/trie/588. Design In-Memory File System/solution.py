class File:
    def __init__(self, isfile=False):
        self.isfile = isfile
        self.files = {}
        self.content = ''

class FileSystem:

    def __init__(self):
        self.root = File()

    def ls(self, path: str) -> List[str]:
        p = self.root
        if path != '/':
            ds = path.split('/')[1:]
            for d in ds:
                p = p.files[d]
            if p.isfile:
                return [ds[-1]]
        return sorted(list(p.files.keys()))

    def mkdir(self, path: str) -> None:
        p = self.root
        ds = path.split('/')[1:]
        for d in ds:
            if d not in p.files:
                p.files[d] = File()
            p = p.files[d]        

    def addContentToFile(self, filePath: str, content: str) -> None:
        p = self.root
        ds = filePath.split('/')[1:]
        for d in ds[:-1]:
            p = p.files[d]
        if ds[-1] not in p.files:
            p.files[ds[-1]] = File(True)
        p = p.files[ds[-1]]
        p.content += content

    def readContentFromFile(self, filePath: str) -> str:
        p = self.root
        ds = filePath.split('/')[1:]
        for d in ds:
            p = p.files[d]
        return p.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
