import codecademylib
from matplotlib import pyplot as plt
import numpy as np

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#make your pie chart here
# Legend can be added with
# plt.legend(payment_method_names)
# or
# plt.pie(payment_method_freqs, labels=payment_method_names)
#
# autopct opion adds the percentage of each slice
# '%0.2f' — 2 decimal places, like 4.08
# '%0.2f%%' — 2 decimal places, but with a percent sign at the end, like 4.08%
# '%d%%' — rounded to the nearest int and with a percent sign at the end, like 4%
#

plt.pie(payment_method_freqs, labels=payment_method_names, autopct='%0.1f%%')
plt.legend(payment_method_names)
plt.axis('equal')

plt.show()