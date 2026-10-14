class FileSystem:
    """Simulated file system. Folders are dicts. Files are strings."""

    def __init__(self):
        self.root = {}
        self.path = []

    def _cwd(self):
        node = self.root
        for part in self.path:
            node = node[part]
        return node

    def location(self):
        return "/" + "/".join(self.path)

    def dir(self):
        items = self._cwd()
        if not items:
            return ["(empty)"]
        lines = []
        for name, value in sorted(items.items()):
            if isinstance(value, dict):
                lines.append(f"<DIR>   {name}")
            else:
                lines.append(f"        {name}")
        return lines

    def mkdir(self, name):
        cwd = self._cwd()
        if name in cwd:
            return "Error: Name already exists."
        cwd[name] = {}
        return "Directory created."

    def create(self, name):
        cwd = self._cwd()
        if name in cwd:
            return "Error: Name already exists."
        cwd[name] = ""
        return "File created."

    def write(self, name, text):
        cwd = self._cwd()
        if name not in cwd or isinstance(cwd[name], dict):
            return "Error: File does not exist."
        cwd[name] = text
        return "File saved."

    def read(self, name):
        cwd = self._cwd()
        if name not in cwd or isinstance(cwd[name], dict):
            return "Error: File does not exist."
        return cwd[name] if cwd[name] else "(file is empty)"

    def delete(self, name):
        cwd = self._cwd()
        if name not in cwd:
            return "Error: File does not exist."
        if isinstance(cwd[name], dict) and cwd[name]:
            return "Error: Directory is not empty."
        del cwd[name]
        return "File deleted."

    def cd(self, name):
        if name == "..":
            if self.path:
                self.path.pop()
            return ""
        cwd = self._cwd()
        if name not in cwd or not isinstance(cwd[name], dict):
            return "Error: Directory does not exist."
        self.path.append(name)
        return ""
