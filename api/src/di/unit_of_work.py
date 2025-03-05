import abc
from abc import abstractmethod
from typing import Any, Generic, Optional, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from repositories.abstraction import AbstractPersonRepository
from repositories.relational_db import RelationalDBPersonDetectRepository
from common.detection import Detection

from common.type import UUIDStr

T = TypeVar("T", bound=AbstractPersonRepository)


class AbstractUnitOfWork(Generic[T], abc.ABC):
    personDetectionRepo: AbstractPersonRepository

    def __init__(self, personDetectionRepo: T):
        self.personDetectionRepo = personDetectionRepo

    @abstractmethod
    async def __aenter__(self) -> 'AbstractUnitOfWork':
        raise NotImplemented
    
    @abstractmethod
    async def __aexit__(self, exc_type, exc, tb):
        raise NotImplemented
    

class AsyncSQLAlchemyUnitOfWork(AbstractUnitOfWork[RelationalDBPersonDetectRepository]):
    def __init__(self, session: AsyncSession, personDetectionRepo: RelationalDBPersonDetectRepository):
        super().__init__(personDetectionRepo=personDetectionRepo)
        self._session = session

    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type: Optional[Type[BaseException]], exc: Optional[BaseException], tb: Any):
        try:
            if exc_type is None:
                await self._session.commit()
            else:
                await self._session.rollback()
        finally:
            await self._session.close()
            await self.remove()
    
    async def remove(self):
        from settings.db import AsyncScopedSession

        await AsyncScopedSession.remove()


class AbstractDetectionUnitOfWork(abc.ABC):
    """Abstract base class for detection unit of work.
    
    This defines the interface that all detection unit of work 
    implementations must follow.
    """
    
    @abstractmethod
    async def __aenter__(self) -> 'AbstractDetectionUnitOfWork':
        """Enter the async context manager."""
        raise NotImplementedError
    
    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the async context manager."""
        raise NotImplementedError
    
    async def detectPersons(self, UUIDStr) -> dict:
        """Detect persons in the provided image data.
        
        Args:
            image_data: The image data to process
            
        Returns:
            Detection results containing detected persons
        """
        raise NotImplementedError


class DetectionUnitOfWork(AbstractDetectionUnitOfWork):
    """Concrete implementation of detection unit of work.

    This unit of work encapsulates operations related to person detection,
    providing a consistent interface for detection services.
    """
    
    def __init__(self, detectionEngine: Detection):  
        self.detectionEngine = detectionEngine
    
    async def __aenter__(self):
        """Enter the async context manager."""
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the async context manager.
        
        The detection engine doesn't require specific cleanup, 
        so this method is minimal.
        """
        pass
    
    async def detectPersons(self, uuid: UUIDStr) -> dict:
        """Detect persons in the provided image data.
        
        Args:
            image_data: The image data to process
            
        Returns:
            Detection results from the detection engine
        """
        return self.detectionEngine.detect(uuid)