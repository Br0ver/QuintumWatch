from __future__ import annotations

import json
import os
from datetime import datetime
import random
from datetime import timedelta

#!/usr/bin/env python3


time_factor = 10 # factor to increase the effect of time spent looking at the clock
decay_rate = 1e-6  # per second



def display_time_and_load_save(
    filepath: str,
) :

    # Display current system time (ISO 8601)
    now = datetime.now().isoformat()

    # Load existing values (safe fallback to defaults)
    a = 0.0
    b = 0.0
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            a = float(data.get("a", a))
            b = datetime.fromisoformat(data.get("b", b))
    except FileNotFoundError:
        # file will be created below
        pass
    except (ValueError, json.JSONDecodeError):
        # corrupted file -> overwrite with defaults or with provided values
        pass
    

    seconds_since_epoch = (datetime.now() - b).total_seconds()
    
    print(f"Loaded values: a={a}, b={b}")
    print(f"Seconds since last update: {seconds_since_epoch} seconds")


    sigma = a*((1-decay_rate)**seconds_since_epoch)
    print(f"Sigma: {sigma}    ")
    print(f"99.7% of values lie within ±3σ: ±{3*sigma} seconds")
    # sample a random value from a normal distribution (mean=0.0, std=1.0)
    sampled_value = random.normalvariate(0.0, sigma) # scew in secods

    # add sampled seconds to the current datetime
    scewed_time = datetime.fromisoformat(now) + timedelta(seconds=sampled_value)

    print(f"Sampled normal value: {sampled_value}")
    print("Current time:", now)
    print(f"scewed time:", str(scewed_time))
    # update 'a' with the sampled value (leave 'b' unchanged)
    # a = float(sampled_value)
    # Prepare payload and save atomically


    input("Press Enter to continue...")

    end = datetime.now().isoformat()

    delta_time = datetime.fromisoformat(end) - datetime.fromisoformat(now)
    print(f"Elapsed time: {delta_time.total_seconds()} seconds")

    elapsed_seconds = delta_time.total_seconds()

    a = sigma + elapsed_seconds * time_factor
    b = end
    payload = json.dumps({"a": a, "b": b}, ensure_ascii=False, indent=2)

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(payload)
    except OSError:
        pass
    return 


if __name__ == "__main__":
    # Example usage: prints time, loads or creates state.json, increments a counter
    state_file = "state.json"

    # Load current values
    display_time_and_load_save(state_file)
