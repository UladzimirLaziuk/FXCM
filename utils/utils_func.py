import asyncio
from functools import update_wrapper, partial


def wrapped_partial(func, *args, **kwargs):
    partial_func = partial(func, *args, **kwargs)
    update_wrapper(partial_func, func)
    return partial_func


def async_partial(func, *args):
   async def wrapper(*args2):
       result = func(*args, *args2)
       if asyncio.iscoroutinefunction(func):
           result = await result
       return result
   return wrapper