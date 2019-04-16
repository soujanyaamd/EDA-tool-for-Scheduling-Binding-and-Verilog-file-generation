This Folder contains the required csv files.

### 1. input.csv:

This file contains the dataflow in a matrix format.

| Column Name | Description |
| --- | --- |
| SERIAL NUM | Assigns an identity to each operation |
| OPERATOR | Specifies the hardware required to perform the operation |
| INPUT 1 | Names the first input required to operate |
| TYPE 1 | Specifies whether the input 1 is independent or depends on previous outputs |
| NATURE1 | Specifies whether the input 1 is a variable or constant |
| BITS 1 | Specifies the number of bits in input 1 |
| INPUT 2 | Names the second input required to operate |
| TYPE 2 | Specifies whether the input 2 is independent or depends on previous outputs |
| NATURE2 | Specifies whether the input 2 is a variable or constant |
| BITS 2 | Specifies the number of bits in input 2 |
| OUTPUT | Assigns a name to the output of the operation |
| BITS OP | Specifies the number of bits in output |
| OPERATION | Specifies whether the operation performed on the inputs to obtain the output |

### 2. operators.csv

This file contains the resource and timing constraints of each operator

| Column Name | Description |
| --- | --- |
| TYPE OF OP | Names the hardware |
| NUM OF UNITS | Specifies the number of units of that hardware present on the chip |
| TIME REQUIRED IN NANO SECONDS | Specifies the time required to complete one such operation |

### 3. operators1.csv

This file is similar to operators.csv, and contains a different contraints set.
