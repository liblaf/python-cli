class ExtraNotInstalledError(RuntimeError):
    extra: str

    def __init__(self, extra: str) -> None:
        self.extra = extra
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message

    @property
    def message(self) -> str:
        return f"{self.extra} should be installed with `pip install python-cli[{self.extra}]"
