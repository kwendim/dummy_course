#This is a template for the grader

from onpit import Grader

class LabGrader(Grader):
	@Grader.addStep(name='step1')
	def step1(self, workingDir, inputCommand):
	    return True

	@Grader.addStep(name='step2')
	def step2(self, workingDir, inputCommand):
	    return True

	@Grader.addStep(name='step3')
	def step3(self, workingDir, inputCommand):
	    return True

	@Grader.addStep(name='step4')
	def step4(self, workingDir, inputCommand):
	    return True

