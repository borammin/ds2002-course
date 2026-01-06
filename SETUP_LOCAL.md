## Python and utility tools

This course will introduce several software tools:
- htop
- curl
- wget
- jq
- awsclient
- python
- docker
- VSCode

In addition you will use VSCode as an integrated development environment for your coding.


### Option 1: GitHub Codespaces (easiest, recommended)


**Skip to step 5.**

### Option 2: Local installation

To set up your own computer for all course activities I highly encourage you to create n If you want to install all the software tools in a new environment. Think of an environment as an isolated area to install the software packages you need for a specific project, i.e. in this case the course activities. Packages in an environment are isolated from other software packages on your computer. An environment
   - **Best practice:** create a new evironment for each of your projects.
   - **Isolation:** is typically defined in a specific folder on your computer.
   - **Experimentation:** allows experimenting with installation of new packages without disrupting packages in other environments 
   - **Multiple projects:** allows to manage conflicting packages in sepatere environments

You will need to install the following software tools.

**Windows**

Since we're using the Linux command line, you will need to install a Linux-like terminal program. I recommend installing Git-Bash which provides the Linux-style terminal and also Git.

1. Install Git-Bash: Download and install Git-Bash from the [official Git website](https://git-scm.com/downloads).
2. Download the Miniforge Installer: Go to the [conda-forge Miniforge GitHub repository](https://github.com/conda-forge/miniforge) and download the Windows executable file (Miniforge3-Windows-x86_64.exe).
3. Run the Executable Installer: Double-click the downloaded .exe file to run the installer.
   - Follow the prompts, accepting the license agreement.
   - It is highly recommended to install for "Just Me" (per user) to avoid potential permission issues later.
   - Note the installation path: The default installation path is usually within your AppData\Local folder (e.g., C:\Users\YOUR_USERNAME\AppData\Local\miniforge3). Remember this location.
   - Check the "Create start menu shortcuts" option. The most convenient and tested way to use the installed software (such as commands conda and mamba) is via the "Miniforge Prompt" installed to the start menu.
   - Check the "Add Miniforge3 to my PATH environment variable" option. 
4. Create a conda (mamba) environment. In your terminal execute the following command
   ```bash
   mamba env create -n ds2002 -c conda-forge python=3.11 htop jq awscli curl wget git zip unzip tar redis-server redis-py mongodb
   ```
5. Configure Git Bash: After the installation is complete, you need to configure Git Bash to recognize the conda commands.
   - Open your Git Bash terminal.
   - Open your ~/.bashrc file in a text editor (e.g., nano ~/.bashrc or notepad ~/.bashrc). If it doesn't exist, create it.
   - Add the following lines to the end of the file. Adjust the path if you installed Miniforge in a non-default location (see step 3):
      ```bash
      # Miniforge initialization code
      echo "source ~/AppData/Local/miniforge3/etc/profile.d/conda.sh" >> ~/.bashrc
      echo "conda activate ds2002
      ```
   - Save the file and close your text editor.
6. Restart Git Bash and Verify:
   - Close and re-open your Git Bash terminal for the changes to take effect.
   - To verify the installation, run the command `conda list`. You should see a list of installed packages, and your prompt might show (base) at the beginning, confirming that the base environment is active.
   - You can now use conda and mamba commands within your Git Bash terminal to manage environments and install packages.


**MacOS, Linux**

MacOS and Linux have terminal applications pre-installed. So you won't need Git-Bash. Follow these steps to install miniforge for Python.

1. Open a terminal window.
2. Download the installer script: The command below automatically detects your system's architecture and downloads the correct Miniforge3 installer from the official conda-forge GitHub repository.
   ```bash
   curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh
   ```
   **Note:** For some specific macOS architectures (like Apple Silicon/arm64), the command might be slightly different; you can check the [Miniforge GitHub page](https://github.com/conda-forge/miniforge) for direct links if the automatic detection fails.
3. Run the installation script: Execute the downloaded script using bash.
   ```bash
   bash Miniforge3-$(uname)-$(uname -m).sh
   ```
   Alternatively, if the automatic detection in the filename does not work, you can use a fixed filename after downloading it, for example:
   ```bash
   bash Miniforge3.sh
   ```
   Follow the prompts: The installer will guide you through the process.
   - Press ENTER or return to view the license agreement.
   - Scroll through the license and type `yes` to accept the terms.
   - Confirm the default installation location (typically ~/miniforge3). Press ENTER to accept it.
   - When asked if you want to initialize Conda for your shell (e.g., bash or zsh), type `yes`.
4. Restart your terminal: For the changes to take effect, close your current terminal window and open a new one.
5. Verify the installation:
   - Once the terminal is restarted, you should see `(base)` in your terminal prompt, indicating the Miniforge base environment is active.
   - Run the following command to verify:
     ```bash
     conda list
     ```
   - If a list of installed packages appears without errors, the installation was successful. 
6. Create a conda (mamba) environment and install the other software packages. In your terminal execute the following command:
   ```bash
   mamba env create -n ds2002 -c conda-forge python=3.11 htop jq awscli curl wget git zip unzip tar redis-server redis-py mongodb
   ```

## Step 5: First steps

Once your codespace is running, open the terminal and try these basic commands:

1. Check your current location:
   ```bash
   pwd
   ```

2. List files and directories:
   ```bash
   ls
   ```

3. Check git status:
   ```bash
   git status
   ```

4. Verify Python is installed:
   ```bash
   python --version
   ```

These commands help you verify your environment is set up correctly and get familiar with the terminal.