class ProcessManager:
    """Simulated processes. Each one has a PID, a name, and a status."""

    def __init__(self):
        self.next_pid = 1
        self.table = {}

    def run(self, name):
        pid = self.next_pid
        self.next_pid += 1
        self.table[pid] = {"name": name, "status": "RUNNING"}
        return pid

    def kill(self, pid):
        if pid not in self.table:
            return False
        del self.table[pid]
        return True

    def listing(self):
        lines = [f"{'PID':<6}{'NAME':<16}STATUS"]
        for pid, info in self.table.items():
            lines.append(f"{pid:<6}{info['name']:<16}{info['status']}")
        return lines
