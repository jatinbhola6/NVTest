randomGenerator.py:
	this python file has a function 'generateRandom'.
	It takes two arguments:
		1. 'max' which is the maximum limit of required random number
		2. 'highPrcnt' which is the percent of bias toward bigger number than half of max
	It return a random number.
	Approach:
		It generates two lists of size (max/2) each. One contaiing numbers bigger than max/2 and other less than max/2. Then it chooses a list between those two lists randomly using timestamp of the system. It takes the timestamp, take the last two digits of decimal part and check if it is smaller than highPrct. If true it selects array with bigger numbers else the other one. Next, to choose a random number from the selected list, it again takes the timestamp, convert it to integer and takes modulus with length of selected array. This result is used as index of selected array to get a random number.

parseJson.py:
	this python file has a function 'parseIt'.
	It takes three arguments:
		1. orignal quantity value 'orig_quant'
		2. target quantity value 'trgt_quant'
		3. path of json file 'json_path'
	It doesnt return any thing but stores updated json in file 'return.json'.
	Approach:
		On loading json file, it reads it as a dictionary and traverse on its keys. If current key is "quantity", it performs a mathematical operation to convert it into desired value. Else if the current value is of dictionary type, it recursively calls itself and pass current value to it. If value is a list, it iterates on that list and pass each dictionary value to itself. It dump the updated json in file 'result.json'

 
