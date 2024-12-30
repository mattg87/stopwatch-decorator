import asyncio
import functools
import time


def stopwatch_decorator(theFunction):
    @functools.wraps(theFunction)
    async def async_wrapper(*args, **kwargs):
        startTime = time.perf_counter()
        result = await theFunction(*args, **kwargs)
        endTime = time.perf_counter()
        print(f"Function {theFunction.__name__} took {(endTime - startTime)} seconds to run")
        return result
    
    
    @functools.wraps(theFunction)
    def sync_wrapper(*args, **kwargs):
        startTime = time.perf_counter()
        result = theFunction(*args, **kwargs)
        endTime = time.perf_counter()
        print(f"Function {theFunction.__name__} took {(endTime - startTime)} seconds to run")
        return result
    

    # Determines whether the theFunction is async or not and returns the right wrapper
    if asyncio.iscoroutinefunction(theFunction):
        return async_wrapper
    else:
        return sync_wrapper
