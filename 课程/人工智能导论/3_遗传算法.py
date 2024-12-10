import numpy as np
from deap import base, creator, tools, algorithms
import matplotlib.pyplot as plt


# 定义适应度函数
def fitness_function(individual):
    x = individual[0]
    y = individual[1]
    value = (6.452 * (x + 0.125 * y) * (np.cos(x) - np.cos(2 * y)) ** 2 /
             np.sqrt(0.8 + (x - 4.2) ** 2 + 2 * (y - 7) ** 2) + 3.226 * y)
    return value


# 创建适应度类和个体类
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)


# 初始化种群
def init_individual(icls):
    return icls([np.random.uniform(0, 10), np.random.uniform(0, 10)])


toolbox = base.Toolbox()
toolbox.register("individual", init_individual, creator.Individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# 注册遗传算法的操作
toolbox.register("evaluate", fitness_function)


def run_experiment(pop_size, selection, sel_kwargs, crossover, cx_kwargs, mutation, mut_kwargs):
    toolbox.register("select", selection, **sel_kwargs)
    toolbox.register("mate", crossover, **cx_kwargs)
    toolbox.register("mutate", mutation, **mut_kwargs)

    pop = toolbox.population(n=pop_size)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=50, stats=stats, halloffame=hof, verbose=False)

    # Unregister operations to prepare for next experiment
    del toolbox.select
    del toolbox.mate
    del toolbox.mutate

    return hof, stats


# 实验配置
pop_sizes = [100, 200, 300]
selections = [(tools.selRoulette, {}), (tools.selTournament, {"tournsize": 3})]
crossovers = [(tools.cxOnePoint, {}), (tools.cxTwoPoint, {}), (tools.cxUniform, {"indpb": 0.5}),
              (tools.cxBlend, {"alpha": 0.5})]
mutations = [(tools.mutGaussian, {"mu": 0, "sigma": 1, "indpb": 0.2}), (tools.mutShuffleIndexes, {"indpb": 0.2})]

# 记录实验结果
experiment_results = []

for pop_size in pop_sizes:
    for selection, sel_kwargs in selections:
        for crossover, cx_kwargs in crossovers:
            for mutation, mut_kwargs in mutations:
                hof, stats = run_experiment(pop_size, selection, sel_kwargs, crossover, cx_kwargs, mutation, mut_kwargs)
                best_ind = hof[0]
                result = {
                    "pop_size": pop_size,
                    "selection": selection.__name__,
                    "crossover": crossover.__name__,
                    "mutation": mutation.__name__,
                    "best_ind": best_ind,
                    "best_value": best_ind.fitness.values[0]
                }
                experiment_results.append(result)

# 打印实验结果
for result in experiment_results:
    print(
        f"Population Size: {result['pop_size']}, Selection: {result['selection']}, Crossover: {result['crossover']}, Mutation: {result['mutation']}, Best Value: {result['best_value']:.15f}")

# 可视化实验结果
import pandas as pd
import seaborn as sns

# 将实验结果转换为DataFrame
df = pd.DataFrame(experiment_results)

# 绘制不同种群规模下的最佳适应度值
plt.figure(figsize=(14, 10))
sns.boxplot(x="pop_size", y="best_value", hue="selection", data=df)
plt.title("Best Fitness Values for Different Population Sizes and Selection Methods")
plt.xlabel("Population Size")
plt.ylabel("Best Fitness Value")
plt.legend(title="Selection Method")
plt.show()
