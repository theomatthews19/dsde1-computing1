class TDIDF:
    def __init__(self, path):
        self.path = path
        self.docs_tf = {}
        self.tf = self.read_file(self.read)

        return docs_tf

    def read_file(self, path):
        with open(path) as f:
            new = f.read()
        outp = new.strip()
        return outp

    def string_to_list(self):
        import string
        new = strng.split = ()
        outp = []
        for i in new:
            freq
            
    def compute_tf(a_string):
        string_dict = {}
        for word in a_string.split():
            if word in string_dict:
                string_dict[word] += 1
            else:
                string_dict[word] = 1
    return string_dict