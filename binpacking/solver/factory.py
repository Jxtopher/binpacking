from typing import Dict, Any, Tuple, List, cast
from os import path
import copy
import json
import importlib
import re

from binpacking.solver.data_structure.domains import Domains
from binpacking.solver.data_structure.solution import Solution


class Register(object):
    class __Register(Dict[str, str]):
        def __init__(self) -> None:
            self["Backtracking"] = "binpacking.solver.optimisation.csp.backtracking"
            self["TabuSearch"] = "binpacking.solver.optimisation.metaheuristic.tabu_search"
            self["BinPacking2D"] = "binpacking.solver.bin_packing_2d"
            self["BinPacking2D_overload"] = "binpacking.solver.bin_packing_2d_overload"
            self["StopCriteria"] = "binpacking.solver.stop_criteria"
            self["CriterionBudget"] = "binpacking.solver.stop_criteria"
            self["Statistics"] = "binpacking.solver.statistics"
            self["StatisticSolution"] = "binpacking.solver.statistics"
            self["StatisticFitness"] = "binpacking.solver.statistics"
            self[
                "Neighborhood_one_mutation"
            ] = "binpacking.solver.optimisation.metaheuristic.atomic_operator.neighborhood"

        def get_import_module(self, name_class: str) -> str:
            return self[name_class]

    instance = None

    def __new__(cls) -> Any:  # __new__ always a classmethod
        if not Register.instance:
            Register.instance = Register.__Register()
        return Register.instance

    def __getattr__(self, name: str) -> Any:
        return getattr(self.instance, name)


class Factory:
    @classmethod
    def load_json(cls, filename: str) -> Any:
        file_path = path.join("", filename)
        with open(file_path) as f:
            content = f.read()
            return json.loads(content)

    @staticmethod
    def build_instance(
        name_class: str, config: Dict[str, Any], list_of_instances: Dict[str, Any]
    ) -> Any:
        list_of_paramters: List[Tuple[str, Any]] = []
        for name_parameter in config:
            if isinstance(config[name_parameter], Dict):
                list_of_paramters.append(
                    (
                        name_parameter,
                        Factory.build_instance(
                            name_parameter, config[name_parameter], list_of_instances
                        ),
                    )
                )
            else:
                if (
                    isinstance(config[name_parameter], str)
                    and re.match(r"^ref:", config[name_parameter]) is not None
                ):
                    reference = re.sub(r"^ref:", '', config[name_parameter])
                    list_of_paramters.append((name_parameter, list_of_instances[reference]))
                else:
                    list_of_paramters.append((name_parameter, config[name_parameter]))

        register = Register()
        module = importlib.import_module(register.get_import_module(name_class))
        class_ = getattr(module, name_class)

        l_parameter = [parameter for name, parameter in list_of_paramters]

        list_of_instances[name_class] = copy.deepcopy(class_(*l_parameter))
        return list_of_instances[name_class]

    @staticmethod
    def build_config(config: Dict[Any, Any]) -> Any:
        list_of_instances: Dict[str, Any] = {}
        instance_of_optimisation_algo = Factory.build_instance(
            config["OptimizationAlgorithm"],
            config[config["OptimizationAlgorithm"]],
            list_of_instances,
        )

        return instance_of_optimisation_algo

    @staticmethod
    def run_solver(config: Dict[Any, Any], instance_optimisation: Any) -> List[Solution]:
        instance_of_probleme = instance_optimisation.get_instance_of_problem()
        if config["dataStructure"] == "Domains":
            domains = Domains(instance_of_probleme)
            ret = instance_optimisation.run(domains)

        elif config["dataStructure"] == "Solution":
            sol_init = Solution(instance_of_probleme.get_instance_size())
            ret = instance_optimisation.run(sol_init)
        return cast(List[Solution], ret)
