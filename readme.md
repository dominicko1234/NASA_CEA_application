# Application of NASA CEA python

This program uses the python interface of NASA CEA to help determine the following parameters for a rocket engine.

Parameters:

- Oxidiser to Fuel (O/F) ratio // Mixture ratio
- Chamber pressure

## Installation

1. Clone repository
   ```bash
   git clone https://github.com/username/project-name.git
   cd project-name
   ```
2. Create a new virtual environment

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies

   ```
   pip3 install -r requirements.txt
   ```

## Usage

Plotting graphs of Specific impulse, Characteristic velocity, Combustion temperature (isp, c\*, temp) against Mixture ratio, for different chamber pressures

```python
from engine import Engine
from main import pc_and_mr_effect

# Example
engine = Engine(
    fuel = "C3H8O,2propanol",
    oxidiser = "O2(L)",
    fuel_temp = 298.15,
    ...
)
mixture_ratio_array = [0.5, 1.0, 1.5, 2.0]
chamber_pressure_array = [10, 15, 20, 25, 30]
pc_and_mr_effect(mixture_ratio_array, chamber_pressure_array, engine)
plt.show()
```
