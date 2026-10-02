import numpy as np
from engine import Engine
from nasa_cea import NASA_CEA
from plotter import Plotter, PlotData
from enum import Enum
from dataclasses import replace
import matplotlib.pyplot as plt
import cea

class Parameters(Enum):
    '''
    returns engine parameter name = (unit)
    '''
    MIXTURE_RATIO = ""
    CHAMBER_PRESSURE = "(bar)"

class Performance_Parameters(Enum):
    '''
    returns performance engine parameter name = (unit)
    '''
    COMBUSTION_TEMPERATUE = "(K)"
    ISP = "(s)"
    C_STAR = "(m/s)"

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
        if parameter == Parameters.MIXTURE_RATIO:
            return f"CHAMBER_PRESSURE = {engine_config.chamber_pressure}"
        elif parameter == Parameters.CHAMBER_PRESSURE:
            return f"MIXTURE_RATIO = {engine_config.OF_ratio}"
        else:
            return ""

    def get_performance_data(self, engine_config: Engine = None) -> dict[Performance_Parameters, float]:  # type: ignore
        '''
        get isp, c* and temp data from rocket_solution
        rocket_solution: cea rocket solution for Engine()
        engine_config: Engine() object, default = self.engine
        '''
        if engine_config is None:
            engine_config = self.engine
        rocket_solution = NASA_CEA().cea_rocket_solver(engine_config)
        return {Performance_Parameters.ISP: self.calc_isp(rocket_solution.Isp[2]), 
                Performance_Parameters.C_STAR: rocket_solution.c_star[2], 
                Performance_Parameters.COMBUSTION_TEMPERATUE: rocket_solution.T[2]}

    def get_performance_parameter_plot_data(self, performance_parameter: Performance_Parameters, x_parameter: Parameters, x_list: list[float], y_list: list[float]) -> PlotData:
        '''
        get plot data object for each performance parameter (isp, c*, temp)
        performance_parameter: engine performance parameter (y axis data) (isp, c*, temp)
        x_paremeter: independent variable (x axis data) (chamber pressure, mixture ratio)
        x_list: x data list
        y_list: y data list
        '''
        if performance_parameter != Performance_Parameters.ISP and performance_parameter != Performance_Parameters.COMBUSTION_TEMPERATUE and performance_parameter != Performance_Parameters.C_STAR:
            raise Exception(f"Invalid performance parameter {performance_parameter}")
        if x_parameter != Parameters.CHAMBER_PRESSURE and x_parameter != Parameters.MIXTURE_RATIO:
            raise Exception(f"Invalid engine parameter {x_parameter}")
        return PlotData(x_list, y_list, x_label=f"{x_parameter.name} {x_parameter.value}", 
                y_label=f"{performance_parameter.name} {performance_parameter.value}", 
                title=f"{self.get_title_independent_variable(x_parameter, self.engine)} {self.engine.fuel}/{self.engine.oxidiser}")

    def change_engine_config_parameter(self, parameter: Parameters, value: int | float,  engine_config: Engine) -> Engine:
        '''
        change value of parameter in engine configuration
        parameter: independent variable
        value: new value to replace
        engine_config: Engine object
        '''
        if parameter == Parameters.MIXTURE_RATIO:
            engine_config = replace(self.engine, OF_ratio=value)
        elif parameter == Parameters.CHAMBER_PRESSURE:
            engine_config = replace(self.engine, chamber_pressure=value)
        return engine_config

    def get_performance_plot_data_dict(self, parameter: Parameters, values: list[float]) -> dict[Performance_Parameters, PlotData]:
        '''
        get PlotData object for all performance parameters(isp, c*, temp) to plot on a graph
        '''
        temp_y_list = []
        isp_y_list = []
        c_star_y_list = []
        for v in values:
            engine_config = self.change_engine_config_parameter(parameter, v, self.engine)
            results = self.get_performance_data(engine_config=engine_config)
            temp_y_list.append(results[Performance_Parameters.COMBUSTION_TEMPERATUE])
            isp_y_list.append(results[Performance_Parameters.ISP])
            c_star_y_list.append(results[Performance_Parameters.C_STAR])
        temp_plot_data = self.get_performance_parameter_plot_data(
                        performance_parameter=Performance_Parameters.COMBUSTION_TEMPERATUE, 
                        x_parameter=parameter,
                        x_list = values,
                        y_list = temp_y_list)
        isp_plot_data = self.get_performance_parameter_plot_data(
                        performance_parameter=Performance_Parameters.ISP, 
                        x_parameter=parameter,
                        x_list = values,
                        y_list = isp_y_list)
        c_star_plot_data = self.get_performance_parameter_plot_data(
                        performance_parameter=Performance_Parameters.C_STAR, 
                        x_parameter=parameter,
                        x_list = values,
                        y_list = c_star_y_list)
        return {
            Performance_Parameters.COMBUSTION_TEMPERATUE: temp_plot_data,
            Performance_Parameters.ISP: isp_plot_data,
            Performance_Parameters.C_STAR: c_star_plot_data}


def pc_and_mr_effect(pc_array: list[float], mr_array: list[float], engine_config: Engine) -> None:
    '''
    plot performance parameters against OF ratio for different chamber pressure values
    pc_array: chamber pressure array
    mr_array: OF ratio array
    engine_config: Engine object
    '''
    temp_list: list[PlotData] = []  # temperature PlotData list
    isp_list: list[PlotData] = []  # isp PlotData list
    c_star_list: list[PlotData] = []  # c* PlotData list
    for pc in pc_array:
        new_config = replace(engine_config, chamber_pressure = pc)  # replace pc and mr value
        performance = EnginePerformance(new_config)
        results = performance.get_performance_plot_data_dict(Parameters.MIXTURE_RATIO, mr_array)
        temp_list.append(results[Performance_Parameters.COMBUSTION_TEMPERATUE])  # append temp line data to list
        isp_list.append(results[Performance_Parameters.ISP])  # append isp line data to list
        c_star_list.append(results[Performance_Parameters.C_STAR])  # append c* line data to list

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