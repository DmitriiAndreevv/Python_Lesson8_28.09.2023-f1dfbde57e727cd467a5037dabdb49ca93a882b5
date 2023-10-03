import pickle

def load_pickle(filename):
    with open(filename, 'rb') as pickle_file:
        return pickle.load(pickle_file)

def save_pickle(data, filename):
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)
