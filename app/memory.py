from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from .config import Config

def get_redis_history(session_id: str) -> BaseChatMessageHistory:
    """
    Return a Redis-backed char message history.
    """
    return RedisChatMessageHistory(
        session_id=session_id,
        url=Config.REDIS_URL,
        ttl=3600  # 1 hour TTL for testing
    )
