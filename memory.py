class MemoryManager:
    """Simulated memory. Tracks total and used megabytes."""

    def __init__(self, total=1024, used=256):
        self.total = total
        self.used = used

    @property
    def free_mb(self):
        return self.total - self.used

    def allocate(self, mb):
        if mb <= 0:
            return "Error: Amount must be greater than 0."
        if mb > self.free_mb:
            return "Error: Not enough free memory."
        self.used += mb
        return f"{mb} MB allocated."

    def release(self, mb):
        if mb <= 0:
            return "Error: Amount must be greater than 0."
        if mb > self.used:
            return "Error: Cannot free more than the used memory."
        self.used -= mb
        return f"{mb} MB released."

    def status(self):
        return [
            "Memory Status",
            "-" * 24,
            f"Total Memory: {self.total} MB",
            f"Used Memory:  {self.used} MB",
            f"Free Memory:  {self.free_mb} MB",
        ]
