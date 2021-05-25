for i in {1..2} # Create 250 samples of running through modelsim
do
    echo "$i iteration"
    # Call python code here to generate machine code
    python main.py
    cat vsim_commands.txt | vsim -c > out.txt

	# Call python code here to add features and class to csv file
	python coverpoint.py
done
