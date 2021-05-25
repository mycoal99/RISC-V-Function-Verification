for i in {1..20} # Create 250 samples of running through modelsim
do
    echo "$i iteration"
    # Call python code here to generate machine code
    python trees.py
    cat vsim_commands.txt | vsim -c > out.txt

	# Call python code here to add features and class to csv file
	python learnedCoverpoint.py
done

for i in {1..20} # Create 250 samples of running through modelsim
do
    echo "$i iteration"
    # Call python code here to generate machine code
    python addSigned.py
    cat vsim_commands.txt | vsim -c > out.txt

	# Call python code here to add features and class to csv file
	python learnedCoverpoint.py
done
for i in {1..20} # Create 250 samples of running through modelsim
do
    echo "$i iteration"
    # Call python code here to generate machine code
    python subNegativeTree.py
    cat vsim_commands.txt | vsim -c > out.txt

	# Call python code here to add features and class to csv file
	python learnedCoverpoint.py
done
for i in {1..20} # Create 250 samples of running through modelsim
do
    echo "$i iteration"
    # Call python code here to generate machine code
    python mulZeroTree.py
    cat vsim_commands.txt | vsim -c > out.txt

	# Call python code here to add features and class to csv file
	python learnedCoverpoint.py
done
for i in {1..20} # Create 250 samples of running through modelsim
do
    echo "$i iteration"
    # Call python code here to generate machine code
    python xorZeroTree.py
    cat vsim_commands.txt | vsim -c > out.txt

	# Call python code here to add features and class to csv file
	python learnedCoverpoint.py
done

for i in {1..20} # Create 250 samples of running through modelsim
do
    echo "$i iteration"
    # Call python code here to generate machine code
    python xorOneTree.py
    cat vsim_commands.txt | vsim -c > out.txt

	# Call python code here to add features and class to csv file
	python learnedCoverpoint.py
done

