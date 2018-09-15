import pandas
import numpy
import random
import string

#combine random strings/integers into a string for selection by numpy

random_strings = []

total_random_string = string.letters + '0123456789'
total_random_array = list(total_random_string)

random_strings = []

for idx in range(0, 1000):
  random_string = numpy.random.choice(total_random_array, random.randint(1, 12))
  random_strings.append(''.join(random_string))

random_normal_dist = numpy.random.randn(1000)
random_iq_scale = numpy.random.normal(100, 15, 1000)
random_uniform_dist = numpy.random.uniform(0.0, 1.0, 1000)

print random_strings

first_test_dictionary = {'rand_strings': random_strings, 'rand_normal_dist': random_normal_dist,
'rand_iq_scale': random_iq_scale, 'rand_uniform_dist 0.0-1.0': random_uniform_dist}

sample_dataframe = pandas.DataFrame(data = first_test_dictionary, columns = ['rand_strings', 'rand_normal_dist', 'rand_iq_scale', 'rand_uniform_dist 0.0-1.0'])

print sample_dataframe

