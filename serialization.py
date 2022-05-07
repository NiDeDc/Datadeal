import pickle


class DataBase:
    def __init__(self):
        self.b = 500


p_bytes = pickle.dumps(DataBase())
print(type(p_bytes), p_bytes)
p_obj: DataBase = pickle.loads(p_bytes)
print(p_obj.b)
print(type(p_obj), p_obj)
