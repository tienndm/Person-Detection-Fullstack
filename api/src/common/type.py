import re
from datetime import datetime

class UUIDStr(str):
    """UUID represented as a hexadecimal string."""

    # regular expression to match 32 hexadecimal characters

    UUID_PATTERN = re.compile(r'^[a-fA-F0-9]{32}$')

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)

        if not cls.UUID_PATTERN.match(instance):
            raise ValueError(f'\'{instance}\' is not a valid UUID hexadecimal string')

        return instance

class DateTime(str):
    """DateTime represented as a string with validation."""
    
    DEFAULT_FORMAT = "%Y-%m-%d %H:%M:%S"
    
    def __new__(cls, value, format=DEFAULT_FORMAT):
        instance = super().__new__(cls, value)
        instance._format = format
        
        try:
            datetime.strptime(value, format)
        except ValueError:
            raise ValueError(f"'{value}' is not a valid datetime string with format '{format}'")
        
        return instance
    
    @property
    def datetime(self):
        """Convert to Python datetime object."""
        return datetime.strptime(self, self._format)