# RISC-V-Function-Verification

<details open='open'>
  <summary>Table of Contents</summary>
  <ul>
    <li>
      <a href=#project-goals>Project Goals</a> 
    </li>
    <li>
      <a href=#procedure>Procedure</a>
  </ul>
</details>

## Project Goals
The goal of this project is to examine key cases where the RISC-V processor will fail by
randomly generating test cases to train a machine learning model in order to help create tests that will
trigger failure cases.

## Procedure
Randomly generate test cases while constraining the test
cases to features that will likely trigger failure cases.

Coverpoints to hit:

'COVERPOINT_ADD_UNSIGNED_OVERFLOW',

'COVERPOINT_ADD_SIGNED_OVERFLOW',

'COVERPOINT_SUB_NEGATIVE',

'COVERPOINT_MUL_ZERO', 'COVERPOINT_XOR_ZERO',

'COVERPOINT_XOR_ALL_ONES'

After the randomly generated test cases are converted into machine code using the provided
assembler, ModelSim is used to test which coverpoints are hit and the results are put into
‘coverpoint.csv’. The results are then inputted into the scikit machine learning model provided to
generate decision trees that help decide whether a test case should trigger a certain coverpoint.
Once the decision tree functions are implemented in a Python file, tests are generated
according to the decision trees in order increase the coverpoint hit rate.

Rule learner first converts the data in the labels and training data csvs into matrices, and processes the data by running it through a decision tree
based machine learning model to generate rules that will be used to hopefully constrain tests to
be more useful in hitting coverpoints.

