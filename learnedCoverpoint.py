import csv
import os


if __name__ == '__main__':

	coverPointList = ['COVERPOINT_ADD_UNSIGNED_OVERFLOW', 'COVERPOINT_ADD_SIGNED_OVERFLOW', 'COVERPOINT_SUB_NEGATIVE', 'COVERPOINT_MUL_ZERO', 'COVERPOINT_XOR_ZERO', 'COVERPOINT_XOR_ALL_ONES'] #These are all of the coverpoints

	coverPointRow = [0] * 6
	if not os.path.exists('learnedCoverpoint.csv'):
		with open('learnedCoverpoint.csv','w') as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow(coverPointList)


	#featureObj.csvFeatureArray[featureObj.instructionFeatureType.index(featureObj.instructionFeature)] = 1
	
	with open('out.txt','r') as file:
		filecontent = file.read()

	with open('learnedCoverpoint.csv','a') as csv_file:
		writer = csv.writer(csv_file)
		for coverpoint_name in coverPointList:
			print(filecontent)
			if coverpoint_name in filecontent:
				print("Coverpoint {} was hit!".format(coverpoint_name))
				coverPointRow[coverPointList.index(coverpoint_name)] = 1
		writer.writerow(coverPointRow)



