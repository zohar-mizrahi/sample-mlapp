import time

from parallelm.components import ConnectableComponent
from parallelm.mlops import mlops
from parallelm.mlops.stats.multi_line_graph import MultiLineGraph
from parallelm.mlops.stats.table import Table
from parallelm.mlops.stats.bar_graph import BarGraph


class SampleSource(ConnectableComponent):

    def __init__(self, engine):
        super(self.__class__, self).__init__(engine)

    def _materialize(self, parent_data_objs, user_data):
        str_value = self._params.get('value', "default-string-value")
        self._demo_stats()
        return [str_value]

    def _demo_stats(self):
        self._demo_line_graph()
        self._demo_multi_line_graph()
        self._demo_table()
        self._demo_bar_graph()

    def _demo_line_graph(self):
        self._logger.info("Demo line graph ...")
        for x in range(100):
            mlops.set_stat("Line graph example", x + 10 if x % 2 == 0 else x - 1)
        self._logger.info("Demo line graph done!")

    def _demo_multi_line_graph(self):
        self._logger.info("Demo multi-line graph ...")
        mlt = MultiLineGraph().name("Multi-line graph example").labels(["l1", "l2", "l3"])
        for x in range(100):
            mlt.data([11 + x, 23 - x, 0.5 * x])
            mlops.set_stat(mlt)
        self._logger.info("Demo multi-line done!")

    def _demo_table(self):
        self._logger.info("Demo table ...")
        tbl = Table().name("Table example").cols(["Worker", "Requests"])
        for index in range(0, 10):
            tbl.add_row(["worker-{}".format(index), index + 3])
        mlops.set_stat(tbl)
        self._logger.info("Demo table done")

    def _demo_bar_graph(self):
        mlt = BarGraph().name("Bar graph example").cols(["g1", "g2"]).data([1.1, 2.4])
        mlops.set_stat(mlt)
