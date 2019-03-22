from parallelm.components import ConnectableComponent
from parallelm.mlops import mlops


class SampleSource(ConnectableComponent):

    def __init__(self, engine):
        super(self.__class__, self).__init__(engine)

    def _materialize(self, parent_data_objs, user_data):
        str_value = self._params.get('value', "default-string-value")
        for x in range(100):
            mlops.set_stat("Sample line graph", x + 10 if x % 2 == 0 else x - 1)
        return [str_value]
