import asyncio
from functools import update_wrapper


def async_partial(func, *args):
   async def wrapper(*args2):
       result = func(*args, *args2)
       if asyncio.iscoroutinefunction(func):
           result = await result
       return result
   return wrapper