## BRAC University Grade Sheet Downloadinator

This is a Python script that can be used to download any student's BRAC University grade sheet. It simplifies the
process of accessing the grade sheet of any students which is a known issue with usis for a long time.

### Requirements

In order to get the .env values for your **Username** and **Password**, we need the **python-dotenv** package. To
install, use the followng command in the terminal:

```bash
pip install python-dotenv
```

### Usage

To use the script, run the following command in the terminal:

#### Without Environment Variables:

```bash
python main.py <username> <password> <student_id>
```

#### With Environment Variables:

```bash
python main.py <student_id>
```

#### Or simply run:

```bash
python main.py
```

Replace `<username>` and `<password>` with your BRAC University login credentials, and `<student_id>` with the student
ID of the grade sheet you want to download.

### Create Environment File

To keep your credentials and other sensitive information separate from your code, it's a good practice to create an
environment file. Here's how you can create an .env file and add your credentials to it:

- Create a new file in your project directory called .env, and open it in a text editor.
- In the .env file, add the following lines, replacing USERNAME and PASSWORD with your USIS login credentials:

```env
USIS_USERNAME={USERNAME}
USIS_PASSWORD={PASSWORD}
```

- Note that the .env file should not be committed to your version control system, as it may contain sensitive
  information.

- Save the .env file.

### Disclaimer

This script is provided for educational purposes only. The use of this script to automate the evaluation process may
violate the terms of service of BRAC University. Please use this script responsibly and at your own risk. The author of
this script is not responsible for any consequences that may arise from the use of this script.