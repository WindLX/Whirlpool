## Whirlpool

A command-line tool for converting **png ico jpg** format files into **png ico jpg** format files in batches.

*version 0.1.0*

### Dependency

1. Python 3.9.13 or higher
2. PowerShell 7.1.1 or higher
3. Python packages in requirements.txt

### How to Use

1. Make sure you have **Python** and **Powershell** on your computer.

2. Please set the **WhirlpoolPath** in **settings.json** to the absolute path of your Whirlpool, the default path is *"D:\\\\Whirlpool"* .

3. Run **wht.ps1** in your PowerShell.

4. This script automatically configures Python's virtual environment in the Whirlpool directory if you are using it for the first time and downloads the required libraries using pip.

5. The Powershell script has five parameters:

    + **-Path** The path of folder which storages your target pictures.
    + **-IsHidden** Change the presentation form of work progress.
    + **-Size** The size of output pictures, only effective when target type is ico.
    + **-RawType** The raw type of pictures, such as png jpg ico.
    + **-TargetType** The target type of pictures, such as png jpg ico.

    You can use `Get-Help .\wht.ps1` for details.

6. An example is

    ```powe
    .\wht.ps1 . 0 128 png ico
    ```

7. The result will be stored in *".\whirlpool_result"*.
