import csv, os
import numpy as np

class Report:

    def __init__(self, array_size, algo_name, array_type) -> None:
        self.array_size = array_size
        self.array_type = array_type
        self.algo_name = algo_name
        self.comparisions_insert = []
        self.comparisions_search = []
        self.comparisions_remove = []
        self.time_execution_insert = []
        self.time_execution_search = []
        self.time_execution_remove = []

    def create_report(self):
        print(f'[{self.algo_name}] - generating report...')
        path = './generated_csvs'
        if not os.path.exists(path):
            os.makedirs(path)
        file = open(f'{path}/{self.algo_name}_{self.array_size}_{self.array_type}.csv', 'w')
        writer = csv.writer(file)

        header_default = ['Nome do Algoritmo', 'Tamanho do Arranjo', 'Cenário testado']
        header_media_time = ['Media de tempo de execucao - Inserção (Segundos)', 'Media de tempo de execucaoo - Pesquisa (Segundos)', 'Media de tempo de execucao - Remocao (Segundos)']
        header_media_comparisions=  ['Media de comparações - Inserção', 'Media de comparações - Pesquisa', 'Media de comparações - Remocao']

        data_default = [self.algo_name, self.array_size, self.array_type]
        data_media_time = [
            self.__get_media(self.time_execution_insert, True),
            self.__get_media(self.time_execution_search, True),
            self.__get_media(self.time_execution_remove, True)]

        data_media_comparisions = [
            self.__get_media(self.comparisions_insert),
            self.__get_media(self.comparisions_search),
            self.__get_media(self.comparisions_remove)]

        writer.writerow(header_default + header_media_time + header_media_comparisions)
        writer.writerow(data_default + data_media_time + data_media_comparisions)

        file.close()
        print('report generated')
        print('------------------------------------------------------------------')
        print('')

    def __get_media(self, sum_a, limit=False):
        if limit:
            return f'{np.average(sum_a):.10f}'
        return np.average(sum_a)

    def __get_standard_derivation(self, sum_a, limit_in=0):
        if limit_in:
            return f'{np.average(sum_a):.10f}'
        return np.std(sum_a)
