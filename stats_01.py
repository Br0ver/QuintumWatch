import numpy as np
import matplotlib.pyplot as plt




time_factor = 10 # factor to increase the effect of time spent looking at the clock
decay_rate = 1e-6  # per second



time = np.logspace(1,8, 1000).reshape(-1,1) # time in seconds from 10s to ~3 years
relative_watch_time = np.linspace(1, 60, 4) / 3600# relative time looked at the clock. e.g. 1 minute per hour 1/60
relative_watch_time = relative_watch_time.reshape(1, -1) # make it a row vector
print(relative_watch_time.shape)


abs_whatch_time = relative_watch_time * time # total time looked at the clock 


# function is C_t = C_(t-1) * b + a



decay_rate = 1-decay_rate  # inverse to make the formula easier to read

trace_decay = 0 # decay of the memory trace for sigma

sigma = relative_watch_time * time_factor/(1-decay_rate)* (1-decay_rate** time)
sigma_3 = 3 * sigma

def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        return f"{seconds/60:.1f}m"
    elif seconds < 86400:
        return f"{seconds/3600:.1f}h"
    elif seconds < 31536000:
        return f"{seconds/86400:.1f}d"
    else:
        return f"{seconds/31536000:.1f}y"

plt.loglog(time, sigma, label=np.round(relative_watch_time.reshape(-1)*3600))
plt.xlabel('Time')
plt.ylabel('Sigma')
ax = plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_time(x)))
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_time(x)))
ax.grid(True, which="major", ls="--", alpha=0.5)
plt.title('Sigma over total time. \n For several amounts of seconds (legend) looked at the clock per hour.')
plt.legend()
plt.show()

