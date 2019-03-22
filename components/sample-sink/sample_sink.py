from parallelm.components import ConnectableComponent


class SampleSink(ConnectableComponent):

    def __init__(self, engine):
        super(self.__class__, self).__init__(engine)

    def _materialize(self, parent_data_objs, user_data):
        expected_str_value = self._params.get('expected-value', "default-string-value")
        actual_value = parent_data_objs[0]
        self._logger.info("String Sink, Got:[{}] Expected: [{}] ".format(actual_value, expected_str_value))
        if expected_str_value != actual_value:
            raise Exception("Actual [{}] != Expected [{}]".format(actual_value, expected_str_value))
        return []
