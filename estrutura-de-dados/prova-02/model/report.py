import csv, os
import gc
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

        self.time_execution_insert_media = 0
        self.time_execution_search_media = 0
        self.time_execution_remove_media = 0

        self.time_execution_insert_standart_derivation = 0
        self.time_execution_search_standart_derivation = 0
        self.time_execution_remove_standart_derivation = 0

        self.comparisions_insert_media = 0
        self.comparisions_search_media = 0
        self.comparisions_remove_media = 0

        self.comparisions_insert_standard_derivation = 0
        self.comparisions_search_standard_derivation = 0
        self.comparisions_remove_standard_derivation = 0
    
    def consolidate_insertion(self):
        self.time_execution_insert_media = self.__get_media(self.time_execution_insert, True)
        self.time_execution_insert_standart_derivation = self.__get_standard_derivation(self.time_execution_insert, True)

        self.comparisions_insert_media = self.__get_media(self.comparisions_insert)

        self.comparisions_insert_standard_derivation = self.__get_standard_derivation(self.comparisions_insert)

        del self.time_execution_insert
        del self.comparisions_insert
        gc.collect()

    def consolidate_search(self):
        self.time_execution_search_media = self.__get_media(self.time_execution_search, True)
        self.time_execution_search_standart_derivation = self.__get_standard_derivation(self.time_execution_search, True)

        self.comparisions_search_media = self.__get_media(self.comparisions_search)
        self.comparisions_search_standard_derivation = self.__get_standard_derivation(self.comparisions_search)

        del self.time_execution_search
        del self.comparisions_search
        gc.collect()

    def consolidate_remove(self):
        self.time_execution_remove_media = self.__get_media(self.time_execution_remove, True)
        self.time_execution_remove_standart_derivation = self.__get_standard_derivation(self.time_execution_remove, True)

        self.comparisions_remove_media = self.__get_media(self.comparisions_remove)
        self.comparisions_remove_standard_derivation = self.__get_standard_derivation(self.comparisions_remove)

        del self.time_execution_remove
        del self.comparisions_remove
        gc.collect()

    def create_report(self):
        print(f'[{self.algo_name}] - generating report...')
        path = './generated_csvs'
        if not os.path.exists(path):
            os.makedirs(path)
        file = open(f'{path}/{self.algo_name}_{self.array_size}_{self.array_type}.csv', 'w')
        writer = csv.writer(file)

        header_default = ['Nome do Algoritmo', 'Tamanho do Arranjo', 'Cenário testado']
        header_media_time = ['Media de tempo de execucao - Inserção (Segundos)', 'Media de tempo de execucaoo - Pesquisa (Segundos)', 'Media de tempo de execucao - Remocao (Segundos)']
        header_media_standard_derivation = ['Desvio Padrao de tempo de execucao - Inserção (Segundos)', 'Desvio Padrao de tempo de execucaoo - Pesquisa (Segundos)', 'Desvio Padrao de tempo de execucao - Remocao (Segundos)']
        header_media_comparisions =  ['Media de comparações - Inserção', 'Media de comparações - Pesquisa', 'Media de comparações - Remocao']
        header_standard_derivation_comparisions =  ['Desvio Padrao de comparações - Inserção', 'Desvio Padrao de comparações - Pesquisa', 'Desvio Padrao de comparações - Remocao']

        data_default = [self.algo_name, self.array_size, self.array_type]
        data_media_time = [
            self.time_execution_insert_media,
            self.time_execution_search_media,
            self.time_execution_remove_media]

        data_standard_derivation_time = [
            self.time_execution_insert_standart_derivation,
            self.time_execution_search_standart_derivation,
            self.time_execution_remove_standart_derivation]

        data_media_comparisions = [
            self.comparisions_insert_media,
            self.comparisions_search_media,
            self.comparisions_remove_media]

        data_standard_derivation_comparisions = [
            self.comparisions_insert_standard_derivation,
            self.comparisions_search_standard_derivation,
            self.comparisions_remove_standard_derivation]

        writer.writerow(header_default + header_media_time + header_media_standard_derivation + header_media_comparisions + header_standard_derivation_comparisions)
        writer.writerow(data_default + data_media_time + data_standard_derivation_time  + data_media_comparisions + data_standard_derivation_comparisions)

        file.close()
        gc.collect()
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
