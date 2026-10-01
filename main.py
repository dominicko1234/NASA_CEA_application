import numpy as np
from engine import Engine
from nasa_cea import NASA_CEA
from plotter import Plotter, PlotData
from enum import Enum
from dataclasses import replace
import matplotlib.pyplot as plt

class Parameters(Enum):
    '''
    returns parameter name = (unit)
    '''
    MIXTURE_RATIO = ""
    CHAMBER_PRESSURE = "(bar)"

class EnginePerformance:
    def __init__(self, engine: Engine) -> None:
        '''
        engine: Engine object
        '''
        self.engine = engine

    def calc_isp(self, effective_exhaust_velocity: float) -> float:
        '''
        calculate isp from effective exhaust velocity
        effective_exhaust_velocity: effective exhaust velocity c in m/s
        '''
        return effective_exhaust_velocity / 9.80665

    def calc_mdot(self, target_thrust: float, effective_exhaust_velocity: float) -> float:
        '''
        calculate total mass flow rate from target thrust and effective exhaust velocity
        target_thrust: target thrust in N
        effective_exhaust_velocity: effective exhaust velocity c in m/s
        '''
        return target_thrust / effective_exhaust_velocity

    def get_title_independent_variable(self, parameter: Parameters, engine_config: Engine) -> str:
        '''
        get title independent variable for graph depending on paramter
        parameter: independent variable
        '''
        if parameter.name == "MIXTURE_RATIO":
            return f"CHAMBER_PRESSURE = {engine_config.chamber_pressure}"
        elif parameter.name == "CHAMBER_PRESSURE":
            return f"MIXTURE_RATIO = {engine_config.OF_ratio}"
        else:
            return ""

    def change_engine_config_parameter(self, parameter: Parameters, value: int | float,  engine_config: Engine) -> Engine:
        '''
        change value of parameter in engine configuration
        parameter: independent variable
        value: new value to replace
        engine_config: Engine object
        '''
        if parameter.name == "MIXTURE_RATIO":
            engine_config = replace(self.engine, OF_ratio=value)
        elif parameter.name == "CHAMBER_PRESSURE":
            engine_config = replace(self.engine, chamber_pressure=value)
        return engine_config
    
    def get_isp(self, parameter: Parameters, values: list[float]) -> PlotData:
        '''
        get isp values from paramter array
        parameter: independent variable = mr, pc
        values: array for paramter
        '''
        y_list = []
        for value in values:
            engine_config = self.change_engine_config_parameter(parameter, value, self.engine)
            solution = NASA_CEA().cea_rocket_solver(engine_config)
            y_list.append(self.calc_isp(solution.Isp[2]))
        return PlotData(values, y_list, f"{parameter} {parameter.value}", "Isp (s)", f"{self.get_title_independent_variable(parameter, engine_config)}, {engine_config.oxidiser}/{engine_config.fuel}")

    def get_c_star(self, parameter: Parameters, values: list[float]) -> PlotData:
        '''
        get c* values from parameter array
        parameter: independent variable = mr, pc
        values: array for paramter
        '''
        y_list = []
        for value in values:
            engine_config = self.change_engine_config_parameter(parameter, value, self.engine)
            solution = NASA_CEA().cea_rocket_solver(engine_config)
            y_list.append(solution.c_star[2])
        return PlotData(values, y_list, f"{parameter} {parameter.value}", "C* (m/s)", f"{self.get_title_independent_variable(parameter, engine_config)}, {engine_config.oxidiser}/{engine_config.fuel}")

    def get_temperature(self, parameter: Parameters, values: list[float]) -> PlotData:
        '''
        get temperature values from parameter array
        parameter: independent variable = mr, pc
        values: array for paramter
        '''
        y_list = []
        for value in values:
            engine_config = self.change_engine_config_parameter(parameter, value, self.engine)
            solution = NASA_CEA().cea_rocket_solver(engine_config)
            y_list.append(solution.T[2]) 
        return PlotData(values, y_list, f"{parameter} {parameter.value}", "Combustion temperature (K)", f"{self.get_title_independent_variable(parameter, engine_config)}, {engine_config.oxidiser}/{engine_config.fuel}")

def pc_and_mr_effect(pc_array: list[float], mr_array: list[float], engine_config: Engine) -> None:
    '''
    plot performance parameters against OF ratio for different chamber pressure values
    pc_array: chamber pressure array
    mr_array: OF ratio array
    engine_config: Engine object
    '''
    temp_list: list[PlotData] = []  # temperature list
    isp_list: list[PlotData] = []  # isp list
    c_star_list: list[PlotData] = []  # c* list
    for pc in pc_array:
        new_config = replace(engine_config, chamber_pressure = pc)  # replace pc value
        performance = EnginePerformance(new_config)
        temp_list.append(performance.get_temperature(Parameters.MIXTURE_RATIO, mr_array))  # append temp line data to list
        isp_list.append(performance.get_isp(Parameters.MIXTURE_RATIO, mr_array))  # append isp line data to list
        c_star_list.append(performance.get_c_star(Parameters.MIXTURE_RATIO, mr_array))  # append c* line data to list
    P = Plotter()
    temp_fig = P.plot_multiple(temp_list, "Temperature vs OF ratio for different chamber pressures", "OF ratio", "Temperature (K)")  # plot temperatures
    isp_fig = P.plot_multiple(isp_list, "Isp vs OF ratio for different chamber pressures", "OF ratio", "Isp (s)")  # plot isp
    c_star_fig = P.plot_multiple(c_star_list, "C* vs OF ratio for different chamber pressures", "OF ratio", "C* (m/s)")  # plot c*
    plt.show()


def main() -> None:
    R2S_ENGINE = Engine(
        fuel = "C3H8O,2propanol",
        oxidiser = "O2(L)",  # LOX
        fuel_temp = 298.15,  # K
        oxidiser_temp = 50,  # K
        OF_ratio = 3.5,
        chamber_pressure = 20,  # bar
        ambient_pressure  = 1.01325  # bar
    )
    mr_array: list[float] = list(np.arange(1, 8.1, 0.1))
    pc_array = [30.0, 35.0, 40.0, 45.0]
    pc_and_mr_effect(pc_array, mr_array, R2S_ENGINE)

if __name__ == "__main__":
    main()