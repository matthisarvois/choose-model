from sklearn import datasets

def load_data():
    data =  datasets.load_breast_cancer(as_frame=True)
    data_frame = data.frame
    data_frame.columns = (
        data_frame.columns
            .str.lower()
            .str.normalize('NFKD')
            .str.encode('ascii', errors='ignore')
            .str.decode('utf-8')
            .str.replace(' ', '_')
            .str.replace(r'[^a-z0-9]', '_', regex=True)
    ) 
    return data_frame

dataset = load_data()
print(dataset.columns)
