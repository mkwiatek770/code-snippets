import cProfile
import pstats
import io

def profile(func):
    """Profile function decorator."""
    
    def inner(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        response = func(*args, **kwargs)
        profiler.disable()

        stream = io.StringIO()
        ps = pstats.Stats(profiler, stream=stream).sort_stats('cumulative')
        ps.print_stats()
        print(stream.getvalue())
        return response
    return inner

