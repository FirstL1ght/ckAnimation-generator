# ckAnimation generator 2.0

[***README.md на русском***](https://github.com/FeelinVoids/ckAnimation-generator/blob/master/README.md)
 
These scripts allow you to generate lighting animation files for some keyboards from A4 Bloody. Tested on Bloody B975, should work on similar models with RGB backlit. By modifying algorithms.py, you can modify or write your own animations by inheriting the `AlgorithmBase` class.

### WARNING! 
If you decide to try these scripts - YOU DO EVERYTHING AT YOUR OWN RISK! If suddenly something happens to your keyboard or computer, you are solely responsible for this.

## Installation:

    pip install git+https://github.com/FeelinVoids/ckAnimation-generator.git

Now the command `ckAnimationGenerator`, which starts the program, will become available in the cmd.

At startup, you will be prompted to enter a file name, but you can skip this by pressing Enter. Next, the program will require you to enter the number of the desired algorithm from the list, after which a file will be generated (the Waves algorithm also requires you to enter the color code). After that, the path to the animation file will be displayed. The file should be imported into KeyDominator2 in the RGB Animation tab and assigned to the Fn slot from 0 to 9 in the table.

![Import](https://i.imgur.com/66R2urN.png)

![Waves](https://i.imgur.com/gO0a5b3.gif)

![Starfall](https://i.imgur.com/Og8kqrh.gif)
