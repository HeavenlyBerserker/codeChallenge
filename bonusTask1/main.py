import sys

def main(argv):
	#Reading in projects and dependencies
	f = 0
	if(len(argv) >= 1):
		print("----------------\nFile:", argv[0],"\n----------------")
		f = open(argv[0], 'r')
	else:
		print("----------------\nFile: in.txt.\nOpened default file in.txt.\n----------------")
		f = open("in.txt", 'r')

	projects = f.readline().rstrip('\n').split(',')
	print("Input projects:", projects)
	
	dependencies = f.readline().rstrip('\n').split()

	for i in range(len(dependencies)):
		dependencies[i] = dependencies[i].split(',')

	print("Input dependencies:",dependencies)

	f.close()

	#Running algo
	lastproj = projects.copy()
	times = 1
	while(not satisfied(projects,dependencies)):
		print("Iteration #", times)
		for d in dependencies:
			before = projects.index(d[0])
			after = projects.index(d[1])
			if(before > after):
				print("Swapped", projects[before], "with", projects[after], "result", projects)
				temp = projects[after]
				projects[after] = projects[before]
				projects[before] = temp
		if(projects == lastproj):
			print("No solution")
			break
		lastproj = projects.copy()
		times += 1

	if(satisfied(projects,dependencies)):
		print("Solution:", projects)
	
def satisfied(proj, dep):	
	for d in dep:
		before = proj.index(d[0])
		after = proj.index(d[1])
		if(before > after):
			return False
	return True
	

if(__name__ == "__main__"):
	main(sys.argv[1:])
