# sourcery skip: avoid-builtin-shadow
import uuid
from datetime import datetime
from dataclasses import dataclass, field # 3.10 - DataClass
from typing import Optional

@dataclass(kw_only=True) #init, repr, eq

class Category: # Constructor

    id: uuid.UUID = field(
        default_factory=lambda: uuid.uuid4() # Create the instance without reapeat id
    )
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now() # Create the instance without reapeat datetime
    ) 
