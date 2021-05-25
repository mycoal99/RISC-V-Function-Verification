import randomFeatureChooser
import Assembler
import csv

#stores instruction into text and fills out csv table

def instructionStore(featureObj): #format instructions and write to instruction file
	instruction = 'lw $t1, 0x0C($zero)\nlw $t2, 0x10($zero)\n'

	instruction += featureObj.instructionFeature + ' ' + '$t3, $t1, $t2' '\n'
	instruction += featureObj.V1 + '\n'
	instruction += featureObj.V2 + '\n' #will newline be an issue?

	file = open("test.asm","w") #write to instructions.txt
	file.write(instruction)
	file.close()

	assembler = Assembler.Assembler()
	assembler.read_file("test.asm")
	assembler.write_file("machinecode.txt")
