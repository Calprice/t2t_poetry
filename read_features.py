import tensorflow as tf

# https://planspace.org/20170323-tfrecords_for_humans/

# This explains how to read the tfrecords that are written by the tensor2tensor application

# as you can see the outputs are the indices


data_path = '/home/fciannel/src/t2t/t2t_testing_pycharm/t2t_data/poetry_line_problem-train-00001-of-00090'

reader = tf.python_io.tf_record_iterator(data_path)
those_examples = [tf.train.Example().FromString(example_str) for example_str in reader]


# We can generate the vocabulary from the file
vocab = {}
with open('/home/fciannel/src/t2t/t2t_testing_pycharm/t2t_data/vocab.poetry_line_problem.8192.subwords', 'r') as f:
    lines = f.readlines()
    for l in enumerate(lines):
        vocab[l[0]] = l[1].strip()

# and we can now see the examples
for example in those_examples:
    inputs = example.features.feature['inputs'].int64_list.value
    targets = example.features.feature['targets'].int64_list.value

    try:
        for input in inputs:
            print(vocab[input])
        for target in targets:
            print(vocab[target])
    except:
        print(inputs, targets)
