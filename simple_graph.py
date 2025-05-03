import matplotlib.pyplot as plt

ind_var = range(1, 10_001)
dep_var = [x * x for x in ind_var]
plt.style.use('dark_background')
figure, graph = plt.subplots()
graph.scatter(ind_var, dep_var, s=15)
graph.set_title('Squared Numbers', fontsize=24)
graph.set_xlabel('Value', fontsize=14)
graph.set_ylabel('Sqares', fontsize=14)
graph.tick_params(labelsize=14)
graph.axis([1, 10_000, 1, 100_000_000])
graph.ticklabel_format(axis='y', style='plain')
plt.show()