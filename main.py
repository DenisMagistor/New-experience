from operator import mod
import modules
import analitics

if __name__ == '__main__':
    modules.create_table()
    modules.add_data(modules.generator_data(10))