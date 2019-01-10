from progress.bar import Bar
import time

bar = Bar('Processing', max=10000, fill='#', suffix='%(percent)d%%')
for i in range(10000):
	#time.sleep(0.1)
	bar.next()
bar.finish()

